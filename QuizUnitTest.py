import unittest
import json


class SimplisticTest(unittest.TestCase):

    def test_question_count(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            questions = []
            questioncount = 0
            data = json.load(file_in)
            question_json = data['questions']
            for question in question_json:
                questions.append(question['info'])
                questioncount = questioncount + 1
        self.assertEqual(questioncount, 20)

    def test_answer_count(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            data = json.load(file_in)
            question_json = data['questions']
            jsonanswers = []
            answercount = 0
            for question in question_json:
                jsonanswers.append(question['Answer'])
                answercount = answercount + 1
        self.assertEqual(answercount, 20)

    def test_question(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            questions = []
            questioncount = 0
            data = json.load(file_in)
            question_json = data['questions']
            for question in question_json:
                questions.append(question['info'])
                questioncount = questioncount + 1
        self.assertEqual(questions[5], "What kind of weapon is a falchion?")

    def test_json_answer(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            data = json.load(file_in)
            questions_json = data['questions']
            jsonanswers = []
            for question in questions_json:
                jsonanswers.append(question['Answer'])
        self.assertEqual(jsonanswers[3], "A farrier")

    def test_json_answer_UPPER(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            data = json.load(file_in)
            questions_json = data['questions']
            jsonanswers = []
            for question in questions_json:
                jsonanswers.append(question['Answer'])
            upperanswers = []
            for answer in jsonanswers:
                upperanswers.append(answer.upper())
        self.assertEqual(upperanswers[3], "A FARRIER")

    def test_user_answer(self):
        filename = "quiz_structure.json"
        test_user_input = "true".upper()
        with open(filename, 'r') as file_in:
            data = json.load(file_in)
            questions_json = data['questions']
            jsonanswers = []
            for question in questions_json:
                jsonanswers.append(question['Answer'])
            upperanswers = []
            for answer in jsonanswers:
                upperanswers.append(answer.upper())
        self.assertEqual(upperanswers[14], test_user_input)

    def test_correct(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            questions = []
            questioncount = 0
            data = json.load(file_in)
            questions_json = data['questions']
            for question in questions_json:
                questions.append(question['info'])
                questioncount = questioncount + 1
            jsonanswers = []
            useranswers = ['I DONT KNOW', 'LAKE SUPERIOR', 'THE MOON',
                           'I DONT KNOW', 'KILT', 'A SWORD', 'STRING', 'DICTIONARY',
                           'URANUS', 'I FORGET', 'FALSE', 'TRUE', 'FALSE', 'TRUE',
                           'TRUE', '1870', '1990', '2009', 'GRATEFUL DEAD', 'LISP']
            for question in questions_json:
                jsonanswers.append(question['Answer'])
            upperanswers = []
            for answer in jsonanswers:
                upperanswers.append(answer.upper())
        if useranswers[5] == upperanswers[5]:
            correct = "Correct"
            self.assertEqual(correct, "Correct")

    def test_incorrect(self):
        filename = "quiz_structure.json"
        with open(filename, 'r') as file_in:
            questions = []
            questioncount = 0
            data = json.load(file_in)
            questions_json = data['questions']
            for question in questions_json:
                questions.append(question['info'])
                questioncount = questioncount + 1
            jsonanswers = []
            useranswers = ['I DONT KNOW', 'LAKE SUPERIOR', 'THE MOON',
                           'I DONT KNOW', 'KILT', 'A SWORD', 'STRING', 'DICTIONARY',
                           'URANUS', 'I FORGET', 'FALSE', 'TRUE', 'FALSE', 'TRUE',
                           'TRUE', '1870', '1990', '2009', 'GRATEFUL DEAD', 'LISP']
            for question in questions_json:
                jsonanswers.append(question['Answer'])
            upperanswers = []
            for answer in jsonanswers:
                upperanswers.append(answer.upper())
        if useranswers[5] == upperanswers[5]:
            correct = "Correct"
        elif useranswers[0] != upperanswers[0]:
            incorrect = "Incorrect"
            self.assertEqual(incorrect, "incorrect")


if __name__ == '__main__':
    unittest.main()
