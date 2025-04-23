import numpy as np

# u = np.array([5, 7, 9])
# print(u)

# # LISTA -> ACEITA DIFERENÇA DE TIPOS DE VARIÁVEIS (FLOAT/STRING/INT)
# # ARRAY -> SÓ ACEITA UM TIPO (SÓ INT OU SÓ FLOAT OU SÓ STRING)

# v = np.array([4, 5, 6])
# w = np.array([7, 8, 9])

# uv = u + v
# print(uv)

# uvw = uv + w
# print(uvw)

# vwu = v + w + u
# print(vwu)

###

# u = np.array([2, 3, 4])
# _3u = 3*u
# print(_3u)

###

# u = np.array([1, 2, 3])
# v = np.array([4, 5, 6])

# m = 10
# n = 20
# mn = m * n

# mnu = mn * u
# print(mnu)

# nu = n * u

# mnu = m * nu
# print(mnu)

# uv = u + v
# muv = m * uv
# print(muv)

# mu = m * u
# mv = m * v
# mumv = mu + mv
# print(mumv)

###

# a = np.array([1, 2, 3])
# b = np.array([2, 3, 4])
# c = np.array([-1, 20, 4])
# d = 3

# ab = a + b
# print(ab)

# abc = a + b + c
# print(abc)

# _3a = d * a
# print(_3a)

# ab = a * b
# print(ab)

###

# MATRIZ = ENTIDADE ORGANIZADA EM TABELA
# I = LINHA
# J = COLUNA

# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8, 9], [10, 11, 12]])
# ab = a + b
# print(ab)

# _2a = 2 * a
# print(_2a)

###

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# ab = a + b
# print(ab)

# c = np.array([[-1, 0], [2, 3]])
# d = np.array([[4, -2], [1, 5]])
# cd = c + d
# print(cd)

# e = np.array([[1, 2, 3], [4, 5, 6]])
# f = np.array([[7, 8, 9], [10, 11, 12]])
# ef = e + f
# print(ef)

# _3a = 3 * a
# print(_3a)

# _2c = -2 * c
# print(_2c)

###

# a = np.array([[1, 2, 3], [4, 5, 6]])
# at = a.T
# print(a)
# print(at)

###

# MATRIZ IDENTIDADE -> MATRIZ NA QUAL TODOS OS ELEMENTOS DA DIAGONAL SÃO 1 E É UMA MATRIZ QUADRADA
# MATRIZ IDENTIDADE É UM ELEMENTO NEUTRO DA MULTIPLICAÇÃO DE MATRIZES
# INVERSO MULTIPLICATIVO -> A * A^-1 = 1

# a = np.array([[1, -1], [2, 1]])
# aI = np.linalg.inv(a)
# print(aI)

###

# MATRIZ AUMENTADA -> MATRIZ QUE REPRESENTA UM SISTEMA DE EQUAÇÕES LINEARES

# a = np.array([[2, 3, -1], [1, -2, 4], [3, 1, 2]])
# b = np.array([3, -5, 7])

# aI = np.linalg.inv(a)

# x = np.dot(aI, b)
# print(x)

# a = np.array([[1, 1, 1], [2, -1, 3], [-3, 4, -1]])
# b = np.array([6, 14, -2])

# aI = np.linalg.inv(a)

# x = np.dot(aI, b)
# print(x)
