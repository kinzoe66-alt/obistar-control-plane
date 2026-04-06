def evaluate(signals):
    alignment = signals.get('alignment')
    clarity = signals.get('clarity')
    intent = signals.get('intent_strength')
    correction = signals.get('correction_signal')

    score = 0

    # alignment weight
    if alignment == 'high':
        score += 2
    elif alignment == 'medium':
        score += 1

    # clarity weight
    if clarity == 'high':
        score += 2
    elif clarity == 'medium':
        score += 1

    # intent strength weight
    if intent == 'high':
        score += 2
    elif intent == 'medium':
        score += 1

    # correction lowers confidence
    if correction:
        score -= 2

    # final decision
    if score >= 5:
        return 'high'
    elif score >= 3:
        return 'medium'
    else:
        return 'low'
