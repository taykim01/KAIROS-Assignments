from initGPT import chat
from toChatObject import toChatObject

def stackAIChat(initial_messages, message, tools): # 신규 메시지를 입력하면, 전체 메시지 리스트를 반환

    lastItem = initial_messages[-1]

    if len(chatList) == 0: # system 메시지로 시작
        chatList.append(toChatObject(message, "system"))
    if lastItem.role == "user":
        chatList.append(toChatObject(message, "assistant"))
    else:
        chatList.append(toChatObject(message, "user"))

    response = chat.create(
        model="gpt-4",
        messages=chatList,
        temperature=1,
        max_tokens=256,
        tools=tools
    )

    return response.choices