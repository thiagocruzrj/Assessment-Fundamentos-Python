import requests

class Publishes:

    def __init__(self,name):
        self.name = name
        self.count = 1
        self.sale = 0
        
    def add(self):
        self.count+=1
        
    def sale_total(self, sale):
        self.sale += sale

def top_three(input_list):
    input_list.sort()
    tops = input_list[-3:]
    q = sorted(tops, reverse=True)
    return q

def filtro(linhas):
    lista_filtro = [] 

    for l in range(1, len(linhas)):
        colunas = linhas[l].split(',')
        genero = colunas[3]
        if(genero == "Action" or genero == "Shooter" or genero == "Platform"):
            lista_filtro.append(colunas)
    return lista_filtro

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

csv = requests.get(url).text

linhas = csv.splitlines()
rotulo_col = linhas[0].split(',')

lista = filtro(linhas)

lista_publishes = []        
flag = False

for l in lista:
    for publish in lista_publishes:
        if(l[4] == publish.name):
            publish.add()
            publish.sale_total(float(l[9]))
            flag = True
            break
    if not flag:
        lista_publishes.append(Publishes(l[4]))
    flag = False
    
total = []
total_sales = []

for l in lista_publishes:
   total.append(l.count)
   total_sales.append(l.sale)
   
list1 = top_three(total)
list2 = top_three(total_sales)

jogos_publicados = []
for l in lista_publishes:
    for jp in list1:
        if jp == l.count:
           jogos_publicados.append(l)

for j in jogos_publicados:
    print(j.name, ": ", j.count)

print("--------------------")

jogos_vendidos = []
for l in lista_publishes:
    for jv in list2:
        if jv == l.sale:
           jogos_vendidos.append(l)

for j in jogos_vendidos:
    print(j.name, ": ", j.sale)