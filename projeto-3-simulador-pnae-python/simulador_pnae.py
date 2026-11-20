## Parâmetro
# Valores per capita diários - Resolução CD/FNDE nº 1/2026
valCreche = 1.57
valPreEscola = 0.82
valFundamental = 0.57

# Custo dos alimentos por refeição: valor diário por aluno do ensino regular
# (uma refeição por dia) na alimentação escolar da rede estadual de SP para 2024:
# R$ 1,60 do Estado + R$ 0,50 do PNAE = R$ 2,10. Fonte: Seduc-SP, anúncio de
# 08/12/2023, publicado pela Gazeta SP e pelo SBT News:
# https://sbtnews.sbt.com.br/noticia/brasil/268064-sp-anuncia-aumento-de-quase-40-no-repasse-as-prefeituras-para-alimentacao-escolar
valRefeicao = 2.10




### funções (processo do backend)
def ler_numero(mensagem):
    numero = input(mensagem)
    while not numero.isdigit():
        print ("Por favor digite um número válido.")
        numero = input (mensagem)
    numero = int (numero)
    return numero


def classificar_porte(numMatriculas):
    if numMatriculas <= 100:
        porteEscola = "Micro"
    elif numMatriculas <= 200:
        porteEscola = "Pequena"
    elif numMatriculas <=300:
        porteEscola = "Média"
    elif numMatriculas <=400:
        porteEscola = "Grande"
    else:
        porteEscola = "Gigante"

    return porteEscola


def calcular_repasse(QTDMatricula, valUnitario, dias):
    TotalRepasse = QTDMatricula * valUnitario * dias
    return TotalRepasse

def calcular_cobertura (TotalRepasse, QTDMatricula, dias, custoRefeicao):
    Custo_Anual = QTDMatricula * dias * custoRefeicao
    if Custo_Anual == 0:
        cobertura = 0
    else:
        cobertura = TotalRepasse/Custo_Anual*100
    if TotalRepasse >= Custo_Anual:
        diferenca = 0
    else:
        diferenca = Custo_Anual - TotalRepasse
    return diferenca, Custo_Anual, cobertura

### Programa Principal ###
print ("Olá, bem-vindo ao simulador PNAE")
nome = input ("Digite o seu Nome: ")
escola = input ("Digite o nome da sua escola: ")
print (f"Olá, {nome} Vamos simular o repasse do PNAE para a escola {escola}.")
### Dias Letivos ###
diasLetivos = ler_numero ("Qual a quantidade de dias letivos no ano: ")


### Pedir as Matrículas ###
creche = ler_numero ("Digite o número de matrículas na creche: ")
preEscola = ler_numero ("Digite o número de Matrículas na pré-escola: ")
fundamental = ler_numero ("Digite o número de Matrículas no fundamental: ")

totMatricula = creche + preEscola + fundamental

repasseCreche = calcular_repasse(creche, valCreche, diasLetivos)
repassePreEscola = calcular_repasse(preEscola, valPreEscola, diasLetivos)
repasseFundamental = calcular_repasse(fundamental, valFundamental, diasLetivos)


repasseTotal = repasseCreche + repassePreEscola + repasseFundamental


porte = classificar_porte(totMatricula)

diferenca, Custo_Anual, cobertura = calcular_cobertura (repasseTotal, totMatricula, diasLetivos, valRefeicao)


print (f"RESULTADO DA SIMULAÇÃO: {escola}")
print ("Total de Matrículas: ", totMatricula)
print ("Sua Escola é de porte: ", porte)
print ("Valor a receber para a creche: R$", round(repasseCreche, 2))
print ("Valor a receber para a pré-escola: R$", round (repassePreEscola, 2))
print ("Valor a receber para o fundamental: R$", round (repasseFundamental, 2))
print ("Repasse estimado: R$", round (repasseTotal, 2))

### Cobertura do repasse ###
print ("Custo dos alimentos por refeição: R$", valRefeicao)
print ("Custo anual estimado dos alimentos: R$", round (Custo_Anual, 2))
print ("Cobertura do repasse federal:", round (cobertura, 1), "%")
if diferenca == 0:
    print ("O repasse federal cobre o custo estimado dos alimentos.")
else:
    print ("Diferença a ser coberta por outras fontes: R$", round (diferenca, 2))

print ("----- Fim dos Cálculos -----")
input ("Aperte enter para fechar")
