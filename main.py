import random


def print_board(board):
    print("   1   2   3")
    letter = 'A'
    for i in board:
        print(f"{letter}  {i[0]} | {i[1]} | {i[2]}")
        letter = chr(ord(letter) + 1)


def print_menu():
    print("Welcome: ")
    print("P - play")
    print("M - mode")
    print("Q - quit")


def mode_select(mode):
    while True:
        print("Choose one of the modes: ")
        print("P - player vs player")
        print("A - player vs ai (default)")
        action = input()
        action.lower()
        match action:
            case 'P':
                mode = 0
                return mode
            case 'A':
                mode = 1
                return mode
            case _:
                print(f"There is no option under {action}")


def action_check(board):
    while True:
        print_board(board)
        print("Choose tile")
        action = input()
        if len(action) > 2:
            print("Wrong action, too many arguments")
            continue
        elif action[0] not in ['A', 'B', 'C']:
            print(f"There is no tile named {action[0]}")
            continue
        elif action[1] not in ['1', '2', '3']:
            print(f"There is no tile with number {action[1]}")
        else:
            break

    return action


def pc_vs_player(board):
    while True:
        action = action_check(board)



def pl_vs_pl(board):
    pass


def menu(board):
    mode = 1
    while True:
        print_menu()
        action = input()
        action = action.upper()
        match action:
            case 'P':
                if mode:
                    pc_vs_player(board)
                else:
                    pl_vs_pl(board)
            case 'M':
                mode = mode_select(mode)
            case 'Q':
                break
            case _:
                print(f"There is no option under {action}")


def main():
    board = [['.'] * 3] * 3
    menu(board)


main()
