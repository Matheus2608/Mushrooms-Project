#!usr/env/bin python3
list_dics = [{'b':0,'c':1,'x':2,'f':3,'k':4,'s':5},
{'f':0,'g':1,'y':2,'s':3},
{'n':0,'b':1,'c':2,'g':3,'r':4,'p':5,'u':6,'e':7,'w':8,'y':9},
{'t':0,'f':1},
{'a':0,'l':1,'c':2,'y':3,'f':4,'m':5,'n':6,'p':7,'s':8},
{'a':0,'d':1,'f':2,'n':3},
{'c':0,'w':1,'d':2},
{'b':0,'n':1},
{'k':0,'n':1,'b':2,'h':3,'g':4,'r':5,'o':6,'p':7,'u':8,'e':9,'w':10,'y':11},
{'e':0,'t':1},
{'b':0,'c':1,'u':2,'e':3,'z':4,'r':5,'?':6},
{'f':0,'y':1,'k':2,'s':3},
{'f':0,'y':1,'k':2,'s':3},
{'n':0,'b':1,'c':2,'g':3,'o':4,'p':5,'e':6,'w':7,'y':8},
{'n':0,'b':1,'c':2,'g':3,'o':4,'p':5,'e':6,'w':7,'y':8},
{'p':0,'u':1},
{'n':0,'o':1,'w':2,'y':3},
{'n':0,'o':1,'t':2},
{'c':0,'e':1,'f':2,'l':3,'n':4,'p':5,'s':6,'z':7},
{'k':0,'n':1,'b':2,'h':3,'r':4,'o':5,'u':6,'w':7,'y':8},
{'a':0,'c':1,'n':2,'s':2,'v':3,'y':4},
{'g':0,'l':1,'m':2,'p':3,'u':4,'w':5,'d':6}]

import math
def calculo_desvio_padrao(matriz, lista_media):
    desvio_padrao = 0
    lista_desvio_padrao = []
    for coluna in range(22):
        for linha in range(len(matriz)):
            desvio_padrao += (matriz[linha][coluna] - lista_media[coluna]) ** 2
        desvio_padrao = math.sqrt(desvio_padrao/Ntrain)
        lista_desvio_padrao.append(desvio_padrao)
        desvio_padrao = 0
    return lista_desvio_padrao

def calculo_media(matriz):
    media = 0
    lista_media = []
    for coluna in range(22):
        for linha in range(len(matriz)):
            media += matriz[linha][coluna]
        media = media/Ntrain
        lista_media.append(media)
        media = 0
    return lista_media

def calcula_distancia(lista1, lista2):
    x = 0
    distancia = 0
    while x < 22:
        distancia += (lista1[x] - lista2[x])**2
        x += 1
    distancia = math.sqrt(distancia)
    return distancia

def k_vizinhos(dic):
    x = dic.keys()
    x = sorted(x)
    x = x[:k]
    n_estados = []
    for key, value in dic.items():
        if key in x:
            n_estados.append(value)
    num_p = n_estados.count('p')
    num_e = n_estados.count('e')
    if num_e > num_p:
        return 'e'
    else:
        return 'p'       
#parte 1
k = int(input())
Ntrain, Ntest = input().split()
Ntrain = int(Ntrain)
Ntest = int(Ntest)
matriz_ntrain = []
for linha in range(Ntrain):
    atributos = input().split()
    for coluna in range(len(atributos)):
        for key, value in list_dics[coluna].items():#transformaçao das letras em numeros
            if atributos[coluna] == key:
                atributos[coluna] = value
    matriz_ntrain.append(atributos)

v_media = calculo_media(matriz_ntrain)
v_desvio_padrao = calculo_desvio_padrao(matriz_ntrain,v_media)
#parte 2
for linha in range(len(matriz_ntrain)):
    for coluna in range(22):
        if v_desvio_padrao[coluna] != 0:
            matriz_ntrain[linha][coluna] = (matriz_ntrain[linha][coluna] - v_media[coluna]) / v_desvio_padrao[coluna]
        else:
            matriz_ntrain[linha][coluna] = 0


#parte3 
v_estado = []
for i in range(Ntrain):
    estado = input()
    v_estado.append(estado)
#parte4
matriz_ntest = []
for linha in range(Ntest):
    atributos = input().split()
    for coluna in range(len(atributos)):
        for key, value in list_dics[coluna].items():#transformaçao das letras em numeros
            if atributos[coluna] == key:
                atributos[coluna] = value
    matriz_ntest.append(atributos)
for linha in range(len(matriz_ntest)):
    for coluna in range(22):
        if v_desvio_padrao[coluna] != 0:
            matriz_ntest[linha][coluna] = (matriz_ntest[linha][coluna] - v_media[coluna]) / v_desvio_padrao[coluna]
        else:
            matriz_ntest[linha][coluna] = 0
#parte 5

dic_estado_distancia = {}

for linha_test in range(Ntest):
    for linha_train in range(Ntrain):
        distancia = calcula_distancia(matriz_ntest[linha_test],matriz_ntrain[linha_train])
        dic_estado_distancia[distancia] = v_estado[linha_train]
    string = k_vizinhos(dic_estado_distancia)
    print(string)
    dic_estado_distancia = {}
