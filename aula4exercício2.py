#Exercício 2: Conversão de Moeda Desenvolva um programa que converta uma quantia em dólares para euros, usando uma taxa de câmbio fixa. O usuário deve inserir a quantia em dólares, e o programa deve calcular e exibir o valor equivalente em euros.
#taxa de câmbio fixa (exemplo: 1 dólar = 0.92 euros)
taxa_cambio = 0.92

# solicita ao usuário a quantia em dólares
dolares = float(input("digite a quantia em dólares (US$): "))

#converte para euros 
euros = dolares * taxa_cambio

#exibe o valor convertido
print(f"valor equivalente em euros: €{euros:.2f}")

#exemplo de uso 
Digite a quantia em dólares (US$): 100
Valor equivalente em euros: €92.00
