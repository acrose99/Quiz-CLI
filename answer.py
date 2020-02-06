import json


def main(filename):
    with open(filename, 'r') as file_in:
        questions = []
        correct_or_incorrect = []
        questioncount = 0
        data = json.load(file_in)
        questions_json = data['questions']
        for question in questions_json:
            questions.append(question['info'])
            questioncount = questioncount + 1
        jsonanswers = []
        useranswers = []
        for question in questions_json:
            jsonanswers.append(question['Answer'])
        upperanswers = []
        for answer in jsonanswers:
            upperanswers.append(answer.upper())
        for i in range(len(questions)):
            print(questions[i])
            if 'options' in questions_json[i]:
                print('Options: ' + str(questions_json[i]['options']))
            elif questions_json[i]['Answer'] == "True" or questions_json[i]['Answer'] == "False":
                print("True or False?")
            answer = input("Answer: ")
            useranswers.append(answer.upper())
        correct_count = 0
        tot_answer_count = 0
        answer_output = []
        while tot_answer_count < questioncount:
            if useranswers[tot_answer_count] == upperanswers[tot_answer_count]:
                correct_count = correct_count + 1
                correct_or_incorrect.append("Correct")
            else:
                correct_or_incorrect.append("Incorrect")
            user_answer_dict = {
                "User Answer: " + str(tot_answer_count + 1): {
                    "Question": questions[tot_answer_count],
                    "Answer": useranswers[tot_answer_count],
                    "Correct_or_not:": correct_or_incorrect[tot_answer_count]
                }
            }
            answer_output.append(user_answer_dict)
            tot_answer_count = tot_answer_count + 1
        print("Your score on Multiple Choice questions: {}/{}".format(correct_count, questioncount))
        with open('Quiz_Multiple_Choice_Questions_Quiz_User_Answers.json', 'w') as file_out:
            json.dump(answer_output, file_out, indent=4, sort_keys=True)


def create():
    question_dict_wrapper = {
        'questions': [

        ]
    }
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

            "question": counter + 1,
            "info": info,
            "options": options,
            "Answer": answer
        }
        counter = counter + 1
        question_dict_wrapper['questions'].append(question_dict)
        questions.append(question_dict_wrapper)
    file_output = input("What would you like to name your quiz?")
    with open(file_output + '.json', 'w') as file_out:
        json.dump(question_dict_wrapper, file_out, indent=4, sort_keys=True)
