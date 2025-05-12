#Exercício 1: Verificação de Número no Intervalo Crie um programa que peça ao usuário um número e verifique se ele está no intervalo entre 10 e 20 (inclusive). Utilize o operador and para fazer a verificação.
numero = int(input("Digite um número: "))

if numero >= 10 and numero <= 20:
    print("o número está entre 10 e 20.")
else:
    print("o número está fora do intervalo entre 10 e 20.")