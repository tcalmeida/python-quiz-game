import questions as q


def new_game():
    player_answers = []
    correct_answer = 0
    question_num = 1

    for key in q.questions:
        print('----------------------------')
        print(key)
        for i in q.answers[question_num - 1]:
            print(i)
        answer = input('Enter the correct question (A, B, C or D): ').upper()
        player_answers.append(answer)

        # check correct answer and computes a point
        correct_answer += check_answer(q.questions.get(key), answer)
        question_num += 1

    display_score(correct_answer, player_answers)


def check_answer(question, answer):
    if question == answer:
        print('Correct!')
        return 1
    else:
        print('Wrong!')
        return 0


def display_score(correct_answer, player_answers):
    print('----------------------------')
    print('Showing results')
    print('----------------------------')
    print('Correct answers:', end=' ')
    for i in q.questions:
        print(q.questions.get(i), end=' ')
    print()

    print('Player answers:', end=' ')
    for i in player_answers:
        print(i, end=' ')
    print()

    score = int((correct_answer / len(q.questions)) * 100)
    print('Your score is: {}%'.format(score))
    print('----------------------------')


