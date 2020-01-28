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
        jsonanswers = []
        useranswers = []
        for question in multiple_choice_questions:
            jsonanswers.append(question['Answer'])
        # print(jsonanswers)
        upperanswers = []
        for answer in jsonanswers:
            upperanswers.append(answer.upper())
        # print(upperanswers)
        for i in range(len(questions)):
            print(questions[i])
            print('Options: ' + str(multiple_choice_questions[i]['options']))
            answer = input("Answer: ")
            useranswers.append(answer.upper())
        with open('Quiz_multiple_choice_questions.txt', 'w') as file_out:
            a = 0
            for i in useranswers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))
        correct_count = 0
        for answer in range(questioncount):
            if useranswers[answer] == upperanswers[answer]:
                correct_count = correct_count + 1
        print("Your score on Multiple Choice: {}/{}".format(correct_count, questioncount))
