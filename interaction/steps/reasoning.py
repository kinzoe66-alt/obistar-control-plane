from interaction.steps.classification import classify

def reason(user_input, signals, confidence, memory):
    alignment = signals.get('alignment')
    clarity = signals.get('clarity')
    intent = signals.get('intent_strength')
    correction = signals.get('correction_signal')

    task_type = classify(user_input)
    history = memory.get("history", [])

    last = history[-1] if history else None



    if last:

        if "continue" in user_input.lower():

            return {

                'situation': 'VALID_ACTION',

                'task_type': task_type,

                'context_used': True

            }


    if correction:
        return {'situation': 'CORRECTION', 'task_type': task_type}

    if alignment == 'low' and intent == 'high':
        return {'situation': 'INVALID', 'task_type': task_type}

    if clarity == 'low':
        return {'situation': 'UNCLEAR', 'task_type': task_type}

    return {'situation': 'VALID_ACTION', 'task_type': task_type}
