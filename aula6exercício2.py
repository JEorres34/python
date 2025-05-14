#Exercício 2: Verificação de Condições Múltiplas Desenvolva um programa que solicite a idade e o sexo do usuário. O programa deve permitir o acesso a um determinado conteúdo apenas se o usuário tiver pelo menos 18 anos e for do sexo masculino. Utilize o operador and para verificar as condições.
idade=int(input("Digite sua idade:"))
sexo=input("Digite seu sexo (masculino/feminino): ").lower()

if idade >= 18 and sexo == "masculino":
    print("Aesso permitido.")
else:
    print("Acesso negado.")
    