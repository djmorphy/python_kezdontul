#list comprehension - lista megértések 2
"""
[0,0,0,0]
[0,0,0,0]
[0,0,0,0]
[0,0,0,0]

[1,0,0,0]
[0,1,0,0]
[0,0,1,0]
[0,0,0,1]
"""
#két list comph. tartalmaz egyik az x a másik az y hozza létre
matrix_zeros = [[0 for x in range(4)] for y in range(4)]

#print(matrix_zeros)

matrix_print = lambda mat: ([print(row) for row in mat], print())  #azért kell sima () -be tenni hogy a print() hozzáadjam és elválassza a matrix-ot

matrix_print(matrix_zeros)

matrix_identity = [[1 if x==y else 0 for x in range(4)] for y in range(4) ] #létrehozza a 4 oszlopt a belső for. Külső for ciklus létrehozza sorokat
matrix_print(matrix_identity)