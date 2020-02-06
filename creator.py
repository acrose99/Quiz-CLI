import json


def main(quiz_type):
    global options
    question_dict = {

    }
    question_dict_wrapper = {
        'questions': [

        ]
    }
    question_count = int(input("How many questions do you want to create?"))
    questions = []
    counter = 0
    while counter < question_count:
        question_type = input("What type of question is question " + str(
            counter + 1) + '\n Type Multiple Choice, Specific Answer, or T/F.')
        info = input("What is question " + str(counter + 1) + "?")
        if quiz_type == 'Combination':
            if question_type == "Multiple Choice":
                number_of_options = int(input("How many options are there?"))
                options = []
                for x in range(number_of_options):
                    option = input("What is option " + str(x + 1) + "?")
                    options.append(option)
                answer = input("What is the answer?")
                if answer not in options:
                    print("Answer not in options, ERROR")
                question_dict = {

                    "question": counter + 1,
                    "info": info,
                    "options": options,
                    "Answer": answer
                }
            else:
                answer = input("What is the answer?")
                question_dict = {
                    "questionCount": counter + 1,
                    "info": info,
                    "Answer": answer
                }
        elif quiz_type == 'Multiple Choice':
            number_of_options = int(input("How many options are there?"))
            options = []
            for x in range(number_of_options):
                option = input("What is option " + str(x + 1) + "?")
                options.append(option)
            answer = input("What is the answer")
            if answer not in options:
                print("Answer not in options, ERROR")
            if quiz_type == 'Multiple Choice':
                question_dict = {

                    "question": counter + 1,
                    "info": info,
                    "options": options,
                    "Answer": answer
                }
            else:
                question_dict = {
                    "questionCount": counter + 1,
                    "info": info,
                    "Answer": answer
                }
        counter = counter + 1
        question_dict_wrapper['questions'].append(question_dict)
        questions.append(question_dict_wrapper)
    file_output = input("What would you like to name your quiz?")
    with open(file_output + '.json', 'w') as file_out:
        json.dump(question_dict_wrapper, file_out, indent=4, sort_keys=True)
