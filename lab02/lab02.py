###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Trem das Onze
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# Leitura de dados
h1,m1,km1,v1= float(input()),int(input()),int(input()),int(input())
h2,m2,km2,v2= float(input()),int(input()),int(input()),int(input())

# Cálculo do tempo gasto para chegar a parada do trem
h1+=(m1/60)
h2+=(m2/60)

t1=h1+(km1/v1)
t2=h2+(km2/v2)

resp = (t1<=h2) and (t2<=11)

# Impressão da resposta
print(resp)