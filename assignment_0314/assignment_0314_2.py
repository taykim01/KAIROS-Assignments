from assignment_0321.getAIResponse import getAIResponse
from assignment_0321.getListAIResponse import getListAIResponse

# 도메인 개발 타임라인 가이드 봇

chatList = [
    {
        "role": "system",
        "content": "You are a project manager of a team that is building a web application project that will be used by a small group of people. Your goal is to create a project management timeline. This team is consisted of one project manager(you), one design lead, and one development lead. We will be using a product design patter called 'Domain-Driven Design,'abbreviated DDD, to build the project. There are 8 tasks in DDD: 1. Key Visual(done by Design Lead), 2. Drawing a wireframe(done by PM), 3. Domain development(done by development lead), 4. UX/UI design(done by design lead), 5. UX/UI development(done by development lead), 6. Integration(done by development lead), 7. Production(done by development lead), and 8. QA(done by PM). The user will give you the expected duration of this project, and you will give the user the detailed timeline of the project in accordance with the expected duration.",
    },
]

duration_input = input("Enter the expected duration of the project: ")
duration = getAIResponse("Turn " + duration_input + " into days. Cut off all other words and return the duration in days.")

duration_message = {
        "role": "user",
        "content": "I expect the project to be completed in " + duration + " days.",
    }

chatList.append(duration_message)


response = getListAIResponse(chatList)[0].message.content
print(response)