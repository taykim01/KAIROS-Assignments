import json
from sympy import symbols, simplify, sqrt
from sympy.abc import x, y
from sympy import init_printing
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)
chat = client.chat.completions


def getListAIResponse(
    chatList, tools
):  # 신규 메시지를 입력하면, 전체 메시지 리스트를 반환

    response = chat.create(
        model="gpt-4", messages=chatList, temperature=1, max_tokens=512, tools=tools
    )

    return response


math_tools = [
    {
        "type": "function",
        "function": {
            "name": "math_function",
            "description": "간단한 수학 문제를 풀어줘.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "수식을 입력해주세요.",
                    },
                },
                "required": ["expression"],
            },
        },
    }
]

messages = [
    {
        "role": "system",
        "content": "함수에 연결할 값을 가정하지 마세요.\
      사용자의 요청이 모호한 경우 추가 설명을 요청하세요\
      한국어로 친절하게 이모지를 섞어서 답변해줘",
    },
    {
        "role": "user",
        "content": "수식 (4 / 2 ** sqrt(2)) ** (2 + sqrt(2))을 간단하게 계산해줘.",
    },
]


def math_function(expression):
    init_printing(use_unicode=True)
    simplified_expression = simplify(expression)
    result = f"{expression}: {simplified_expression}"
    return result


expr = math_function((4 / 2 ** sqrt(2)) ** (2 + sqrt(2)))

response = getListAIResponse(messages, math_tools)
print(response.choices[0].message.tool_calls)
fn = response.choices[0].message.tool_calls[0].function.name
arg = json.loads(response.choices[0].message.tool_calls[0].function.arguments)

fn_response = eval(f"{fn}(**arg)")

new_messages = [
    {
        "role": "user",
        "content": "수식 " + expr + "을 간단하게 계산해줘.",
    },
    {
        "role": "function",
        "name": fn,
        "content": fn_response,
    },
]

finalAnswer = getListAIResponse(new_messages, math_tools).choices[0].message.content
print(finalAnswer)
