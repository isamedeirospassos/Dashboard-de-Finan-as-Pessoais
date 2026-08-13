import csv
import random
from datetime import datetime, timedelta

# Dicionário com categorias e suas descrições correspondentes
categorias = {
    "Alimentação": ["Supermercado", "Restaurante", "Padaria", "Delivery"],
    "Transporte": ["Uber", "Gasolina", "Metrô", "Estacionamento"],
    "Lazer": ["Cinema", "Show", "Streaming", "Jogos"],
    "Moradia": ["Aluguel", "Conta de Luz", "Internet", "Condomínio"],
    "Saúde": ["Farmácia", "Consulta Médica", "Academia"]
}

# Data inicial para começar a gerar os gastos (ex: 1 de Janeiro de 2025)
data_inicial = datetime(2025, 1, 1)

# Preparando a primeira linha (cabeçalho)
linhas = [["Data", "Categoria", "Descricao", "Valor"]]

# Gerando 500 linhas de dados aleatórios
for _ in range(500):
    
    dias = random.randint(0, 365)
    data = (data_inicial + timedelta(days=dias)).strftime("%Y-%m-%d")

    categoria = random.choice(list(categorias.keys()))
    descricao = random.choice(categorias[categoria])
    
    if descricao == "Aluguel":
        valor = round(random.uniform(1200.0, 2500.0), 2)
    else:
        valor = round(random.uniform(15.0, 350.0), 2)
        
    linhas.append([data, categoria, descricao, valor])

with open("gastos_500.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(linhas)

print("✅ Sucesso! O arquivo 'gastos_500.csv' foi gerado com 500 linhas.")