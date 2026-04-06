def select(confidence, signals, reasoning_output):
    situation = reasoning_output.get('situation')
    task_type = reasoning_output.get('task_type')

    # hard stops
    if situation == 'INVALID':
        return 'reject'

    if situation == 'CORRECTION':
        return 'ask'

    # --- TASK-SPECIFIC TOLERANCE ---

    # EXPLAIN: allow ambiguity
    if task_type == 'EXPLAIN':
        return 'guide'

    # UNCLEAR (non-explain tasks)
    if situation == 'UNCLEAR':
        return 'ask'

    # VALID ACTIONS
    if situation == 'VALID_ACTION':
        if task_type == 'COMPUTE':
            return 'act'

        if task_type == 'BUILD':
            return 'guide'

        return 'ask'

    return 'ask'
