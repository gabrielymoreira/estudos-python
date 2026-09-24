autorizacao = input("Há autorização para receber contato?")
tem_email = input("Há um email disponível para contato?")
tem_whatsapp = input("Há um WhatsApp disponível para contato?")

if autorizacao == "sim" and (tem_email == "sim" or tem_whatsapp == "sim"):
    print("Cadastro pronto.")
else:
    print("Cadastro incompleto")
# Ex4 - Cadastro pronto para campanha - intermediário
# Situação: . Para que um cadastro possa ser incluído em uma campanha de relacionamento, duas exigências
# devem ser atendidas: a pessoa precisa ter autorizado o contato e deve existir pelo menos um canal digital
# disponível.
# Sua tarefa:  Crie um programa que verifique essas três informações e indique se o cadastro está pronto para a campanha.