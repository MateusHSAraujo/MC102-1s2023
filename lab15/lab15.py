###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - A Caçada II
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

'''
Função para simular o caminho do gato, essa função deve
ser implementado de forma recursiva. A função Recebe uma
matriz representando as plataformas e a posição (linha,coluna)
do gato. A função deve retornar o numero de petiscos recolhidos.
'''
def simula_caminho(matriz, i, j, dir, viradas, ptsDirAtual):

    if viradas > 2 or i>=len(matriz):
        if viradas==3:
            return 0 , True
        else:
            return 0, False
     
    else:
        cop=copia(matriz)

        if j<0 or (j<len(matriz[0]) and matriz[i][j]=="|" and dir=="E"):
            if ptsDirAtual>0:
                viraCaminho, linhaCompleta = simula_caminho(cop,i,j+1,"D",viradas+1,0)
                return viraCaminho, linhaCompleta
            else:
                if viradas==2:
                    return 0, True
                else:
                    return 0, False

        if j>=len(matriz[0]) or (j>=0 and matriz[i][j]=="|" and dir=="D"):
            if ptsDirAtual>0:
                viraCaminho, linhaCompleta = simula_caminho(cop,i,j-1,"E",viradas+1,0)
                return viraCaminho, linhaCompleta
            else:
                if viradas==2:
                    return 0, True
                else:
                    return 0, False
        
        pts = 0
        if cop[i][j]=="*":
            pts+=1
            ptsDirAtual+=1
            cop[i][j]="_"
        
        #printa(matriz,i,j)
        
        if dir=='D':
            caminhoH , linhaCompletaH = simula_caminho(cop,i,j+1,"D",viradas,ptsDirAtual)
        if dir=='E':
            caminhoH , linhaCompletaH = simula_caminho(cop,i,j-1,"E",viradas,ptsDirAtual)
        if dir=='B':
            caminhoH, linhaCompletaH = simula_caminho(cop,i,j+1,"D",viradas,ptsDirAtual)
            if not(linhaCompletaH):
                caminhoE, linhaCompletaE = simula_caminho(cop,i,j-1,"E",viradas,ptsDirAtual)
                if caminhoE>caminhoH:
                    caminhoH=caminhoE
                    linhaCompletaH = linhaCompletaE

        caminhoB, linhaCompletaB = 0, False
        if cop[i][j]==".":
            if dir == "B":
                return simula_caminho(cop,i+1,j,"B",0,0)
            else:
                caminhoB, linhaCompletaB = simula_caminho(cop,i+1,j,"B",0,0)[0], False

        if caminhoH>=caminhoB:
            return pts+caminhoH, linhaCompletaH
        else:
            return pts+caminhoB, linhaCompletaB

''' DEBBUG
def printa(matriz,i,j):
    print("\n"+("-"*len(matriz[0])))
    aux = matriz[i][j]
    matriz[i][j]="G"
    for a in matriz:
        print("".join(a))
    matriz[i][j]=aux
'''

def copia(matriz):
    aux=[]
    for k in matriz:
        aux.append(k.copy())
    return aux


# Leitura da matriz de plataformas
plataformas = []
n = int(input())
for _ in range(n):
  plataformas.append(list(input()))

# Simulação do caminho
pts = simula_caminho(plataformas,0,0,"D",0,0)[0]


# Impressão da saída
print(pts)