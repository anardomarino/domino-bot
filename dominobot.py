DOMINOES = [
    (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6),
           (1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
                  (2,2), (2,3), (2,4), (2,5), (2,6),
                         (3,3), (3,4), (3,5), (3,6),
                                (4,4), (4,5), (4,6),
                                       (5,5), (5,6),
                                              (6,6)
]

class dominobot():
    def __init__(self):
        self.dominoes_left = DOMINOES.copy()
        self.hand = []
    def reset_dominoes(self):
        self.dominoes_left = DOMINOES.copy()
        self.hand = []
    def set_hand(self, hand):
        self.hand = hand
        print("dominobot hand set to: ", self.hand)
    def read(board):
        pass
