import os
os.system ('cls') 

# Programa para calcular o preço final de um produto em reais, considerando a cotação do dólar e um imposto de 17%

# Solicita a cotação do dólar
cotacao_dolar = float(input("Digite a cotação do dólar de hoje: "))

# Solicita o preço do produto em dólares
preco_produto_dolar = float(input("Digite o preço do produto em dólares: "))

# Calcula o preço do produto em reais
preco_produto_reais = preco_produto_dolar * cotacao_dolar

# Calcula o ICMS de 17% sobre o preço do produto em reais
imposto_icms = preco_produto_reais * 0.17

# Calcula o imposto de 20% sobre o preço do produto em reais com INSS
imposto_total = imposto_icms * 0.20


# Calcula o preço final do produto em reais, incluindo o imposto
preco_final_reais = preco_produto_reais + imposto_total

# Exibe o resultado formatado com duas casas decimais
print(f"O preço final do produto em reais, incluindo os impostos é: R${preco_final_reais:.2f}")