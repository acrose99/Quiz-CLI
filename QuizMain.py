import answer
import creator


# import CombinationQuiz


def main():
    print("Would you like to create a quiz, or answer quizzes that have been made?")
    quiz_or_answer = input("Type answer or create: ")
    default_file = 'quiz_structure.json'
    if quiz_or_answer == "answer" or quiz_or_answer == "Answer":
        filename = input(
            "Which quiz do you want to answer?\nType the full filename\nType DEFAULT for the hardcoded example ")
        if filename == "default" or filename == "DEFAULT":
            answer.main(default_file)
        else:
            try:
                answer.main(filename)
            except AttributeError:
                print("No file given, try again!")
    elif quiz_or_answer == "create" or quiz_or_answer == "Create":
        print(
            "Which quiz type do you want to create?\n You can create a Multiple Choice quiz, a T/F quiz, a Specific Answers quiz, or a combination.")
        quiz_format = input("Type Specific Answers, Multiple Choice, T/F, or combination: ")
        if quiz_format == "multiple choice" or quiz_format == "Multiple choice" or quiz_format == "Multiple Choice":
            creator.main('Multiple Choice')
        elif quiz_format == "Specific Answers" or quiz_format == "specific answers":
            creator.main('Specific Answer')
        elif quiz_format == "T/F" or quiz_format == "True/False" or quiz_format == "t/f":
            creator.main('T/F')
        elif quiz_format == "combination" or quiz_format == "Combination":
            creator.main('Combination')
    else:
        print("Error")
main()
