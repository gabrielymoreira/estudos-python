tem_email = input("Há um email disponível para contato?")
tem_whatsapp = input("Há um WhatsApp disponível para contato?")

if tem_email == "sim" or tem_whatsapp == "sim":
    print("Contato possível")
else:
    print("Sem canal digital.")

# Ex2 - Canal digital disponível - simples
# Situação: Um apoiador pode ser contatado por e-mail ou por WhatsApp. Para a equipe, basta que pelo menos um desses canais esteja disponível.
# Sua tarefa: Crie um programa que leia a disponibilidade de e-mail e WhatsApp e informe se existe um canal digital para contato.
