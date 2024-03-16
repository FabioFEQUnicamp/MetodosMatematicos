"""
Alunos: Fábio Menslin, Alcione Freitas e Hezb Ullah
RA: 289297, 289288, 290405
"""

import math as m

V = 30.0
R = 3.0
h0 = float(input("Insira o primeiro ponto para altura: "))
h1 = float(input("Insira o segundo ponto para altura: "))

def volumeTanque(h):
  return V - m.pi*h*h*(3*R - h)/3

def metodoSecante(h0, h1):
  hn = h1 - volumeTanque(h1)*(h1-h0)/(volumeTanque(h1) - volumeTanque(h0))
  if (volumeTanque(hn)*volumeTanque(hn) <= 1e-9):
    return hn
  return metodoSecante(h1, hn)

h = metodoSecante(h0, h1)
print(f"A profundidade do tanque no volume de 30 m³ é de: {h}")