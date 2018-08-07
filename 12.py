import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text

requisicao = requests.get(url, timeout=5)
if requisicao.status_code != 200:
  requisicao.raise_for_status()
else:
  print("Conectado com sucesso!")

soup = BeautifulSoup(html, "lxml")

for i in soup.html.body.find_all('div', class_="tabela"):
  print(i.text)

print()
print("{:=^224}".format("Estados da Região Centro-Oeste"))
d_regiao = {}
tabela = soup.html.find("div", class_="tabela")

titulos = tabela.find("div", class_="titulo").find_all("div", class_="celula")
for i in range(len(titulos)):
  titulos[i] = titulos[i].text

for linha in tabela.find_all("div", class_="linha"):
  celulas = linha.find_all("div", class_="celula")
  d_estado = {}
  for i in range(len(celulas)):
    d_estado[titulos[i]] = celulas[i].text
  d_regiao[d_estado["Sigla"]] = d_estado
print(d_regiao)

print("{:=^224}".format("Informações sobre o Estado:"))
UF = input("Digite a UF da região centro-oeste: ")

if UF in d_regiao:
  print(d_regiao[UF])
else:
  print("Esta sigla não existe na tabela!")