###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Caçada I
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura da matriz de plataformas
plataformas = []
n = int(input())

for _ in range(n):
  plataformas.append(list(input()))

m = len(plataformas[0])

# Simulação do caminho
pts = catI = catJ =0
catDir = "D"
catHitWall = 0

while catHitWall<2 and catI<n:
    nowP = plataformas[catI][catJ]
    
    if nowP == ".":
        catI+=1
        catHitWall=0    
        
    else:
        
        if nowP == "*":
            pts+=1
            plataformas[catI][catJ]="_"

        if catDir=="D" and catJ+1<m:
            catJ+=1
        elif catDir=="E" and catJ-1<0:
            catJ+=1
            catDir="D"
            catHitWall+=1
        elif catDir=="E" and catJ-1>=0:
            catJ-=1
        elif catDir=="D" and catJ+1>=m:
            catJ-=1
            catDir="E"
            catHitWall+=1
        



# Impressão da saída
print(pts)