from interaction.steps.classification import classify

def reason(user_input, signals, confidence):
    alignment = signals.get('alignment')
    clarity = signals.get('clarity')
    intent = signals.get('intent_strength')
    correction = signals.get('correction_signal')

    task_type = classify(user_input)

    if correction:
        return {'situation': 'CORRECTION', 'task_type': task_type}

    if alignment == 'low' and intent == 'high':
        return {'situation': 'INVALID', 'task_type': task_type}

    if clarity == 'low':
        return {'situation': 'UNCLEAR', 'task_type': task_type}

    return {'situation': 'VALID_ACTION', 'task_type': task_type}
