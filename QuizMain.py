import json


def main():
    question_dict = {
        "specificAnswerQuestions": {
            "question",
            "info"
            "species",
        }
    }
    with open("quiz_structure.json", 'r') as file_in:
        questions = []
        questionCount = 0
        data = json.load(file_in)
        print(data)
        print(data['specificAnswerQuestions'][0])
        print(data['specificAnswerQuestions'][0]['info'])
        for question in data['specificAnswerQuestions']:
            questions.append(question['info'])
            questionCount = questionCount + 1
        print(questions)
        realAnswers = []
        answers = []
        for question in data['specificAnswerQuestions']:
            realAnswers.append(question['Answer'])
        print(realAnswers)
        for i in range(len(questions)):
            print(questions[i])
            answer = input("Answer: ")
            answers.append(answer)
        print(answers)
        with open('Quiz Answers.txt', 'w') as file_out:
            a = 0
            for i in answers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))


main()
