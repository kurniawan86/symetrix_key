from generateMatrixD_file import generateD
from generateMatrixG import gen_MatrixG
if __name__ == '__main__':
    print("hello")
    k = 3
    n_alpha = 14
    N = 4
    obj = generateD(k, n_alpha)
    matrix = obj.matrix
    print("===============")
    obj2 = gen_MatrixG(k, N, n_alpha)