#Exercício 3: Calculadora de IMC Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar ao usuário o peso em quilogramas e a altura em metros, e em seguida calcular e exibir o IMC.
peso=float(input("digite o peso: "))
altura=float(input("digite o altura: "))
print("imc:", round(peso/altura**2,2))