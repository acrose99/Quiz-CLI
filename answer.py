import unittest
import json

def main(filename):
    question_dict = {}
    question_dict_wrapper = {
        'filled': [

        ],
        'multChoice': [

        ],
        'T/F': [

        ]
    }
    with open(filename, 'r') as file_in:
        question_count = 0
        data = json.load(file_in)
        filled_questions_json = data['filled']
        filled_questions = []
        filled_answers = []
        for question in filled_questions_json:
            filled_questions.append(question['question'])
            filled_answers.append(question['answer'])
            question_count = question_count + 1
        mult_questions_json = data['multChoice']
        mult_questions = []
        mult_answers = []
        for question in mult_questions_json:
            mult_questions.append(question['question'])
            mult_answers.append(question['answer'])
            question_count = question_count + 1
        tf_questions_json = data['T/F']
        tf_questions = []
        tf_answers = []
        for question in tf_questions_json:
            tf_questions.append(question['question'])
            tf_answers.append(question['answer'])
            question_count = question_count + 1
        for i in range(len(filled_questions)):
            print(filled_questions[i])
            user_answer = input("Answer: ")
            question_dict = {
                'question': filled_questions[i],
                'input': user_answer,
                'answer': filled_answers[i],
                "correct": None
            }
            question_dict_wrapper['filled'].append(question_dict)
        for i in range(len(mult_questions)):
            if 'button' in mult_questions_json[i]:
                print(mult_questions[i])
                print('Options: ' + str(mult_questions_json[i]['button']))
                user_answer = input("Answer: ")
                question_dict = {
                    'question': mult_questions[i],
                    'button': mult_questions_json[i]['button'],
                    'input': user_answer,
                    'answer': mult_answers[i],
                    'correct': None
                }
                question_dict_wrapper['multChoice'].append(question_dict)
        for i in range(len(tf_questions)):
            if 'options' in tf_questions_json[i]:
                print(tf_questions[i])
                print("True or False?")
                user_answer = input("Answer: ")
                question_dict = {
                                    'question': tf_questions[i],
                                    'options': {
                                        '0': True,
                                        '1': False,
                                    },
                                    'input': user_answer,
                                    'answer': tf_answers[i],
                                    'correct': None
                                },
                question_dict_wrapper['T/F'].append(question_dict)
        with open('test.json', 'w') as file_out:
            json.dump(question_dict_wrapper, file_out, indent=4)
