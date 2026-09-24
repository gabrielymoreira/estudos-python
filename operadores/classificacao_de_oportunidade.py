nivel_interesse = int(input("Nível de Interesse: "))
valor_estimado = float(input("Valor do Estimado: "))
dias_sem_contato = int(input("Quantos dias sem contato?"))

if  nivel_interesse == 3 and valor_estimado >= 1000:
    print("Prioridade Alta.")
elif nivel_interesse == 3 or dias_sem_contato > 7:
        print("Prioridade Média.")
else:
    print("Acompanhamento.")
# Ex5 - Classificação de oportunidade - intermediário
# Situação:Para que um cadastro possa ser incluído em uma campanha de relacionamento, duas exigências
# devem ser atendidas: a pessoa precisa ter autorizado o contato e deve existir pelo menos um canal digital disponível.
# Sua Tarefa:Implemente a classificação abaixo usando if, elif e else. Observe que a primeira regra deve ser verificada antes da segunda.
