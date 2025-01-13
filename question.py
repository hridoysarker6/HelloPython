import json

with open('questions.json','r') as file:
    content = file.read()

data = json.loads(content)

for questions in data:
    print(questions['question_text'])
    for index,alternative in enumerate(questions['alternative']):
        print(f"{index+1}. {alternative}")

    user_input = int(input("put your answer:"))

    questions['user_input'] = user_input

score = 0

for questions in data:
    if questions['correct_answer'] == questions['user_input']:
        score +=1

print(f"your score is {score} out of {len(data)}")

