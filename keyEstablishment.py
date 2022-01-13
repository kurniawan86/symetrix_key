import numpy as np

class keyEstab:
    sym_matrix = None
    def __init__(self, keyspace):
        self.keyspace =keyspace

    def linkKey(self, nodeA, nodeB):
        n = nodeA.shape[0]
        res = []
        for i in range(n):
            res1 = (self.perkalian(nodeA[i], nodeB[i])) % 15
            res.append(res1)
        res = np.array(res)
        res = self.keyspace.XOR_array1D(res)
        res = self.keyspace.pencocokan(res)
        return res

    def perkalian(self,A, B):
        if A > 0 and B > 0:
            return A+B
        elif A == -1 or B == -1:
            return 0
        elif A == 0:
            return B
        elif B == 0:
            return A
