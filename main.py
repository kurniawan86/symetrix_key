from keyGeneration_file import keyGeneration
from symentric_matrix_file import symetric_matrix
from generateMatrixG import gen_MatrixG

if __name__ == '__main__':
    obj3 = symetric_matrix()
    fieldElement = obj3.matrix
    # print("SYMETRIX METRIX", fieldElement)

    pAlpha = obj3.powerAlpha
    # print("VECTOR G", pAlpha)
    obj = keyGeneration(fieldElement, pAlpha)