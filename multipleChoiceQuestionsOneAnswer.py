import json


def main():
    with open("quiz_structure.json", 'r') as file_in:
        questions = []
        questioncount = 0
        data = json.load(file_in)
        multiple_choice_questions = data['questions']['multipleChoiceQuestionsOneAnswer']
        # print(multiple_choice_questions)
        # print(multiple_choice_questions[0])
        # print(multiple_choice_questions[0]['info'])
        for question in multiple_choice_questions:
            questions.append(question['info'])
            questioncount = questioncount + 1
        # print(questions)
        realanswers = []
        answers = []
        for question in multiple_choice_questions:
            realanswers.append(question['Answer'])
        # print(realanswers)
        for i in range(len(questions)):
            print(questions[i])
            print('Options: ' + str(multiple_choice_questions[i]['options']))
            answer = input("Answer: ")
            answers.append(answer)
        print('Answers:' + str(answers))
        with open('Quiz_multiple_choice_questions.txt', 'w') as file_out:
            a = 0
            for i in answers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))
