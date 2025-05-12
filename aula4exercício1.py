#Exercício 1: Cálculo do Perímetro e Área do Retângulo Crie um programa que solicite ao usuário a largura e a altura de um retângulo e calcule o seu perímetro e área. 
largura = float(input("digite a largura do retângulo: "))
altura = float(input("digite a altura do retângulo: "))

#calcula o perímetro e a área 
perimetro = 2 * (largura + altura)
area = largura * altura 

#exibir os resultados
print(f"Perímetro do retângulo: {perimetro}")
print(f"Área do retângulo: {area}")