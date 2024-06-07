###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Escolha da Missão
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# leitura de dados
lvl,atk,dff,mon = int(input()), int(input()), int(input()), int(input())


# Escolha da missão
m1Reward = m2Reward = m3Reward = m4Reward = m5Reward = m6Reward = 0

m1LogicExp = (atk>=30) and (dff>=10)
if m1LogicExp:
    m1Reward = 25

m2LogicExp = (mon>=30) and (dff >=30)
if m2LogicExp :
    m2Reward =10

m3LogicExp = (lvl>=3) and (mon>=50) and (atk<dff)
if m3LogicExp:
    m3Reward = 50

m4LogicExp = (lvl>=3) and ( (mon>=20) or ( (atk>=20) and (dff >=30) ))
if m4LogicExp:
    if (atk>=20) and (dff >=30) :
        m4Reward = 40
    else:
        m4Reward = 20

m5LogicExp = (lvl>=5) and (atk>=40) and (dff>=50) and (mon>=50)
if m5LogicExp:
    m5Reward = 80

m6LogicExp = (lvl>=5) and (dff>=50)
if m6LogicExp:
    if (atk>=50):
        m6Reward = 60
    else:
        m6Reward = 30

missao = 0
ouro = mon

if m1Reward > m2Reward and m1Reward > m3Reward and m1Reward > m4Reward and m1Reward > m5Reward and m1Reward > m6Reward:
    missao = 1
    ouro += m1Reward
elif m2Reward > m1Reward and m2Reward > m3Reward and m2Reward > m4Reward and m2Reward > m5Reward and m2Reward > m6Reward:
    missao = 2
    ouro += m2Reward
elif m3Reward > m1Reward and m3Reward > m2Reward and m3Reward > m4Reward and m3Reward > m5Reward and m3Reward > m6Reward:
    missao = 3
    ouro += m3Reward
elif m4Reward > m1Reward and m4Reward > m2Reward and m4Reward > m3Reward and m4Reward > m5Reward and m4Reward > m6Reward:
    missao = 4
    ouro += m4Reward
elif m5Reward > m1Reward and m5Reward > m2Reward and m5Reward > m3Reward and m5Reward > m4Reward and m5Reward > m6Reward:
    missao = 5
    ouro += m5Reward
elif m6Reward > m1Reward and m6Reward > m2Reward and m6Reward > m3Reward and m6Reward > m4Reward and m6Reward > m5Reward:
    missao = 6
    ouro += m6Reward


# Impressão da missão escolhida
print('missão escolhida:', missao)
print('moedas de ouro:', ouro)