import sys
import json
import os

from interaction.steps.interpretation import interpret
from interaction.steps.confidence import evaluate
from interaction.steps.reasoning import reason
from interaction.steps.response_selection import select
from interaction.steps.response_execution import execute

MEMORY_PATH = "memory/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return {
            "history": [],
            "execution_history": []
        }
    with open(MEMORY_PATH, "r") as f:
        memory = json.load(f)

    if "execution_history" not in memory:
        memory["execution_history"] = []

    if "history" not in memory:
        memory["history"] = []

    return memory

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)

def run_system(user_input):
    memory = load_memory()

    signals = interpret(user_input)
    confidence = evaluate(signals)
    reasoning_output = reason(user_input, signals, confidence)

    response_type = select(confidence, signals, reasoning_output)
    response = execute(response_type, user_input)

    # ✅ observation INSIDE function
    observation = {
        "input": user_input,
        "response_type": response_type,
        "response": response,
        "outcome": "UNCLASSIFIED"
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
        "response": response
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        print(run_system(user_input))
    else:
        user_input = input("> ")
        print(run_system(user_input))
