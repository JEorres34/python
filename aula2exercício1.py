#Exercício 1: Cálculo de Juros Compostos Crie um programa que calcule o montante final de um investimento com juros compostos. O programa deve solicitar ao usuário o valor principal, a taxa de juros anual e o número de anos de investimento. Em seguida, ele deve calcular e exibir o montante total.
p=float(input("valor inicial: ")) # O programa deve solicitar ao usuário o valor principal
r=float(input("juros anual: ")) /100 # O programa deve solicitar ao usuário a taxa de juros anual
t=int(input("anos: ")) # número de anos de investimento
print("montante", round(p*(1+r)**t,2 )) #Em seguida, ele deve calcular e exibir o montante total.

