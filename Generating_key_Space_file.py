import numpy as np

class KeySpace:
    n = 0
    sym_matrix = None
    index_aplah = None

    def __init__(self, nAlpha, symetric_matrix, index_aplha):
        self.n = nAlpha
        self.sym_matrix = symetric_matrix
        self.index_aplah = index_aplha
        # print(self.cocok(np.array([1,0,1,1]),self.sym_matrix[13]))
        # vector1 = self.convert_index2Biner(3)
        # vector2 = self.convert_index2Biner(5)
        # print(vector1)
        # print(vector2)
        # self.XOR_vector(vector1, vector2)

    def multiplyPolinom1(self,vector1, vector2):
        res = vector1 + vector2
        res1 = res % 15
        res1 = self.XOR_array1D(res1)
        res1 = self.pencocokan(res1)
        return  res1

    def multiplyPolinom(self, matrixD, matrixG):
        bar, kol = matrixD.shape
        bar2, kol2 = matrixG.shape
        baris = []
        for i in range(bar):
            kolom = []
            for j in range(kol2):
                temp = []
                for k in range(bar2):
                    temp.append(matrixG[k,j])
                    a = np.array(temp)
                res = self.multiplyPolinom1(matrixD[i], a)
                kolom.append(res)
            baris.append(kolom)
        return np.array(baris)

    def convert_index2Biner(self, index):
        n = self.index_aplah.shape[0]
        ind = None
        for i in range(n):
            if index == self.index_aplah[i]:
                ind = self.sym_matrix[i]
        return ind

    def XOR_vector(self, vector1, vector2):
        n = vector1.shape[0]
        res = []
        for i in range(n):
            res.append(self.XOR(vector1[i], vector2[i]))
        res = np.array(res)
        return res

    def XOR_array1D(self, matrix1D):
        n = matrix1D.shape[0]
        vector1 = self.convert_index2Biner(matrix1D[0])
        vector2 = self.convert_index2Biner(matrix1D[1])
        res = self.XOR_vector(vector1, vector2)
        for i in range(2, n):
            vector = self.convert_index2Biner(matrix1D[i])
            res = self.XOR_vector(res, vector)
        return res

    def XOR(self, a, b):
        res = 1
        if a == b:
            res = 0
        return res

    #kudu pakek fungsi mencocokan satu vector dengan satu dimensi matrix
    def pencocokan(self, vector):
        baris,kol = self.sym_matrix.shape
        cek = False
        res = -10
        for i in range(baris):
            cek = self.cocok(self.sym_matrix[i],vector)
            if cek == True:
                res = i
        return res-1
    def cocok(self, vector1,vector2):
        n = vector1.shape[0]
        count = 0
        cek = False
        # print(vector1)
        # print(vector2)
        for i in range(n):
            a = (int(vector1[i]))
            b = (int(vector2[i]))
            if a==b:
                count = count +1
        if count == 4:
            cek = True
        return cek
