from keyGeneration_file import keyGeneration
from symentric_matrix_file import symetric_matrix
from generateMatrixG import gen_MatrixG

if __name__ == '__main__':
    #scenario 1 : sesuai dengan yang ada di paper
    #scenario 2 : generate yang matrik dari perhitungan manual
    obj3 = symetric_matrix("scenario 1")
    fieldElement = obj3.matrix
    pAlpha = obj3.powerAlpha
    obj = keyGeneration(fieldElement, pAlpha)