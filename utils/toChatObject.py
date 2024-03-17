def toUserObject(message, role):
    if role == "user":
        return {"role": "user", "content": message}
    elif role == "assistant":
        return {"role": "assistant", "content": message}