from turtle import *

speed(70)


def quadrado(lados):
  for i in range(4):
    forward(lados)
    left(90)


def localizar(x, y, referencial):
  pu()
  goto(referencial + x, referencial + y)
  pd()


def forma(lados, referencial):
  metade = lados / 2
  distancia = lados / 25

  quadrado(lados)

  localizar(0, metade, distancia + referencial)
  quadrado(metade - (distancia * 2))

  localizar((metade - distancia) + (metade / 2), metade, distancia + referencial)
  circle((metade / 2) - distancia)

  localizar((metade - distancia) + (metade / 2), 0, distancia + referencial)
  circle((metade / 2) - distancia)

  localizar(distancia, distancia, referencial)

  novoLado = metade - (distancia * 2)
  novoreferencial = referencial + distancia

  forma(novoLado, novoreferencial) if lados > 1 else ''


localizar(0, 0, -250)
forma(500, -250)

exitonclick()
done()
