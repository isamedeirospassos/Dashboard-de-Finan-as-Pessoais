import csv
import random
from datetime import datetime, timedelta

categorias = {
    "Alimentação": ["Supermercado", "Restaurante", "Padaria", "Delivery"],
    "Transporte": ["Uber", "Gasolina", "Metrô", "Estacionamento"],
    "Lazer": ["Cinema", "Show", "Streaming", "Jogos"],
    "Moradia": ["Aluguel", "Conta de Luz", "Internet", "Condomínio"],
    "Saúde": ["Farmácia", "Consulta Médica", "Academia"]
}

categorias_fixas = ["Moradia", "Saúde"]

data_inicial = datetime(2024, 1, 1)

linhas = [["Data", "Categoria", "Tipo", "Descricao", "Valor"]]

for _ in range(500):
    
    dias = random.randint(0, 365)
    data = (data_inicial + timedelta(days=dias)).strftime("%Y-%m-%d")

    categoria = random.choice(list(categorias.keys()))
    descricao = random.choice(categorias[categoria])
    
    # Define se o gasto é Fixo ou Variável
    tipo = "Fixo" if categoria in categorias_fixas else "Variável"
    
    if descricao == "Aluguel":
        valor = round(random.uniform(1200.0, 2500.0), 2)
    else:
        valor = round(random.uniform(15.0, 350.0), 2)
        
    linhas.append([data, categoria, tipo, descricao, valor])

with open("gastos_500.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(linhas)

print("✅ Sucesso! O arquivo 'gastos_500.csv' foi gerado com 500 linhas e a nova coluna 'Tipo'.")