import SpecificAnswerQuiz
import multipleChoiceQuestionsOneAnswer
import trueOrFalseQuestion
# import CombinationQuiz
import json


def main():
    print("Would you like to create a quiz, or answer quizzes that have been made?")
    quiz_or_answer = input("Type answer or create: ")
    if quiz_or_answer == "answer" or quiz_or_answer == "Answer":
        print("Which quiz do you want to answer/look at")
        quiz_type = input("Type T/F, Multiple Choice, or Specific Answers, or all:")
        if quiz_type == 'T/F' or quiz_type == 't/f':
            trueOrFalseQuestion.answer('quiz_structure.json')
        elif quiz_type == 'Multiple Choice' or quiz_type == 'multiple choice':
            multipleChoiceQuestionsOneAnswer.answer('quiz_structure.json')
        elif quiz_type == 'Specific Answers' or quiz_type == 'specific answers':
            SpecificAnswerQuiz.answer('quiz_structure.json')
        elif quiz_type == 'all' or quiz_type == 'ALL':
            SpecificAnswerQuiz.answer('quiz_structure.json')
            trueOrFalseQuestion.answer('quiz_structure.json')
            multipleChoiceQuestionsOneAnswer.answer('quiz_structure.json')
            # WIP, change over to using CombinationQuiz.py
    elif quiz_or_answer == "create" or quiz_or_answer == "Create":
        print(
            "Which quiz type do you want to create?\n You can create a Multiple Choice quiz, a T/F quiz, a Specific Answers quiz, or a combination.")
        quiz_format = input("Type specific, multiple choice, T/F, or combination")
        if quiz_format == "specific" or quiz_format == "Specific":
            SpecificAnswerQuiz.create()
        elif quiz_format == "multiple choice" or quiz_format == "Multiple choice" or quiz_format == "Multiple Choice":
            multipleChoiceQuestionsOneAnswer.create()
        if quiz_format == "T/F" or quiz_format == "True/False" or quiz_format == "t/f":
            trueOrFalseQuestion.create()
        if quiz_format == "combination" or quiz_format == "Combination":
            # CombinationQuiz.answer()
            print("Feature currently not implemented yet. Stay tuned for future updates.")
    else:
        print("Error")

main()
