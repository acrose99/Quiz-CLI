import json


def main():
    with open("quiz_structure.json", 'r') as file_in:
        questions = []
        questioncount = 0
        data = json.load(file_in)
        specific_answer_questions = data['questions']['specificAnswerQuestions']
        # print(specific_answer_questions)
        # print(specific_answer_questions[0])
        # print(specific_answer_questions[0]['info'])
        for question in specific_answer_questions:
            questions.append(question['info'])
            questioncount = questioncount + 1
        # print(questions)
        realanswers = []
        answers = []
        for question in specific_answer_questions:
            realanswers.append(question['Answer'])
        # print(realanswers)
        for i in range(len(questions)):
            print(questions[i])
            answer = input("Answer: ")
            answers.append(answer)
        print(print('Answers:' + str(answers)))
        with open('Quiz_Specific_Questions_Answers.txt', 'w') as file_out:
            a = 0
            for i in answers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))
