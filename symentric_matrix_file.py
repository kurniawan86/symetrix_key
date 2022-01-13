import numpy as np

class symetric_matrix:
    matrix = None
    powerAlpha = None
    n = 16

    def __init__(self):
        self.generateFourTuple()
        self.create_powerAlpha()

    def generateFourTuple(self):
        matrik = np.zeros((self.n,4))
        matrik[0] = [0, 0, 0, 0]
        matrik[1] = [1, 0, 0, 0]
        matrik[2] = [0, 1, 0, 0]
        matrik[3] = [0, 0, 1, 0]
        matrik[4] = [0, 0, 0, 1]
        matrik[5] = [1, 1, 0, 0]
        matrik[6] = [0, 1, 1, 0]
        matrik[7] = [0, 0, 1, 1]

        matrik[8] = [1, 1, 0, 1]
        matrik[9] = [1, 0, 1, 0]
        matrik[10] = [0, 1, 0, 1]
        matrik[11] = [1, 1, 1, 0]
        matrik[12] = [0, 1, 1, 1]
        matrik[13] = [1, 1, 1, 1]
        matrik[14] = [1, 0, 1, 1]
        matrik[15] = [1, 0, 0, 1]
        self.matrix = matrik

    def create_powerAlpha(self):
        power_alpha = np.zeros(self.n)
        power_alpha[0] = 0
        power_alpha[1] = 1
        for i in range(1, self.n-1):
            power_alpha[i+1] = i
        self.powerAlpha = power_alpha
