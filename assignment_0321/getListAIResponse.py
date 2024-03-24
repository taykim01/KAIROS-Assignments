from initGPT import chat

def getListAIResponse(chatList, tools): # 신규 메시지를 입력하면, 전체 메시지 리스트를 반환

    response = chat.create(
        model="gpt-4",
        messages=chatList,
        temperature=1,
        max_tokens=512,
        tools=tools
    )

    return response