###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Novos Algoritmos de Ordenação
# Nome: Mateus Hnerique Silva Araujo
# RA: 184940
###################################################

def minimumIdx(vct,str):
    min , idx = vct[str] , str
    
    for i in range(str,len(vct)):
        if vct[i] < min:
            idx = i
            min = vct[i]
    
    return idx

def checkOrder(lista):
    prev=lista[0]
    for i in range(1,len(lista)):
        if prev > lista[i]:
            return False
        else:
            prev = lista[i]
    return True

'''
Recebe uma lista de elementos e retorna o número de trocas realizadas pelo algoritmo Seleção e Inserção.
Essa função deve imprimir a lista de elementos após cada inserção.
'''
def selecao_e_insercao(lista):
    swps = prevswps = 0
    
    for i in range(1,len(lista)):
        minIdx = minimumIdx(lista,i)
        min = lista[minIdx]
        j = minIdx-1
        
        while j>=0 and lista[j]>min:
            lista[j+1]=lista[j]
            j-=1
            swps+=1
        
        lista[j+1]=min
        if prevswps!=swps:
            print(lista)
        prevswps=swps

        if checkOrder(lista):
            break

    return swps

'''
Recebe uma lista de elementos e retorna o número de trocas realizadas pelo algoritmo Bubble Up and Down.
Essa função deve imprimir a lista de elementos sempre que o algoritmo fizer a verificação da completa lista.
'''
def bubble_up_and_down(lista):
    swps = prevswps = 0
    drctStp = len(lista)-1
    rvrsStp = 0

    while drctStp>rvrsStp:
        for i in range(rvrsStp,drctStp):
            if lista[i] > lista[i+1]:
                lista[i] , lista[i+1] = lista[i+1], lista[i]
                swps+=1
        if prevswps == swps:
            if swps==0:
                print(lista)
            break
        else:
            prevswps = swps
            print(lista)
            drctStp-=1

        for i in range(drctStp,rvrsStp,-1):
            if lista[i] < lista[i-1]:
                lista[i] , lista[i-1] = lista[i-1], lista[i]
                swps+=1
        
        if prevswps == swps:
            break
        else:
            prevswps = swps
            print(lista)
            rvrsStp+=1

    return swps

# Leitura da sequência
lista = [int(a) for a in input().split()]

# Execução dos algoritmos de ordenação e impressão dos resultados
print("Algoritmo Seleção e Inserção:")
X = selecao_e_insercao(lista.copy())
print("Trocas realizadas:", X)
print()
print("Algoritmo Bubble Up and Down:")
Y = bubble_up_and_down(lista.copy())
print("Trocas realizadas:", Y)
