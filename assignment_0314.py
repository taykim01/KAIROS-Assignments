from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)
chat = client.chat.completions

character = (
    chat.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": "Give me a famous movie character. Just the name of the character.",
            },
        ],
        temperature=1,
        max_tokens=256,
    )
    .choices[0]
    .message.content
)
baseMessage = {
    "role": "system",
    "content": "The user will try to guess who "
    + character
    + " is by asking you random questions about "
    + character
    + ". You will only return in YES OR NO to the user's questions. If the user guessed who "
    + character
    + " is, you will say TERMINATE.",
}
initMessage = "Let's start."


def toUserObject(message):
    return {"role": "user", "content": message}


def toAssistantObject(message):
    return {"role": "assistant", "content": message}


def getSimpleResponse(newMessage):
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


chatList = [baseMessage]


def iterateMessageList(message):  # goal: get the full chat list
    # print(chatList)
    if len(chatList) % 2 == 0:  # even
        chatList.append(toAssistantObject(message))
    else:  # odd
        chatList.append(toUserObject(message))
    return chatList


def getAIResponse(newMessage=None):
    response = chat.create(
        model="gpt-4",
        messages=iterateMessageList(newMessage),
        temperature=1,
        max_tokens=256,
    )
    reply = response.choices[0].message.content
    return reply


num_inputs = int(input("Enter the number of questions: ")) + 1

for i in range(1, num_inputs + 1):
    user_input = input(f"Enter question {i}: ")
    reply = getAIResponse(user_input) # Yes / No / Terminate game.
    if len(chatList) > num_inputs:
        print(getSimpleResponse("Give me a discouraging message saying that I failed to guess the answer, which was " + character + ".")) # Fail message
        exit()
    elif "Terminate" in reply or "terminate" in reply or "TERMINATE" in reply:
        print(getSimpleResponse("Give me a congratulatory message saying that I correctly guessed the answer, which was " + character + ".")) # Congratulatory message
        exit()
    else:
        print(reply)


# initiate game by asking user to think of a character
# add the inital message to the chatList array
# get the reply from the user and prompt a new chat that replies yes or no
# add the step above to the chatList array
# get the reply from the user and prompt a new chat that replies yes or no
# add the step above to the chatList array
# repeat 5 times

# 수정할 것:
# 1. 시작할 때 assistant가 yes/no로 대답하는것 수정 -> 해결
# 2. 맞췄을 때 게임 종료할 것 -> 해결
# 3. 뜬금없이 답 알려줌 -> 해결
