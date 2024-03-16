"""

Alunos: Fábio Menslin, Alcione Freitas e Hezb Ullah
RA: 289297, 289288, 290405
"""

#Implementação do método matricial
A = [[-250, 0, 40],[240, -250, 0],[0, 240, -250]]
B = [-6500, -2500, -2500]


tamanhoA = len(A)
C = []
I = []
L = []

def matrizIdentidade():
  for i in range(0, tamanhoA):
    for j in range(0, tamanhoA):
      if (i!=j):
        L.append(0)
      else: L.append(1)
    I.append(L.copy())
    L.clear()
  return I


def inversaDecomposicao(A,I):
  #Primeira etapa de cima para baixo
  for h in range(0, tamanhoA):
    dividirLinha = A[h][h]
    for i in range(h+1, tamanhoA):
      fatorPivot = fatorGauss(A[h][h], A[i][h])
      for j in range(0, tamanhoA):
        A[i][j] = A[i][j] - fatorPivot*A[h][j]
        I[i][j] = I[i][j] - fatorPivot*I[h][j]
        A[i-1][j] /= dividirLinha
        I[i-1][j] /= dividirLinha
  #Segunda etapa de baixo para cima
  n = tamanhoA-1
  for h in range(0, tamanhoA):
    dividirLinha = A[n-h][n-h]
    for i in range(h+1, tamanhoA):
      fatorPivot = fatorGauss(A[n-h][n-h], A[n-i][n-h])
      for j in range(0, tamanhoA):
        A[n-i][n-j] = A[n-i][n-j] - fatorPivot*A[n-h][n-j]
        I[n-i][n-j] = I[n-i][n-j] - fatorPivot*I[n-h][n-j]
        A[n-(i-1)][n-j] /= dividirLinha
        I[n-(i-1)][n-j] /= dividirLinha

  return I

def fatorGauss(m,n):
  fatorPivot = n/m
  return fatorPivot

def matrizMultiplica(I,B):
  for i in range(0,tamanhoA):
    somaIB = 0
    for j in range(0, tamanhoA):
      somaIB = somaIB + I[i][j]*B[j]
    C.append(somaIB)
  return C
I = matrizIdentidade()
I = inversaDecomposicao(A, I)
C = matrizMultiplica(I, B)
print("As temperaturas finais são: ")
for i in range(0, tamanhoA):
  print(f"T{i}: {C[i]}")