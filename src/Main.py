import json

# Abrindo arquivo JSON
with open("lib/dados.json") as arquivo:
    dados_json = json.load(arquivo)
    
# Criando vetores para armazenar dados do arquivo JSON
dias = []
valores = []

# Adicionando dados aos vetores
for dado in dados_json:
    dia = dado['dia']
    valor = dado['valor']
    dias.append(dia)
    valores.append(valor)

# Função para calcular menor faturamento
def calcular_menor_faturamento(vetor):
    menor_faturamento = min(vetor)
    return f"Menor faturamento: {menor_faturamento}"
    
# Função para calcular maior faturamento
def calcular_maior_faturamento(vetor):
    maior_faturamento = max(vetor)
    return f"Maior faturamento: {maior_faturamento}"
    
# Função para selecionar valores acima da média mensal
def acima_da_media(vetor):
    media_mensal = sum(vetor) / len(vetor)
    valores_acima_da_media = [val for val in vetor if val > media_mensal]
    return f"Média mensal: {media_mensal}, Valores acima da média: {valores_acima_da_media}." 

# Exibindo menu
print("+", "-"*38, "+")
print("|           FATURAMENTO MENSAL           |")
print("+", "-"*38, "+")
print("|      O que você deseja consultar?      |")
print("+", "-"*38, "+")
print("|      1 - Menor faturamento mensal      |")
print("+", "-"*38, "+")
print("|      2 - Maior faturamento mensal      |")
print("+", "-"*38, "+")
print("| 3 - Faturamentos acima da média mensal |")
print("+", "-"*38, "+")

# Loop criado para caso o input do usuário seja inválido o sistema não finalize
loop = True
# Recebendo o input do usuário e executando a função correspondente ao valor inserido
while loop:
    try:
        op = int(input("Insira o número da opção: "))
        if op == 1:
            print(calcular_menor_faturamento(valores)) 
            loop = False
        elif op == 2:
            print(calcular_maior_faturamento(valores))
            loop = False
        elif op == 3:
            print(acima_da_media(valores))
            loop = False
        else:
            print("insira uma opção válida!")
    except:
        print("insira uma opção válida!")
        






