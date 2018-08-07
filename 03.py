def potencia(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * potencia(a, b - 1)

a = int(input("Digite a base: "))
b = int(input("Digite o expoente: "))

print("A potência é: ", potencia(a, b))