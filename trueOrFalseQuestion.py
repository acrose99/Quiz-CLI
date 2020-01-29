import json


def answer(filename):
    with open(filename, 'r') as file_in:
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
        jsonanswers = []
        useranswers = []
        for question in True_False_Questions:
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
        with open('True_False_Questions.txt', 'w') as file_out:
            a = 0
            for i in useranswers:
                a = a + 1
                file_out.write('{}) {}\n\n'.format(a, i))
        correct_count = 0
        for answer in range(questioncount):
            if useranswers[answer] == upperanswers[answer]:
                correct_count = correct_count + 1
        print("Your score on True/False: {}/{}".format(correct_count, questioncount))


def create():
    question_count = int(input("How many questions do you want to create?"))
    questions = []
    counter = 0
    while counter < question_count:
        info = input("What is question " + str(counter + 1) + "?")
        answer = input("True or False?")
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
    with open('Quiz_True_or_False_Quiz.json', 'w') as file_out:
        json.dump(questions, file_out, indent=4, sort_keys=True)
