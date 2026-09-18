numeroDeErros = int(input("Quantos erros foram encontrados no sistema?"))

if numeroDeErros < 0:
    print("Entrada inválida")
elif numeroDeErros == 0:
    print("Sistema estável")
elif numeroDeErros <= 5:
    print("Ajustes necessários")
else:
    print("Sistema crítico")
