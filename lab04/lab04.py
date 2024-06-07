###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Picos e Vales I
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################


# leitura e verificação dos picos e vales
picos = 0
vales = 0

prev = int(input())
if prev!=0:
    itr = int(input())
    if itr!= 0:
        next = int(input())
        while next!=0 :
            if prev < itr and next < itr:
                picos+=1
            elif prev > itr and next > itr:
                vales+=1
            prev = itr
            itr = next
            next = int(input())

# impressão da saída
print("Quantidade de picos:", picos)
print("Quantidade de vales:", vales)