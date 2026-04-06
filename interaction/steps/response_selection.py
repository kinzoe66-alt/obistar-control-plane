def select(confidence):
    if confidence == 'low':
        return 'ask'
    if confidence == 'medium':
        return 'guide'
    if confidence == 'high':
        return 'act'
    return 'ask'
