from initGPT import chat

def getAIResponse(newMessage):
    response = chat.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": newMessage,
            },
        ],
        temperature=1,
        max_tokens=256,
    )
    reply = response.choices[0].message.content
    return reply

