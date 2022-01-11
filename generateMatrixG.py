import random
import numpy as np

class gen_MatrixG:
    k = 0
    N = 0
    nAlpha = 0
    matrix = None
    def __init__(self, k, N, nAplha):
        self.k = k
        self.N = N
        self.nAlpha = nAplha
        self.initMatrixZeros()
        self.genG1()
        self.statisG1()
        self.cetak()
        self.calculateG1()

    def initMatrixZeros(self):
        self.matrix = np.zeros((self.k, self.N))

    def cetak(self):
        print(self.matrix)

    def genG1(self):
        for i in range(self.N):
            self.matrix[0, i] = random.randint(0, self.nAlpha)

    def statisG1(self):
        self.matrix[0] = np.array([5,11,6,10])

    def calculateG1(self):
        print("G2 \n",self.matrix[0] * 2 % (self.nAlpha+1))