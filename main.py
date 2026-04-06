from interaction.steps.interpretation import interpret
from interaction.steps.confidence import evaluate

user_input = input('> ')
signals = interpret(user_input)
confidence = evaluate(signals)

print({
    'signals': signals,
    'confidence': confidence
})

