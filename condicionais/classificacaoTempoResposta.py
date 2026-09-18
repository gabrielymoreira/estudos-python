tempoDeResposta = float(input("Qual tempo de resposta do sistema (ms)?"))

if tempoDeResposta <= 100:
    print("Sistema Excelente")
elif tempoDeResposta <= 300:
    print("Sistema Aceitável")
elif tempoDeResposta <= 800:
    print("Sistema Lento")
else:
    print("Sistema crítico")
