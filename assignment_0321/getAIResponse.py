from tools import tools
from initGPT import chat

def getAIResponse(newMessage):
    
    response = chat.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "user",
                "content": newMessage,
            },
        ],
        temperature=1,
        max_tokens=256,
        tools=tools
    )
    
    reply = response.choices[0].message.content
    return reply

