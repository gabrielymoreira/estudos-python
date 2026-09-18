# Missão de Drone de Entrega
# Objetivo: decidir se um drone pode iniciar uma entrega com segurança.

bateria = int(input("Digite a porcentagem da bateria (%): "))
velocidadeVento = int(input("Digite a velocidade do vento (km/h): "))
pesoDaCarga = int(input("Qual o peso da carga? (kg) "))

if bateria < 30:
    print("Missão Cancelada: Bateria insuficiente.")
else:
    if velocidadeVento > 40:
        print("Missão Cancelada: Vento forte.")
    else:
        if pesoDaCarga > 5:
            print("Missão Autorizada com alerta: carga pesada.")
        else:
            print("Missão Autorizada.")
