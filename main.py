from interaction.steps.interpretation import interpret
from interaction.steps.confidence import evaluate
from interaction.steps.reasoning import reason
from interaction.steps.response_selection import select
from interaction.steps.response_execution import execute

user_input = input('> ')
signals = interpret(user_input)
confidence = evaluate(signals)
reasoning_output = reason(signals, confidence)
response_type = select(confidence, signals, reasoning_output)
response = execute(response_type, user_input)

print({
    'signals': signals,
    'confidence': confidence,
    'reasoning': reasoning_output,
    'response_type': response_type,
    'response': response
})
