def execute(response_type, user_input):
    if response_type == 'ask':
        return "Can you clarify what you mean?"
    
    if response_type == 'guide':
        return f"Starting system build for: {user_input}"
    
    return "Unhandled response"
