###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Cupons de Desconto I
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# Leitura de dados
x1,z1,x2,z2,x3,z3,n = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
val = [int(input()) for i in range(n)]

# Cálculo da melhor atribuição de cupons
desc1 = []
desc2 = []
desc3 = []


for i in val:
    # Desconto do cupom 1:
    if i>=z1:
        desc1.append(x1)
    else:
        desc1.append(0)
    
    # Desconto do cupom 2:    
    cp2 = i*(x2/100)
    if cp2 > z2:
        desc2.append(z2)
    else:
        desc2.append(cp2)

    # Desconto do cupom 3:
    if i >= z3:
        desc3.append(i*(x3/100))
    else:
        desc3.append(0)

maxSum = 0
for i in range(len(desc1)):
    for j in range(len(desc2)):
        for k in range(len(desc3)):     
            sum = desc1[i] + desc2[j] + desc3[k]
            if sum > maxSum and i!=j and i!=k and j!=k:
                maxSum =sum
                idxCp1, idxCp2, idxCp3 = i,j,k

# Impressão da resposta
print("Cupom 1:",idxCp1+1)
print("Cupom 2:",idxCp2+1)
print("Cupom 3:",idxCp3+1)