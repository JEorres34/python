aluno={"nome": "Claudio", "idade": 28 , "turno":"tarde"}

#posso recuperar o elemento , vamo supor que eu quero o nome do aluno,vou chamar pelo dicionário (aluno)
print(aluno["nome"])#claudio
#se eu buscar pela chave "idade"
print(aluno["idade"])#28
#se eu buscar pela chave "turno"     
print(aluno["turno"])#tarde

#Manipulando dados de um dicionário
#podemos alterar os valores por meio de sua chave e , se a chave não existir , o dicionário insere uma nova chave e armazena o valor.
#vamo supor que o claudio fez aniversário , ele vai ter 29 anos
aluno["idade"]=29
print(aluno) 
