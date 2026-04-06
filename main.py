from interaction.steps.interpretation import interpret
from interaction.steps.confidence import evaluate
from interaction.steps.response_selection import select
from interaction.steps.response_execution import execute

user_input = input('> ')
signals = interpret(user_input)
confidence = evaluate(signals)
response_type = select(confidence)
response = execute(response_type, user_input)

print({
    'signals': signals,
    'confidence': confidence,
    'response_type': response_type,
    'response': response
})
