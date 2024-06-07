###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Chuva de Meteoritos
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura de dados
(N,M) = [int(i) for i in input().split()]
matriz = [[0 for i in range(M)] for i in range(N)]

# Processamento
for met in range(int(input())):
    (metI,metJ,r) = [int(aux) for aux in input().split()]
    
    if metI>=0 and metJ>=0 and metI<N and metJ<M:
        dmgIstr = metI-(((2*r)-1)//2)
        dmgIstp = metI+(((2*r)-1)//2)
        dmgJstr = metJ-(((2*r)-1)//2)
        dmgJstp = metJ+(((2*r)-1)//2)

        for i in range(dmgIstr,dmgIstp+1):
            for j in range(dmgJstr,dmgJstp+1):
                if i>=0 and j>=0 and i<N and j<M:
                    matriz[i][j]+=1


# Impressão da saída
for linha in matriz:
  print(" ".join([str(i) for i in linha]))