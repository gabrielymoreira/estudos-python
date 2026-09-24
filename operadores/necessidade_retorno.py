dias_sem_contato = int(input("Quantos dias sem contato?"))
nivel_interesse = int(input("Nível de Interesse: "))

if dias_sem_contato > 7 or nivel_interesse == 3:
    print("Realizar retorno")
else:
    print("Manter acompanhamento")

# Ex3- Necessidade de Retorno - simples
# Situação: A equipe acompanha contatos de captação. Um contato precisa receber atenção quando ficou mais de 7 dias sem retorno ou quando foi marcado com nível de interesse 3.
# Sua tarefa:  Desenvolva um programa que leia os dias sem contato e o nível de interesse e indique se a equipe deve realizar um retorno.