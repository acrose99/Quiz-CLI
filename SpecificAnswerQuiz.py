import json
import csv


def answer(filename):
    with open(filename, 'r') as file_in:
        questions = []
        correct_or_incorrect = []
        questioncount = 0
        data = json.load(file_in)
        specific_answer_questions = data['questions']['specificAnswerQuestions']
        for question in specific_answer_questions:
            questions.append(question['info'])
            questioncount = questioncount + 1
        jsonanswers = []
        useranswers = []
        for question in specific_answer_questions:
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
        print("Your score on Specific Answer questions: {}/{}".format(correct_count, questioncount))
        with open('Quiz_Specific_Questions_Quiz_User_Answers.json', 'w') as file_out:
            json.dump(answer_output, file_out, indent=4, sort_keys=True)

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
