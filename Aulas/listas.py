# -*- coding: utf-8 -*-

minha = ["abacaxi", "melancia", "abacate"]
minha2 = [1,2,3,4,5]
minha3 = ["abacaxi", 2, 9.89, True]

print(minha)
print(minha2)
print(minha3)

print(minha3[2])

for item in minha:
    print(item)

tamanho = len(minha2)

print(tamanho)

minha2.append("limão")
print(minha2)

if 3 in minha2:
    print("3 está na lista")

del minha[2:]

print(minha)

minha4 = []

minha4.append(57)

print(minha4)