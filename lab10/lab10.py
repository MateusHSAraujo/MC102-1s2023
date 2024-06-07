#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Carrinho Elétrico
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
#####################################################

# Leitura do circuito
n, m = [int(i) for i in input().split()]

voltas = 0

pista = []
for _ in range(n):
  linha = input().split()
  pista.append(linha)

startI = carI = nextCarI = 0
startJ = carJ = nextCarJ = 0

for i in range(n):
    for j in range(m):
        if pista[i][j] == "-":
            startI = carI = nextCarI = i
            startJ = carJ = nextCarJ =j
            break


# Leitura e processamento das instruções
instr = input()
while instr!="0":
    (amount,direct) = instr.split()
    amount = int(amount)
    while amount!=0:
        if direct == "N":
            nextCarI-=1
        if direct == "S":
            nextCarI+=1
        if direct == "O":
            nextCarJ-=1
        if direct == "L":
            nextCarJ+=1

        if nextCarI<0 or nextCarJ<0 or nextCarI>=n or nextCarJ>=m or (pista[nextCarI][nextCarJ]=="#"):
            nextCarI = carI
            nextCarJ = carJ
            break
        else:
            carI = nextCarI
            carJ = nextCarJ
            if pista[carI][carJ]=="-":
                voltas+=1

        amount-=1

    instr = input()

# Impressão da saída
print('Voltas completadas:', voltas)
