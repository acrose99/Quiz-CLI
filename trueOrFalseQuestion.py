import json


def answer(filename):
    with open(filename, 'r') as file_in:
        questions = []
        questioncount = 0
        data = json.load(file_in)
        True_False_Questions = data['questions']['trueOrFalseQuestions']
        for question in True_False_Questions:
            questions.append(question['info'])
            questioncount = questioncount + 1
        jsonanswers = []
        useranswers = []
        for question in True_False_Questions:
            jsonanswers.append(question['Answer'])
        upperanswers = []
        for answer in jsonanswers:
            upperanswers.append(answer.upper())
        for i in range(len(questions)):
            print(questions[i])
            answer = input("Answer: ")
            useranswers.append(answer.upper())
        correct_count = 0
        tot_answer_count = 0
        answer_output = []
        while tot_answer_count < questioncount:
            if useranswers[tot_answer_count] == upperanswers[tot_answer_count]:
                correct_count = correct_count + 1
            user_answer_dict = {
                "User Answers": {
                    "Answer": useranswers[tot_answer_count]
                }
            }
            answer_output.append(user_answer_dict)
            tot_answer_count = tot_answer_count + 1
        print("Your score on True/False: {}/{}".format(correct_count, questioncount))
        with open('Quiz_True_or_False_Quiz_User_Answers.json', 'w') as file_out:
            json.dump(answer_output, file_out, indent=4, sort_keys=True)


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
