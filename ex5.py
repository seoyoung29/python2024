import datetime
import re
import random

def chatbot(input_text):
    if re.search(r'\b조심해\b', input_text):
        return "조심하세요!"
    elif re.search(r'\b오늘\s+날짜\b', input_text):
        today = datetime.datetime.now().strftime("%m월 %d일")
        return f"오늘은 {today} 입니다."
    elif re.search(r'\b힘내\b', input_text):
        responses = ["힘내세요!", "조금만 힘내보세요!", "잘 될 거에요!"]
        return random.choice(responses)
    else:
        return "죄송합니다. 이해할 수 없는 메시지입니다."

while True:
    user_input = input("사용자: ")
    response = chatbot(user_input)
    print("챗봇:", response)