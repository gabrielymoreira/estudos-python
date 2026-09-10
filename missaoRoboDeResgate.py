# Missão do Robô de Resgate
# Objetivo: decidir se um robô pode iniciar uma missão de resgate  com segurança.

bateria = int(input("Digite a porcentagem da bateria (%): "))
temperaturaDoMotor = int(input("Digite a a temperatura do motor (Cº): "))
rotaBloqueada  = input("A rota está bloqueada? (S/N) ")

if bateria < 25:
    print("Missão Cancelada: Bateria insuficiente.")
else:
    if temperaturaDoMotor > 80:
        print("Missão Cancelada: superaquecimento.")
    else:
        if rotaBloqueada == "S":
            print("Missão Autorizada com atenção: rota bloqueada.")
        else:
            print("Missão Autorizada.")
