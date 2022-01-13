from keyGeneration_file import keyGeneration
from symentric_matrix_file import symetric_matrix
from generateMatrixG import gen_MatrixG

if __name__ == '__main__':
    obj3 = symetric_matrix()
    symetric = obj3.matrix
    vectorG1 = gen_MatrixG
    pAlpha = obj3.powerAlpha
    obj = keyGeneration(symetric,pAlpha)