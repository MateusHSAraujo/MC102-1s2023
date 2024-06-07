###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Qual o Melhor Cartão de Crédito?
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# Leitura de dados
x1,x2,Z,VP,M = int(input()), int(input()), int(input()), int(input()), int(input()),
faturas = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(faturas)) :
    faturas[i] = int(input())

# Cálculo das milhas e cashback

# Cartão Gratuito:
D1 = VP

# Cartão CashBack:
B = 0
for i in faturas:
    B+= i/100
D2 = x1+VP-B

# Cartão Milhas:
milhas = B = 0

for i in range(len(faturas)):
    milhas+=(faturas[i])//5

if M <= milhas: 
    opB1 = VP + (((milhas-M)//1000)*Z)
    opB2 = (milhas//1000)*Z
    if opB1 > opB2 :
        B = opB1
    else:
        B = opB2
else:
    B = (milhas//1000)*Z

D3 = x2+VP-B

# Achando o melhor cartão (menor despesa):
if D1 < D2 and D1 < D3:
    MELHOR_CARTAO = "Cartão Gratuito"
elif D2 < D1 and D2 < D3:
    MELHOR_CARTAO = "Cartão Cashback"
elif D3 < D1 and D3 < D2:
    MELHOR_CARTAO = "Cartão Milhas"

# Impressão da resposta

print("Cartão Gratuito: {:.2f}".format(D1))
print("Cartão Cashback: {:.2f}".format(D2))
print("Cartão Milhas: {:.2f}".format(D3))

print(MELHOR_CARTAO)