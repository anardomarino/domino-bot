from dominobot import *

HAND_COUNT = 7
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

def welcome():
    with open("welcome.txt",'r') as file:
        print(file.read())

def reset_available():
    global available
    available = DOMINOES.copy()

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

def main():
    bot = dominobot()
    welcome()
    hand = select_hand()


if __name__ == '__main__':
    main()
