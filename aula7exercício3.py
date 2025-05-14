dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
#print("Dias da semana:", dias_da_semana)

dias_da_semana.pop()  # remove o último item (domingo)
#print("Lista após remoção:", dias_da_semana)
#print("Tamanho da lista:", len(dias_da_semana))

dias_da_semana.append("domingo")  # adiciona de volta no final
print("Lista atualizada:", dias_da_semana)
print("Tamanho da lista:", len(dias_da_semana))
