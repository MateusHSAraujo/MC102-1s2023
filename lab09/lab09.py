###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Classificação de Imagens
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura de dados
N = int(input())
animalsDict = {}
models = [input() for i in range(N)]

# Processamento
for model in models:
    predAni = model.split()
    for animal in predAni:
        if animal in animalsDict:
            animalsDict[animal]+=1
        else:
            animalsDict[animal]=1

min = N/2
finalPred = []
noPred = True
for (animal,reps) in animalsDict.items():
    if reps >= min:
        noPred = False
        finalPred.append(animal)
finalPred.sort()

# Impressão da saída
if not(noPred):
    print("Animais preditos: "+", ".join(finalPred))
else:
    print("Nenhum animal foi predito")