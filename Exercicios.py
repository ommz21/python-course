# Exercicio 1: Maioridade
print("Quantos anos você tem? ", end = '')
idade = int (input())
if idade >= 18:
    print("Você é maior de idade.\n")
else:
    print("Você é menor de idade.\n")

# Ecercicio 2: Notas
for i in range(2):
    string = str(i+1)
    print(string + "° nota: ", end = '')
    nota = int (input())
    if nota >= 6:
        print("Aprovado.")
    else:
        print("Reprovado.")
print("")

# Exercicio 3: Equação de segundo grau
import math
print("Uma equação de segundo grau pode ser escrita da seguinte forma: ax² + bx + c = 0")
print("Digite os valores dos coeficientes:")
print("a = ", end = '')
a = float(input())
print("b = ", end = '')
b = float(input())
print("c = ", end = '')
c = float(input())
delta = b * b -(4 * a * c)
try:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
except ValueError:
    print("Essa equação não possui raizes reais.")
else:
    print("x = %.2f" % float(raiz1))
    print("x' = %.2f\n" % float(raiz2))

# Exercicio 4: Ordenar lista
lista = []
for i in range(3):    
    print("Digite o %i° elemento da lista: " %(i+1), end = '')
    lista.append(input())
lista.sort()
print(lista)
print("")

# Exercicio 5: Operação matemática
lista = []
for i in range(2):
    print("Digite o %i° numero: " %(i+1), end = '')
    lista.append(float(input()))
print("Digite a operação a ser efetuada entre os numeros digitados('a+b', 'a-b', 'a*b' ou 'a/b'): ", end = '')
op = input()
resultado = 0
verificador = False
if op == "+":
    resultado = lista[0] + lista[1]
elif op == "-":
    resultado = lista[0] - lista[1]
elif op == "*":
    resultado = lista[0] * lista[1]
elif op == "/":
    try:
        resultado = lista[0] / lista[1]
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
        verificador = True
else:
    print("Operação inválida.")
    verificador = True
if verificador:
    pass
else:
    print("Resultado = %.2f" %resultado)