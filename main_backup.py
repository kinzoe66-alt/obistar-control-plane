import sys

from interaction.steps.interpretation import interpret
from interaction.steps.confidence import evaluate
from interaction.steps.reasoning import reason
from interaction.steps.response_selection import select
from interaction.steps.response_execution import execute


def run_system(user_input):
    signals = interpret(user_input)
    confidence = evaluate(signals)
    reasoning_output = reason(user_input, signals, confidence)
    response_type = select(confidence, signals, reasoning_output)
    response = execute(response_type, user_input)

    return {
        "signals": signals,
        "confidence": confidence,
        "reasoning": reasoning_output,
        "response_type": response_type,
        "response": response
    }


if __name__ == "__main__":
    # CLI mode (for testing)
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
        output = run_system(user_input)
        print(output)

    # Interactive mode (your current behavior)
    else:
        user_input = input("> ")
        output = run_system(user_input)
        print(output)
