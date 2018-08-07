n_tuple = (2, 9, 15, 95, 12, 17, 20, 45, 72, 666)

impar = []
par = []

def separador():
  for index in range(len(n_tuple)):
    if (n_tuple[index] % 2 == 0):
      par.append(n_tuple[index])
    else:
      impar.append(n_tuple[index])
  return impar, tuple(par)


print(separador())