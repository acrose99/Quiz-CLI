import SpecificAnswerQuiz
import multipleChoiceQuestionsOneAnswer
import trueOrFalseQuestion


def main():
    print("Which quiz do you want to answer/look at")
    quiz_type = input("Type T/F, Multiple Choice, or Specific Answers, or all:")

    if quiz_type == 'T/F':
        trueOrFalseQuestion.main()
    elif quiz_type == 'Multiple Choice':
        multipleChoiceQuestionsOneAnswer.main()
    elif quiz_type == 'Specific Answers':
        SpecificAnswerQuiz.main()
    elif quiz_type == 'all':
        SpecificAnswerQuiz.main()
        trueOrFalseQuestion.main()
        multipleChoiceQuestionsOneAnswer.main()
    else:
        print('Error')


main()
