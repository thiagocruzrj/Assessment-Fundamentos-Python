import requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

# Usando requests
csv = requests.get(url).text

linhas = csv.splitlines()

SUI = []
DEN = []
NOR = []

for lin in range(1, len(linhas)):
    colunas = linhas[lin].split(',')

    if int(colunas[0]) > 2001:

        if colunas[4] == 'SUI':

            if colunas[2] == 'Ice Hockey' and colunas[7] == 'Gold':
                SUI.append(colunas)

            if colunas[2] == 'Curling' and colunas[7] == 'Gold':
                SUI.append(colunas)

            if colunas[2] == 'Skating' and colunas[7] == 'Gold':
                SUI.append(colunas)

            if colunas[2] == 'Skiing' and colunas[7] == 'Gold':
                SUI.append(colunas)

    if int(colunas[0]) > 2001:

        if colunas[4] == 'NOR':

            if colunas[2] == 'Ice Hockey' and colunas[7] == 'Gold':
                NOR.append(colunas)

            if colunas[2] == 'Curling' and colunas[7] == 'Gold':
                NOR.append(colunas)

            if colunas[2] == 'Skating' and colunas[7] == 'Gold':
                NOR.append(colunas)

            if colunas[2] == 'Skiing' and colunas[7] == 'Gold':
                NOR.append(colunas)

    if int(colunas[0]) > 2001:

        if colunas[4] == 'DEN':

            if colunas[2] == 'Ice Hockey' and colunas[7] == 'Gold':
                DEN.append(colunas)

            if colunas[2] == 'Curling' and colunas[7] == 'Gold':
                DEN.append(colunas)

            if colunas[2] == 'Skating' and colunas[7] == 'Gold':
                DEN.append(colunas)

            if colunas[2] == 'Skiing' and colunas[7] == 'Gold':
                DEN.append(colunas)

print(len(SUI))
print(len(NOR))
print(len(DEN))


def calcWinner(a, b, c):
    if a > b and a > c:
        print('maior medalhista de ouro: Suiça com ', a, 'medalhas de ouro')

    if b > a and b > c:
        print('maior medalhista de ouro: Noruega com ', b, 'medalhas de ouro')

    else:
        print('maior medalhista de ouro: Dinamarca com ', c, 'medalhas de ouro')


calcWinner(len(SUI), len(NOR), len(DEN))