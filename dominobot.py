from support_fns import *

class dominobot():
    def __init__(self):
        self.dominoes_left = DOMINOES.copy()
        self.hand = []
    def reset_dominoes(self):
        self.dominoes_left = DOMINOES.copy()
        self.hand = []
    def set_hand(self, hand):
        self.hand = hand
        for domino in hand:
            self.dominoes_left.remove(domino)
        print("dominobot hand set to: ", self.hand)
    def read(board):
        pass
    def manual_move(self, board, hasDoubleSix = False):
        """
        void operation for debugging
        manual selection of domino to place
        """
        if hasDoubleSix:
            print("***Bot has Double-Six.")
        print("Current Hand: ")
        print(self.hand)
        print("Select domino to play: ")
        print("Format as x,y where x <= y.")
        while True:
            try:
                domino = tuple([int(x) for x in input("Domino: ").split(',')])
                if domino in self.hand:
                    self.hand.remove(domino)
                    return [domino]
                else:
                    print("DOMINO NOT HELD.")
                    continue
            except:
                print("INVALID SELECTION.")
                continue
            break
    def get_hand(self):
        return self.hand
