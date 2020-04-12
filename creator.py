import json


def main():
    question_dict = {

    }
    question_dict_wrapper = {
        'filled': [

        ],
        'multChoice': [

        ],
        'T/F': [

        ]
    }
    question_count = int(input("How many questions do you want to create?"))
    multiplechoice_count = 0
    button = {
        "0": None,
        "1": None,
        "2": None,
        "3": None
    }
    counter = 0
    while counter < question_count:
        question_type = input("What type of question is question " + str(
            counter + 1) + '\n Type Multiple Choice, Specific Answer, or T/F.')
        if question_type.upper() == "MULTIPLE CHOICE":
            info = input("What is question " + str(counter + 1) + "?")
            multiplechoice_count += 1
            button_count = int(input("How many options are there?"))
            buttons = []
            for x in range(button_count):
                option = input("What is option " + str(x + 1) + "?")
                buttons.append(option)
            answer = input("What is the answer?")
            if answer not in buttons:
                print("Answer not in options, ERROR")
            else:
                multiplechoice_counter = 0
                while multiplechoice_counter < button_count:
                    button[str(multiplechoice_counter)] = buttons[multiplechoice_counter]
                    print(button)
                    multiplechoice_counter += 1
            question_dict = {
                'question': info,
                'button': button,
                'input': "",
                'answer': buttons.index(answer),
                'correct': None
            }
            question_dict_wrapper['multChoice'].append(question_dict)
            # multiple_choice_object_dict['question'] = answer
            # multiple_choice_object_dict['answer'] = buttons.index(answer)
            # multiple_choice_dict['multipleChoice'].append(multiple_choice_dict)

        elif question_type.upper() == 'SPECIFIC ANSWER':
            info = input("What is question " + str(counter + 1) + "?")
            answer = input("What is the answer")
            question_dict = {
                'question': info,
                'input': "",
                'answer': answer,
                "correct": None
            }
            question_dict_wrapper['filled'].append(question_dict)
        elif question_type.upper() == 'T/F':
            info = input("What is question " + str(counter + 1) + "?")
            answer = input("Is it True or False?")
            if answer.upper() == "TRUE":
                question_dict = {
                                    'question': info,
                                    'options': {
                                        '0': True,
                                        '1': False,
                                    },
                                    'input': "",
                                    'answer': True,
                                    'correct': None
                                },
            elif answer.upper() == "FALSE":
                question_dict = {
                                    'question': info,
                                    'options': {
                                        '0': True,
                                        '1': False,
                                    },
                                    'input': "",
                                    'answer': False,
                                    'correct': None
                                },
            question_dict_wrapper['T/F'].append(question_dict)
        counter = counter + 1
        # question_dict_wrapper['questions'].append(question_dict)
    file_output = input("What would you like to name your quiz?")
    with open(file_output + '.json', 'w') as file_out:
        json.dump(question_dict_wrapper, file_out, indent=4)
