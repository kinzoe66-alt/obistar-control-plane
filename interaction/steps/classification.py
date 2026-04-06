def classify(user_input):
    text = user_input.lower()

    if any(x in text for x in ['+', '-', '*', '/', 'calculate']):
        return 'COMPUTE'

    if any(x in text for x in ['explain', 'what is']):
        return 'EXPLAIN'

    if any(x in text for x in ['build', 'create', 'fix']):
        return 'BUILD'

    return 'UNKNOWN'
