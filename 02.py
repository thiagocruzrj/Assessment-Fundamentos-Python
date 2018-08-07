def somar_pares(num):
    suma = 0;
    for n in range(0, num+1):
        if(n % 2 == 0):
            suma += n
    print(suma)

n = int(input("Entre com o valor de n: "))
somar_pares(n)