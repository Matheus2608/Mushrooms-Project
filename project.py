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
def calculus_standard_deviation(matrix, avarage_list):
    standard_deviation = 0
    list_standard_deviation = []
    for colun in range(22):
        for line in range(len(matrix)):
            standard_deviation += (matrix[line][colun] - avarage_list[colun]) ** 2
        standard_deviation = math.sqrt(standard_deviation/Ntrain)
        list_standard_deviation.append(standard_deviation)
        standard_deviation = 0
    return list_standard_deviation

def calculus_avarage(matrix):
    avarage = 0
    avarage_list = []
    for colun in range(22):
        for line in range(len(matrix)):
            avarage += matrix[line][colun]
        avarage = avarage/Ntrain
        avarage_list.append(avarage)
        avarage = 0
    return avarage_list

def calculus_distance(list1, list2):
    x = 0
    distance = 0
    while x < 22:
        distance += (list1[x] - list2[x])**2
        x += 1
    distance = math.sqrt(distance)
    return distance

def k_neighbors(dic):
    x = dic.keys()
    x = sorted(x)
    x = x[:k]
    n_features = []
    for key, value in dic.items():
        if key in x:
            n_features.append(value)
    num_p = n_features.count('p')
    num_e = n_features.count('e')
    if num_e > num_p:
        return 'e'
    else:
        return 'p'       
#part 1
k = int(input())
Ntrain, Ntest = input().split()
Ntrain = int(Ntrain)
Ntest = int(Ntest)
matrix_ntrain = []
for line in range(Ntrain):
    attributes = input().split()
    for colun in range(len(attributes)):
        for key, value in list_dics[colun].items():#transformaçao das letras em numeros
            if attributes[colun] == key:
                attributes[colun] = value
    matrix_ntrain.append(attributes)

v_avarage = calculus_avarage(matrix_ntrain)
v_standard_deviation = calculus_standard_deviation(matrix_ntrain,v_avarage)
#part 2
for line in range(len(matrix_ntrain)):
    for colun in range(22):
        if v_standard_deviation[colun] != 0:
            matrix_ntrain[line][colun] = (matrix_ntrain[line][colun] - v_avarage[colun]) / v_standard_deviation[colun]
        else:
            matrix_ntrain[line][colun] = 0

#part 3
v_feature = []
for i in range(Ntrain):
    estado = input()
    v_feature.append(estado)
#part 4
matrix_ntest = []
for line in range(Ntest):
    attributes = input().split()
    for colun in range(len(attributes)):
        for key, value in list_dics[colun].items():#transforming letters in numbers
            if attributes[colun] == key:
                attributes[colun] = value
    matrix_ntest.append(attributes)
for line in range(len(matrix_ntest)):
    for colun in range(22):
        if v_standard_deviation[colun] != 0:
            matrix_ntest[line][colun] = (matrix_ntest[line][colun] - v_avarage[colun]) / v_standard_deviation[colun]
        else:
            matrix_ntest[line][colun] = 0
#part 5

dic_feature_distance = {}

for line_test in range(Ntest):
    for line_train in range(Ntrain):
        distance = calculus_distance(matrix_ntest[line_test],matrix_ntrain[line_train])
        dic_feature_distance[distance] = v_feature[line_train]
    string = k_neighbors(dic_feature_distance)
    print(string)
    dic_feature_distance = {} 
