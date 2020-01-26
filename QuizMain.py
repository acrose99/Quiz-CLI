
def main():
    with open("Quiz Questions.txt") as file_in:
        questions = []
        for line in file_in:
            questions.append(line)

    answers = []
    for i in range(len(questions)):
        print(questions[i])
        answer = input("Answer: ")
        answers.append(answer)

    with open('Quiz Answers.txt', 'w') as file_out:
        a = 0
        for i in answers:
            a = a + 1
            file_out.write('{}) {}\n\n'.format(a, i))



main()