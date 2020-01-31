import json


def answer(filename):
    with open(filename, 'r') as file_in:
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
        for answer in range(questioncount):
            if useranswers[answer] == upperanswers[answer]:
                correct_count = correct_count + 1
        print("Your score on Multiple Choice: {}/{}".format(correct_count, questioncount))
        with open('Quiz_multiple_choice_questions_quiz_User_Answers.json', 'w') as file_out:
            json.dump(answer_output, file_out, indent=4, sort_keys=True)



def create():
    question_count = int(input("How many questions do you want to create?"))
    questions = []
    counter = 0
    while counter < question_count:
        info = input("What is question " + str(counter + 1) + "?")
        number_of_options = int(input("How many options are there?"))
        options = []
        for x in range(number_of_options):
            option = input("What is option " + str(x + 1) + "?")
            options.append(option)
        answer = input("What is the answer")
        if answer not in options:
            print("Answer not in options, ERROR")

        question_dict = {
            "question":
                {
                    "questionCount": counter + 1,
                    "info": info,
                    "options": options,
                    "Answer": answer
                }
        }
        questions.append(question_dict)
        counter = counter + 1
    with open('Quiz_multiple_choice_questions_quiz.json', 'w') as file_out:
        json.dump(questions, file_out, indent=4, sort_keys=True)
