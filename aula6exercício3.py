#Exercício 3: Validador de Senha Crie um programa que peça ao usuário criar uma senha com pelo menos 8 caracteres e que contenha pelo menos uma letra maiúscula ou um número. Utilize o operador or para verificar as condições.
senha = input("Crie uma senha: ")

tem_maiuscula = any(c.isupper() for c in senha)
tem_numero = any(c.isdigit() for c in senha)

if len(senha) >= 8 and (tem_maiuscula or tem_numero):
    print("Senha válida.")
else:
    print("Senha inválida. Ela deve ter pelo menos 8 caracteres e conter uma letra maiúscula ou um número.")
