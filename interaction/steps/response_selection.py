def select(confidence, signals, reasoning_output):
    situation = reasoning_output.get('situation')
    task_type = reasoning_output.get('task_type')

    if situation == 'INVALID':
        return 'reject'

    if situation == 'UNCLEAR':
        return 'ask'

    if situation == 'CORRECTION':
        return 'ask'

    if situation == 'VALID_ACTION':
        if task_type == 'COMPUTE':
            return 'act'

        if task_type == 'BUILD':
            return 'guide'

        if task_type == 'EXPLAIN':
            return 'guide'

        return 'ask'

    return 'ask'
