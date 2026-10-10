def welcome():
    while True:
        print('''\n\tWelcome to Tic-Tac-Toe!!\n
                1. Play Game\n
                2. Quit\n''')
        try:
            ch = int(input())
        except ValueError:
            print("\nInvalid Input\n")
            continue
        match ch:
            case 1: 
                game()
            case 2:
                print("\nBye Bye!!\n")
                break
            case _:
                print("\nInvalid Input\n")

def display(board):
    for i in range(len(board)):
        print('\n' + '|'.join(board[i]))
        if i < 2:
            print('\n' + '-'*5 + '\n')

def ref_board():
    ref = []
    k = 1
    for i in range(3):
        ref.append([])
        for j in range(3):
            ref[i] += [str(k)]
            k += 1
    print("\nThis is the reference for the positions:\n")
    display(ref)
    print("\nNow, the game starts!!\n\n")

def check(layout):
    n = len(layout)
    # check rows and columns
    for i in range(n):
        if all(layout[i][j] == 'X' for j in range(n)) or all(layout[j][i] == 'X' for j in range(n)):
            print("\nCongrats Player 1 for winning the game!!\n")
            return 1
        if all(layout[i][j] == 'O' for j in range(n)) or all(layout[j][i] == 'O' for j in range(n)):
            print("\nCongrats Player 2 for winning the game!!\n")
            return 1
    # check diagonals
    if all(layout[i][i] == 'X' for i in range(n)) or all(layout[i][n-1-i] == 'X' for i in range(n)):
        print("\nCongrats Player 1 for winning the game!!\n")
        return 1
    if all(layout[i][i] == 'O' for i in range(n)) or all(layout[i][n-1-i] == 'O' for i in range(n)):
        print("\nCongrats Player 2 for winning the game!!\n")
        return 1
    return 0

def play(pl, z, layout, post):
    while True:
        try:
            pno = int(input(f"\nEnter the position of {z}: \n"))
        except ValueError:
            print("\nEnter a valid input!!\n")
            continue
        if pno in pl:
            print("\nPosition already occupied!! Try some other position\n")
        elif pno in post:
            i, j = post[pno]
            layout[i][j] = z
            pl.append(pno)
            display(layout)
            return pl  # return updated move list
        else:
            print("\nEnter a valid position!!\n")

def game():
    ref_board()
    layout = [[' ' for _ in range(3)] for _ in range(3)]
    pl = []
    post = {k: (i, j) for k, (i, j) in enumerate([(i, j) for i in range(3) for j in range(3)], start=1)}
    display(layout)

    symbols = ['X', 'O']
    turn = 0

    while True:
        if check(layout) == 1:
            break
        if len(pl) == 9:
            print("\nThe Game is drawn!!\n")
            break

        z = symbols[turn % 2]  # alternate between X and O
        pl = play(pl, z, layout, post)
        turn += 1

welcome()
