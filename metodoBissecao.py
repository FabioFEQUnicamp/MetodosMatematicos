'''
Implementação do método da bisseção - com relação ao problema proposto em sala de volume do reservatório
Alunos: Fábio Menslin, Alcione Freitas e Hezb Ullah
RA: 289297, 289288, 290405
Implementação em Python
'''

import math

R = 3.0 #Define o raio do reservatório
pi = math.pi #Atribui o valor de pi da biblioteca Math para a variável pi
V = float(input("Digite o volume alvo (em m³): ")) #Solicita ao usuário o volume alvo

#Define o cálculo da função de volume
def func_vol(h):
    return V - pi*h*h*(3*R-h)/3

#Verifica se o intervalo a0 e b0 possuem valores de função com sinais inversos
def checa_intervalo(a0, b0):
    fa = func_vol(a0)
    fb = func_vol(b0)
    return fa*fb > 0

#Implementação do método da bisseção
def metodo_bissecao(a0, b0): #Chama a função, passando como parâmetros a0 e b0
    fa = func_vol(a0) #Calcula f(a0)
    fm = func_vol((b0+a0)*0.5) #Calcula f(m) - sendo m o valor da média aritmética de a0 e b0
    if(abs(fm) > 1e-6): #Verifica o quão próximo do erro é o resultado de f(m)
        #se ele for maior que o erro:
        if (fa*fm > 0): #Calcula o valor de fa*fm que se for maior que 0, implica que m está na mesma seção que a 
            a0 = (b0+a0)*0.5 #Substitui o valor da variável a0 por m
        else: b0 = (b0+a0)*0.5 #Caso contrário, significa que o valor de m estava na mesma seção de b, dessa forma substituímos o valor de b0 por m
        return metodo_bissecao(a0, b0) #Feito isso, chamamos novamente a função (recurssividade) 
    else: #caso contrário, o valor de fm é menor que nossa tolerância - erro, significa que chegamos a um valor aceitável de raiz
        return (b0+a0)*0.5 #retornamos o valor de m, calculado como b0+a0

#Área de inserção de dados
print("Digite o intervalo de busca (em m): ")
a0 = float(input("a0: "))
b0 = float(input("b0: "))
#Checagem se o intervalo é válido
if (checa_intervalo(a0, b0)):
    print("Intervalo invalido f({}) e f({}) resultam em valor positivo - método falhou")
else: #Se o intervalo for válido, chama o método da bisseção
    h = metodo_bissecao(a0, b0)
    print("A profundidade do tanque para o volume de {} m³ é: {} m".format(V, h))
