import numpy as np

class node:
    rowFromA = None
    seedFromG = None
    group = None
    index = 0

    def __init__(self, group, if_a):
        self.group = group
        self.index = if_a
        self.setRowFromA()
        self.setSeedG()

    def setRowFromA(self):
        self.rowFromA = self.group.getRowA(self.index)

    def setSeedG(self):
        self.seedFromG = self.group.getSeedG(self.index)

class group:
    matrix_G = None
    matrix_A = None
    obj_matrixG = None
    keyspace = None
    bil = 0

    def __init__(self, obj_matrixG, keyspace, bil):
        self.keyspace = keyspace
        self.obj_matrixG = obj_matrixG
        self.bil = bil
        self.generateG1()

    def generateG1(self):
        k = self.obj_matrixG.k
        N = self.obj_matrixG.N
        nAlpha = self.obj_matrixG.nAlpha
        matrixG1 = self.obj_matrixG.matrixG1
        matrix = np.zeros((k, N))
        if self.bil == 0:
            matrix[0] = matrixG1
        else:
            matrix[0] = matrixG1 + self.bil
        for i in range(1, k):
            matrix[i] = matrix[i - 1] * 2 % (nAlpha + 1)
        self.matrix_G = matrix

    def generateA(self, matrixD):
        res = self.keyspace.multiplyPolinom(matrixD,self.matrix_G)
        self.matrix_A = np.transpose(res)

    def getRowA(self, index):
        return self.matrix_A[index-1]

    def getSeedG(self, index):
        return self.matrix_G[:,index-1]