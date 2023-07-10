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
