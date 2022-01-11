import random
import numpy as np

class generateD:
    matrix = None
    k = 0
    n_alpha = 0
    nAlpha = 0
    def __init__(self, k, n_powerAlpha):
        self.k = k
        self.n_alpha = n_powerAlpha
        self.initMatrixZero()
        self.generate()
        self.statisMatrix()
        self.cetak()

    def initMatrixZero(self):
        self.matrix = np.zeros((self.k, self.k))

    def cetak(self):
        print(self.matrix)

    def generate(self):
        for i in range(self.k):
            for j in range(self.k):
                self.matrix[i,j] = random.randint(0,self.n_alpha)

        #ajustment matrix symetrix
        self.matrix[0,1] = self.matrix[1,0]
        self.matrix[0,2] = self.matrix[2,0]
        self.matrix[1,2] = self.matrix[2,1]

    def statisMatrix(self):
        self.matrix[0, 0] = 3
        self.matrix[0, 1] = 9
        self.matrix[0, 2] = 2

        self.matrix[1, 0] = 9
        self.matrix[1, 1] = 13
        self.matrix[1, 2] = 6

        self.matrix[2, 0] = 2
        self.matrix[2, 1] = 6
        self.matrix[2, 2] = 11
