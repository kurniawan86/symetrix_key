from keyGeneration_file import keyGeneration
from symentric_matrix_file import symetric_matrix
if __name__ == '__main__':
    obj3 = symetric_matrix()
    symetric = obj3.matrix
    pAlpha = obj3.powerAlpha
    obj = keyGeneration(symetric,pAlpha)