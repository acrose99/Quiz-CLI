import json


def main():
    with open("quiz_structure.json", 'r') as file_in:
        questions = []
        questioncount = 0
        data = json.load(file_in)
        True_False_Questions = data['questions']['trueOrFalseQuestions']
        # print(True_False_Questions)
        # print(True_False_Questions[0])
        # print(True_False_Questions[0]['info'])
        for question in True_False_Questions:
            questions.append(question['info'])
            questioncount = questioncount + 1
        # print(questions)
        realanswers = []
        answers = []
        for question in True_False_Questions:
            realanswers.append(question['Answer'])
        # print(realanswers)
        for i in range(len(questions)):
            print(questions[i])
            answer = input("True or False: ")
            answers.append(answer)
        print(print('Answers:' + str(answers)))
        with open('True_False_Questions.txt', 'w') as file_out:
            a = 0
            for i in answers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))
