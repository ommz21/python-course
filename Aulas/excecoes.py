a = 2
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print("Não é permitida divisão por 0")

print(a/a)