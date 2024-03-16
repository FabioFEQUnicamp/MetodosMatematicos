import scipy.optimize as op #Importa as funções de otimização do scipy

C = [200, 200] #Atribui um chute inicial para as variáveis de concentração

def funcaoUV(C): 
  return [funU(C), funV(C)]

def funU(C):
   return C[0] +0.06*C[0]*C[1] - 200
def funV(C):
  return C[1] +0.06*C[0]*C[1] - 200


C = op.fsolve(funcaoUV, C)

print(f"Ca = {C[0]}")
print(f"Cb = {C[1]}")