from dominobot import *
from copy import deepcopy

HAND_COUNT = 7
NUM_PLAYERS = 4
DOMINOES = [
    (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6),
           (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
                  (2,2), (2,3), (2,4), (2,5), (2,6),
                         (3,3), (3,4), (3,5), (3,6),
                                (4,4), (4,5), (4,6),
                                       (5,5), (5,6),
                                              (6,6)
]

available = DOMINOES.copy()
board = ""

def welcome():
    with open("welcome.txt",'r') as file:
        print(file.read())

def get_board_ends(board):
    if board == "":
        return (-1,-1)
    return (int(board[1]), int(board[-2]))

def reset_dominoes():
    global board, available
    available = DOMINOES.copy()
    board = ""

def select_hand():
    global available
    hand = []
    for i in range(HAND_COUNT):
        while True:
            try:
                domino = tuple([int(x) for x in input("DOMINO {}: ".format(i+1)).split(',')])
                if domino not in available:
                    print("UNAVAILABLE DOMINO")
                    continue
                available.remove(domino)
                hand.append(domino)
            except:
                print("INVALID INPUT.")
                continue
            break
    print("HAND:", hand)
    print()
    return hand

def add_to_board(new_pieces: list) -> None:
    global board
    to_add = deepcopy(new_pieces)
    if board == "":
        first = to_add.pop(0)
        board = "(" + str(first[0]) + "," + str(first[1]) + ")"
    pot_spots = get_board_ends(board)
    for piece in to_add:
        if piece[0] in pot_spots:
            if piece[0] == pot_spots[0]:
                board = "(" + str(piece[1]) + "," + str(piece[0]) + ")" + board
            elif piece[0] == pot_spots[1]:
                board = board + "(" + str(piece[0]) + "," + str(piece[1]) + ")"
        elif piece[1] in pot_spots:
            if piece[1] == pot_spots[0]:
                board = "(" + str(piece[0]) + "," + str(piece[1]) + ")" + board
            elif piece[1] == pot_spots[1]:
                board = board + "(" + str(piece[1]) + "," + str(piece[0]) + ")"
        pot_spots = (int(board[1]), (int(board[-2])))
    return board

def move():
    global board, available
    print("--------------------------------")
    print("Enter player moves as dominoes: ")
    print("Format as (x,y) where x <= y.")
    new_pieces = []
    pot_spots = get_board_ends(board)
    for i in range(NUM_PLAYERS-1):
        while True:
            try:
                domino = tuple([int(x) for x in input("PLAYER {}: ".format(i+1)).split(',')])
                if domino not in available:
                    print("UNAVAILABLE DOMINO.")
                    print('available:')
                    print(available)
                    print("------------------")
                    continue
                elif pot_spots != (-1,-1) and (domino[0] not in pot_spots and domino[1] not in pot_spots):
                    print("INVALID PLACEMENT.")
                    continue
                if pot_spots == (-1,-1):
                    pot_spots = (domino[0], domino[1])
                elif pot_spots[0] in domino:
                    if pot_spots[0] == domino[1]:
                        pot_spots = (domino[0], pot_spots[1])
                    elif pot_spots[0] == domino[0]:
                        pot_spots = (domino[1], pot_spots[1])
                else:
                    if pot_spots[1] == domino[1]:
                        pot_spots = (domino[0], pot_spots[0])
                    elif pot_spots[1] == domino[0]:
                        pot_spots = (domino[1], pot_spots[0])
                available.remove(domino)
                new_pieces.append(domino)
            except:
                print("INVALID INPUT.")
                continue
            break
    add_to_board(new_pieces)
    return new_pieces, board

def main():
    bot = dominobot()
    welcome()
    bot.set_hand(select_hand())
    if (6,6) in bot.get_hand():
        # TODO replace manual move with automatic 6 placement
        play = bot.manual_move(board, hasDoubleSix=True)
        add_to_board(play)
    else:
        print("Order goes:")
        print("\t2")
        print("1\t\t3")
        print("\tYou")

    while True:
        new_pieces, new_board = move()
        print("Pieces played:")
        print("\tPlayer 1: " + str(new_pieces[0]))
        print("\tPlayer 2: " + str(new_pieces[1]))
        print("\tPlayer 3: " + str(new_pieces[2]))
        print("Board:")
        print("\t" + board)
        bot.manual_move(new_board)

if __name__ == '__main__':
    main()
