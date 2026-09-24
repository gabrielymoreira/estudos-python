ultimo_digito_rm = int(input("Digite o último dígito do RM: "))
penultimo_digito_rm = int(input("Digite o penúltimo dígito do RM: "))
campanha_ativa = input("Campanha está ativa?")
dias_sem_contato = int(input("Quantos dias sem contato?"))
valor_estimado = float(input("Valor do Estimado: "))

limite_dias = 3 + (ultimo_digito_rm % 5)
limite_valor = 500 + 100 * penultimo_digito_rm

print(f"Limite de dias: {limite_dias} e Limite de valor: {limite_valor}")

if campanha_ativa == "sim" and dias_sem_contato >= limite_dias:
    print("Classificação: URGENTE")
elif valor_estimado >= limite_valor or dias_sem_contato >= limite_dias:
    print("Classificação: PRIORIZAR")
else:
    print("Classificação: ACOMPANHAR")
# Ex6 - Parâmetros personalizados pelo RM - Desafio
# Situação:Cada equipe terá limites diferentes para a classificação de um contato. Esses limites serão calculados a partir dos dois últimos dígitos do RM do integrante que apresentará a solução.
# Sua tarefa:Calcule os limites definidos abaixo e, em seguida, use-os para classificar um contato em URGENTE, PRIORIZAR ou ACOMPANHAR.

