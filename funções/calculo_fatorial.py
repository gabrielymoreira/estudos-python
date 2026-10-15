# Calcula Fatoriaal
def calcula_fatorial(numero):
  fatorial = 1
  while numero > 0:
    fatorial *= numero
    numero -= 1
  return fatorial
  
#Programa Principal
numero = int(input("Digite o número: "))
fat = calcula_fatorial(numero)
print(f"Fatorial c/ Repetição: {fat}")      
