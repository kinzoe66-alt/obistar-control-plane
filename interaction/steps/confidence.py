def evaluate(signals):
    clarity = signals.get('clarity')
    alignment = signals.get('alignment')

    if clarity == 'low' or alignment == 'low':
        return 'low'

    if clarity == 'medium':
        return 'medium'

    return 'high'

