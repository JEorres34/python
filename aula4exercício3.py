#Exercício 3: Calculadora de Desconto Crie um programa que peça ao usuário o preço original de um produto e o percentual de desconto a ser aplicado. O programa deve calcular o valor do desconto e o preço final após o desconto.
# Solicita o preço original do produto
preco_original = float(input("Digite o preço original do produto (em R$): "))

# Solicita o percentual de desconto
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

# Calcula o valor do desconto
valor_desconto = preco_original * (percentual_desconto / 100)

# Calcula o preço final com desconto
preco_final = preco_original - valor_desconto

# Exibe os resultados
print(f"\nValor do desconto: R${valor_desconto:.2f}")
print(f"Preço final após o desconto: R${preco_final:.2f}")
