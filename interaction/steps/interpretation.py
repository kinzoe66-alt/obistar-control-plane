def interpret(text):
    lowered = text.lower().strip()

    correction_signal = any(word in lowered for word in ["no", "wrong", "actually", "instead", "correction"])

    if len(lowered.split()) <= 2:
        clarity = 'low'
    elif any(word in lowered for word in ["system", "thing", "stuff"]) and len(lowered.split()) < 5:
        clarity = 'low'
    else:
        clarity = 'medium'

    if any(word in lowered for word in ["build", "make", "create", "help", "fix"]):
        intent_strength = 'high'
    else:
        intent_strength = 'medium'

    if any(word in lowered for word in ["api", "oauth", "system", "app", "website"]):
        alignment = 'high'
    else:
        alignment = 'low'

    return {
        'alignment': alignment,
        'clarity': clarity,
        'intent_strength': intent_strength,
        'correction_signal': correction_signal
    }
