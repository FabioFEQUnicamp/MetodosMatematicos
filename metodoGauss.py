"""
Alunos: Fábio Menslin, Alcione Freitas e Hezb Ullah
RA: 289297, 289288, 290405
"""

#Define as matrizes para processar
A = [[6,0,-1,0,0],[-3,3,0,0,0],[0,-1,9,0,0],[0,-1,-8,11,-2],[-3,-1,0,0,4]]
B = [50, 0, 160, 0, 0]
#A = [[-250, 0, 40],[240, -250, 0],[0, 240, -250]]
#B = [-6500, -2500, -2500]
C = []
n = len(A)
h = 0

def Pivotacao(h):
  for i in range(h+1, n):
    fp = fatorPivot(A[h][h], A[i][h])
    for j in range(0, n):
      A[i][j] = A[i][j] - fp*A[h][j]
    B[i] = B[i] - fp*B[h]
  if (h > n):
    return A
  h+=1
  return Pivotacao(h)

def fatorPivot(m, n):
  return n/m

def matrizResultado():
  for i in range (1, n+1):
    C.append((B[n-i] - somaC(C, n-i))/A[n-i][n-i])
  C.reverse()
  return C

def somaC(C, pos, soma=0, h=0):
  tamanhoC = len(C)
  if (h < tamanhoC):
    soma = soma + C[h]*A[pos][n-1-h]
    h+=1
    return somaC(C, pos, soma, h)
  return soma

A = Pivotacao(h)
C = matrizResultado()

print("Abaixo, as matrizes resultantes do escalonamento e resultados aplicados do método de Gauss")
print("Matriz coeficientes: ")
for i in range(0,n):
  print(f"A{i+1}: {A[i]}")
print("Matriz resultados: ")
for i in range(0,n):
  print(f"B{i+1}: [{B[i]}]")
print("Matriz variáveis : ")
for i in range(0,n):
  print(f"C{i+1}: [{C[i]}]")