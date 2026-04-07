import json
import os
import sys

MEMORY_PATH = "memory/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {"history": [], "execution_history": []}
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

def interpret(user_input):
    words = user_input.lower().split()
    return {
        "alignment": "high" if any(w.startswith("build") for w in words) else "low",
        "clarity": "high" if len(words) > 2 else "medium",
        "intent_strength": "high" if any(w in words for w in ["build","create","make"]) else "medium",
        "correction_signal": False
    }

def evaluate(signals):
    return "high" if signals["intent_strength"] == "high" else "medium"

def reason(user_input, signals, confidence, memory):
    user_input_lower = user_input.lower()

    last = memory["execution_history"][-1] if memory["execution_history"] else None

    if "continue" in user_input_lower and last:
        return {
            "situation": "VALID_ACTION",
            "task_type": "BUILD",
            "context_used": True
        }

    if "build" in user_input_lower:
        return {
            "situation": "VALID_ACTION",
            "task_type": "BUILD",
            "context_used": len(memory["history"]) > 0
        }

    if "what is" in user_input_lower:
        return {
            "situation": "UNKNOWN",
            "task_type": "EXPLAIN",
            "context_used": False
        }

    return {
        "situation": "UNKNOWN",
        "task_type": "UNKNOWN",
        "context_used": False
    }

def select(confidence, signals, reasoning_output):
    if reasoning_output.get("situation") == "VALID_ACTION" and reasoning_output.get("task_type") == "BUILD":
        return "guide"

    if signals["alignment"] == "high":
        return "guide"

    return "fallback"

def execute(response_type, user_input):
    if response_type == "guide":
        return f"Starting system build for: {user_input}"
    return f"I can't perform '{user_input}' — that request is outside my capabilities."

def classify_outcome(signals, reasoning_output, response):
    situation = str(reasoning_output.get("situation","")).upper()
    task_type = str(reasoning_output.get("task_type","")).upper()
    alignment = str(signals.get("alignment","")).lower()
    response_lower = response.lower()

    if "can't perform" in response_lower:
        return "REJECTED"

    if situation == "VALID_ACTION" and task_type == "BUILD":
        return "SUCCESS"

    if task_type == "EXPLAIN":
        return "MISALIGNED"

    if alignment == "low":
        return "FAILURE"

    return "UNCLASSIFIED"

def run_system(user_input):
    memory = load_memory()

    signals = interpret(user_input)
    confidence = evaluate(signals)
    reasoning_output = reason(user_input, signals, confidence, memory)

    response_type = select(confidence, signals, reasoning_output)
    response = execute(response_type, user_input)

    outcome = classify_outcome(signals, reasoning_output, response)

    observation = {
        "input": user_input,
        "response_type": response_type,
        "response": response,
        "outcome": outcome
    }

    memory["execution_history"].append(observation)
    memory["history"].append({
        "input": user_input,
        "response": response
    })

    save_memory(memory)

    return {
        "signals": signals,
        "confidence": confidence,
        "reasoning": reasoning_output,
        "response_type": response_type,
        "response": response,
        "outcome": outcome
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        print(run_system(user_input))
    else:
        while True:
            user_input = input(">>> ")
            if user_input.lower() in ["exit","quit"]:
                break
            print(run_system(user_input))
