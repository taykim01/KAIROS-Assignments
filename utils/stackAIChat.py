from initGPT import chat
from utils.toChatObject import toChatObject

chatList = []
def continuousChat(message): # 신규 메시지를 입력하면, 전체 메시지 리스트를 반환

    lastItem = chatList[-1]

    if len(chatList) == 0: # system 메시지로 시작
        chatList.append(toChatObject(message, "system"))
    if lastItem.role == "user":
        chatList.append(toChatObject(message, "assistant"))
    else:
        chatList.append(toChatObject(message, "user"))

    response = chat.create(
        model="gpt-4",
        messages=continuousChat(chatList),
        temperature=1,
        max_tokens=256,
    )
    reply = response.choices[0].message.content
    return reply