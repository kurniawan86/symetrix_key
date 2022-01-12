import numpy as np

from generateMatrixD_file import generateD
from generateMatrixG import gen_MatrixG
from symentric_matrix_file import symetric_matrix
from Generating_key_Space_file import KeySpace

class keyGeneration:
    k = 3
    n_alpha = 14
    N = 4
    matrix_D = None
    matrix_G1 = None
    matrix_G2 = None
    matrix_A1 = None
    matrix_A2 = None
    symetric = None
    pAlpha = None

    def __init__(self, symetric, palpha):
        self.symetric = symetric
        self.pAlpha = palpha
        self.main()

    def main(self):
        # STEP 1
        self.matrix_D = self.step1()
        print("MATRIX D \n",self.matrix_D)
        print("===============")

        # STEP 2
        obj2 = gen_MatrixG(self.k, self.N, self.n_alpha)
        self.matrix_G1 = obj2.calculateG1(0)
        print("MATRIX G1")
        print(self.matrix_G1)
        print("+++++++++++++")
        print("MATRIK G2")
        if_a = 3
        self.matrix_G2 = obj2.calculateG1(if_a)
        print(self.matrix_G2)
        print("===================")

        # STEP 4
        obj4 = KeySpace(self.n_alpha, self.symetric, self.pAlpha)
        self.matrix_A1 = np.transpose(obj4.multiplyPolinom(self.matrix_D, self.matrix_G1))
        self.matrix_A2 = np.transpose(obj4.multiplyPolinom(self.matrix_D, self.matrix_G2))
        print("MATRIX A1")
        print(self.matrix_A1)
        print("++++++++++++++++")
        print("MATRIX A2")
        print(self.matrix_A2)
        print("================")

    def step1(self):
        # print("MATRIK D")
        obj = generateD(self.k, self.n_alpha)
        return obj.matrix