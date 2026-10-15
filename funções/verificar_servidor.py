# Função que lê os dados e classifica a situação
def verificar_servidor():
    nome_servidor = input("Nome do Servidor: ")
    uso_cpu = float(input("Percentual de Uso da CPU: "))
    
    if uso_cpu >= 90:
        situacao = "Crítico"
    elif uso_cpu >= 70:
        situacao = "Atenção"
    else: 
        situacao = "Normal"
    
    print(f"""
    
    VERIFICADOR DE Servidor
    Servidor: {nome_servidor}
    Situação: {situacao}
    
    
    """)
    
# Código Principal - chamada daa função
verificar_servidor()
