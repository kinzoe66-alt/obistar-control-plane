def execute(response_type, user_input):
    if response_type == 'ask':
        return "Can you clarify what you mean?"

    if response_type == 'guide':
        return f"Starting system build for: {user_input}"

    if response_type == 'act':
        try:
            # SAFE compute (only basic math)
            result = eval(user_input.replace('calculate', '').strip())
            return str(result)
        except:
            return f"Executing action for: {user_input}"

    if response_type == 'reject':
        return f"I can't perform '{user_input}' — that request is outside my capabilities."

    return "Unhandled response"
