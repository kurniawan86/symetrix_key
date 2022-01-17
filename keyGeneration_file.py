import numpy as np
from generateMatrixD_file import generateD
from generateMatrixG import gen_MatrixG
from grup_node_file import *
from symentric_matrix_file import symetric_matrix
from Generating_key_Space_file import KeySpace
from keyEstablishment import keyEstab

class keyGeneration:
    k = 3
    n_alpha = 14
    N = 4
    matrix_D = None
    vector_G1 = None
    symetric = None
    pAlpha = None

    def __init__(self, symetric, palpha):
        self.symetric = symetric
        self.pAlpha = palpha
        # print("power alpha ",self.pAlpha)
        self.main()

    def main(self):
        keyspace = KeySpace(self.n_alpha, self.symetric, self.pAlpha)
        ## STEP 1
        self.matrix_D = self.step1()
        print("MATRIX D \n",self.matrix_D)
        print("===============")

        ## STEP 2
        obj2 = gen_MatrixG(self.k, self.N, self.n_alpha)
        self.vector_G1 = obj2.matrixG1

        ## STEP 3
        # CREATE GR0UP
        # GROUP 1
        group1 = group(obj2,keyspace, 0)
        matrixG1 = group1.matrix_G
        print("MATRIX G1")
        print(matrixG1)
        print("+++++++++++++++++++")
        # GROUP 2
        if_a = 3
        group2 = group(obj2, keyspace, if_a)
        matrixG2 = group2.matrix_G
        print("MATRIK G2")
        print(matrixG2)
        print("===================")

        ## STEP 4
        group1.generateA(self.matrix_D)
        print("MATRIX A1")
        print(group1.matrix_A)
        print("+++++++++++")
        group2.generateA(self.matrix_D)
        print("MATRIX A2")
        print(group2.matrix_A)
        print("===========")

        ## STEP 5
        node_W = node(group1,4)
        print("NODE W")
        print("Row from A")
        print(node_W.rowFromA)
        print("seed from G")
        print(node_W.seedFromG)
        print("--------------")

        node_X = node(group1,2)
        print("NODE X")
        print("Row from A")
        print(node_X.rowFromA)
        print("seed from G")
        print(node_X.seedFromG)
        print("--------------")

        node_Y = node(group2,4)
        print("NODE Y")
        print("Row from A")
        print(node_Y.rowFromA)
        print("seed from G")
        print(node_Y.seedFromG)
        print("--------------")

        node_Z = node(group2,1)
        print("NODE Z")
        print("Row from A")
        print(node_Z.rowFromA)
        print("seed from G")
        print(node_Z.seedFromG)
        print("--------------")

        ################################
        #key Establish
        key = keyEstab(keyspace)
        res = key.linkKey(node_Y.rowFromA,node_Z.seedFromG)
        print("SATU GRUP Y - Z")
        print(res)
        res1 = key.linkKey(node_Y.seedFromG, node_Z.rowFromA)
        print("SATU GRUP Z - Y")
        print(res1)

        #key Establish beda Grup
        res2 = key.linkKey(node_Y.rowFromA, node_W.seedFromG)
        print("SATU GRUP Y - W")
        print(res2)
        res3 = key.linkKey(node_W.rowFromA, node_Y.seedFromG)
        print("SATU GRUP W - Y")
        print(res3)

    def step1(self):
        # print("MATRIK D")
        obj = generateD(self.k, self.n_alpha)
        return obj.matrix