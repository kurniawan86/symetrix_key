import numpy as np

from generateMatrixD_file import generateD
from generateMatrixG import gen_MatrixG
from symentric_matrix_file import symetric_matrix
from Generating_key_Space_file import KeySpace
if __name__ == '__main__':
    print("MATRIK D")
    k = 3
    n_alpha = 14
    N = 4
    obj = generateD(k, n_alpha)
    matrix = obj.matrix
    print("===============")
    print("MATRIK G1")
    obj2 = gen_MatrixG(k, N, n_alpha)
    G1 = obj2.calculateG1(0)
    print(G1)
    print("+++++++++++++")
    print("MATRIK G2")
    G2 = obj2.calculateG1(3)
    print(G2)
    print("===================")
    obj3 = symetric_matrix()
    symetric = obj3.matrix
    print("symentric")
    print(symetric)
    print("================")
    obj4 = KeySpace(n_alpha)
    obj4.multiplyPolinom(matrix, G1)