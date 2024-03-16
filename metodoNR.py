"""

Alunos: Fábio Menslin, Alcione Freitas e Hezb Ullah
RA: 289297, 289288, 290405
"""

# Commented out IPython magic to ensure Python compatibility.
import math #Importa a biblioteca de matemática do python
import time


h = float(input("Insira altura inicial"))
R = 3
V = 30

def volumeTanque(h):
    return V - math.pi*h*h*(3*R - h)/3

def derivadaVolume(h):
    return -2*R*math.pi*h + math.pi*h*h

def nrMethod(h):
    hn = h - (volumeTanque(h)/derivadaVolume(h))
    if ((h - hn)*(h- hn) >= 1E-8):
        return nrMethod(hn)
    else:
        return hn

h = nrMethod(h)
print(f"A altura para 30 m³ é de: {h}")