import numpy as np

class KeySpace:
    n = 0

    def __init__(self, nAlpha):
        self.n = nAlpha

    def multiplyPolinom1(self,vector1, vector2):
        print("vector 1 :",vector1)
        print("Vector 2:",vector2)
        res = vector1 + vector2
        print ("vector 1 + vector 2 :",res)
        res1 = res % 15
        print("mod :",res1)

    def multiplyPolinom(self, matrixD, matrixG):
        bar, kol = matrixD.shape
        bar2, kol2 = matrixG.shape
        for i in range(bar):
            for j in range (kol2):
                temp = []
                for k in range(bar2):
                    temp.append(matrixG[k,j])
                    a = np.array(temp)
                self.multiplyPolinom1(matrixD[i],a)