import json


def answer(filename):
    with open(filename, 'r') as file_in:
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
        jsonanswers = []
        useranswers = []
        for question in specific_answer_questions:
            jsonanswers.append(question['Answer'])
        # print(jsonanswers)
        upperanswers = []
        for answer in jsonanswers:
            upperanswers.append(answer.upper())
        # print(upperanswers)
        for i in range(len(questions)):
            print(questions[i])
            answer = input("Answer: ")
            useranswers.append(answer.upper())
        with open('Quiz_Specific_Questions_Answers.txt', 'w') as file_out:
            a = 0
            for i in useranswers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))
        correct_count = 0
        for answer in range(questioncount):
            if useranswers[answer] == upperanswers[answer]:
                correct_count = correct_count + 1
        print("Your score on Specific Answers: {}/{}".format(correct_count, questioncount))


def create():
    question_count = int(input("How many questions do you want to create?"))
    questions = []
    counter = 0
    while counter < question_count:
        info = input("What is question " + str(counter + 1) + "?")
        answer = input("What is the answer")
        question_dict = {
            "question":
                {
                    "questionCount": counter + 1,
                    "info": info,
                    "Answer": answer
                }
        }
        questions.append(question_dict)
        counter = counter + 1
    with open('Quiz_Specific_Questions_Quiz.json', 'w') as file_out:
        json.dump(questions, file_out, indent=4, sort_keys=True)
