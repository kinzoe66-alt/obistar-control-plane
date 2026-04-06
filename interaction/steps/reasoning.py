def reason(signals, confidence):
    alignment = signals.get('alignment')
    clarity = signals.get('clarity')
    intent = signals.get('intent_strength')
    correction = signals.get('correction_signal')

    # correction always wins
    if correction:
        return {'situation': 'CORRECTION', 'task_type': 'UNKNOWN'}

    # invalid (impossible / outside scope)
    if alignment == 'low' and intent == 'high':
        return {'situation': 'INVALID', 'task_type': 'UNKNOWN'}

    # unclear
    if clarity == 'low':
        return {'situation': 'UNCLEAR', 'task_type': 'UNKNOWN'}

    # --- task classification (NEW) ---
    # lightweight + controlled
    task_type = 'UNKNOWN'

    # compute detection
    if any(x in str(signals).lower() for x in ['calculate', '+', '-', '*', '/']):
        task_type = 'COMPUTE'

    # explain detection
    elif any(x in str(signals).lower() for x in ['what is', 'explain']):
        task_type = 'EXPLAIN'

    # build / system
    elif any(x in str(signals).lower() for x in ['build', 'create', 'fix']):
        task_type = 'BUILD'

    return {'situation': 'VALID_ACTION', 'task_type': task_type}
