import random
import numpy as np

class gen_MatrixG:
    k = 0
    N = 0
    nAlpha = 0
    matrixG1 = None
    def __init__(self, k, N, nAplha):
        self.k = k
        self.N = N
        self.nAlpha = nAplha
        self.initMatrixZeros()
        self.statisG1()
        # self.genG1()

    def initMatrixZeros(self):
        self.matrix = np.zeros((self.k, self.N))

    def cetak(self):
        print(self.matrix)

    def genG1(self):
        for i in range(self.N):
            self.matrixG1 = random.randint(0, self.nAlpha)

    def statisG1(self):
        self.matrixG1 = np.array([5,11,6,10])

    def calculateG1(self , bil):
        matrix = np.zeros((self.k, self.N))
        if bil == 0:
            matrix[0] = self.matrixG1
        else:
            matrix[0] = self.matrixG1+bil
        for i in range(1,self.k):
            matrix[i] = matrix[i-1] * 2 % (self.nAlpha+1)
        return matrix
