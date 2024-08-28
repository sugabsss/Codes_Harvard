import csv

candidatos = []

# Abrir e ler o arquivo CSV
with open("candidatos.csv", mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convertendo votos para inteiro
        row['Quantidade de votos'] = int(row['Quantidade de votos'])
        candidatos.append(row)

# Exibir informações dos candidatos
for candidato in candidatos:
    print(f"Nome: {candidato['nome']}, Quantidade de votos: {candidato['Quantidade de votos']}")
