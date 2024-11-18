
import numpy as np
from datetime import datetime


# Carregar o arquivo CSV
file_path = 'vendas.csv'  # Altere para o caminho correto do arquivo
data = np.genfromtxt(file_path, delimiter=',', dtype=None, encoding='utf-8', names=True)

# Conversão de datas para datetime
dates = np.array([datetime.strptime(row['Data'], '%Y-%m-%d') for row in data])
quantities = data['Quantidade_Vendida']
unit_prices = data['Preço_Unitário']
total_values = data['Valor_Total']
products = data['Produto']
regions = data['Região']

# Cálculo de métricas estatísticas
mean_total = np.mean(total_values)
median_total = np.median(total_values)
std_total = np.std(total_values)

# Produto com maior quantidade vendida
unique_products, quantities_sold = np.unique(products, return_counts=True)
max_quantity_product = unique_products[np.argmax(quantities_sold)]

# Produto com maior valor total de vendas
total_sales_by_product = {product: total_values[products == product].sum() for product in unique_products}
max_value_product = max(total_sales_by_product, key=total_sales_by_product.get)

# Valor total de vendas por região
unique_regions = np.unique(regions)  # Obter apenas os valores únicos
region_sales = {region: total_values[regions == region].sum() for region in unique_regions}

# Venda média por dia
unique_dates = np.unique(dates)  # Obter apenas os valores únicos
daily_sales = {date: total_values[dates == date].sum() for date in unique_dates}
average_sales_per_day = np.mean(list(daily_sales.values()))

# Exibir resultados
print("=== Análise Estatística ===")
print(f"Média do Valor Total das Vendas: R$ {mean_total:.2f}")
print(f"Mediana do Valor Total das Vendas: R$ {median_total:.2f}")
print(f"Desvio Padrão do Valor Total das Vendas: R$ {std_total:.2f}")
print(f"Produto com Maior Quantidade Vendida: {max_quantity_product}")
print(f"Produto com Maior Valor Total de Vendas: {max_value_product}")

print("\n=== Valor Total de Vendas por Região ===")
for region, sales in region_sales.items():
    print(f"{region}: R$ {sales:.2f}")

print("\n=== Venda Média por Dia ===")
print(f"R$ {average_sales_per_day:.2f}")
