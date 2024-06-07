###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Picos e Vales II
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# leitura dos terrenos
terreno_1 = [int(i) for i in input().split()]
terreno_2 = [int(i) for i in input().split()]

# verificação das condições de sequência e quantidade
seq=False
quant=False
pv1=[]
pv2=[]

for i in range(1,len(terreno_1)-1):
    prev = terreno_1[i-1]
    itr = terreno_1[i]
    next = terreno_1[i+1]

    if itr > prev and itr > next:
        pv1.append('p')
    if itr < prev and itr < next:
        pv1.append('v')
    
for i in range(1,len(terreno_2)-1):
    prev = terreno_2[i-1]
    itr = terreno_2[i]
    next = terreno_2[i+1]

    if itr > prev and itr > next:
        pv2.append('p')
    if itr < prev and itr < next:
        pv2.append('v')

if pv1.count('v')==pv2.count('v') and pv1.count('p')==pv2.count('p'):
    quant=True

    for i in range(len(pv1)):
        if pv1[i]!=pv2[i]:
            break
    else:
        seq=True

# impressão da saída
if seq and quant:
  print("As sequências e as quantidades de picos e vales são iguais")
elif quant:
  print("As quantidades de picos e vales são iguais")
else:
  print("As sequências e as quantidades de picos e vales são diferentes")