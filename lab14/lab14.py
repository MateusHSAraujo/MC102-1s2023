###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Cupons de Desconto II
# Nome: Mateus Henrique Silva Araujo
# RA: 184940
###################################################

# Leitura de dados
(q1,x1,z1,q2,x2,z2,q3,x3,z3,n) = [int(input()) for i in range(10)]
compras = [int(input()) for i in range(n)]

# Cálculo da melhor atribuição de cupons
def dsctC1(val,qte):
    dsct=0
    if val>=z1 and qte>0:
        dsct=x1
    return dsct

def dsctC2(val, qte):
    dsct = val*(x2/100)
    if dsct >= z2:
        dsct = z2
    if qte<=0:
        dsct=0
    return dsct

def dsctC3(val,qte):
    dsct = 0
    if val>=z3 and qte>0:
        dsct=val*(x3/100)
    return dsct


def maxdsct(valores,q1,q2,q3,msg,idx=0): 
    c1 = dsctC1(valores[0],q1)
    c2 = dsctC2(valores[0],q2)
    c3 = dsctC3(valores[0],q3)

    if len(valores)==1:
        if c1>=c2 and c1>=c3 and q1>0 and valores[0]>=z1:
            msg+="Compra "+str(idx+1)+": Cupom 1\n"
            return c1,msg
        elif c2>c1 and c2>=c3 and q2>0:    
            msg+="Compra "+str(idx+1)+": Cupom 2\n"
            return c2,msg
        elif c3>c1 and c3>c2 and q3>0 and valores[0]>=z3:
            msg+="Compra "+str(idx+1)+": Cupom 3\n"            
            return c3,msg
        else:
            return 0, ""
    else:
        aux1=maxdsct(valores[1:],q1-1,q2,q3,msg,idx+1)
        aux2=maxdsct(valores[1:],q1,q2-1,q3,msg,idx+1)
        aux3=maxdsct(valores[1:],q1,q2,q3-1,msg,idx+1)
        aux4=maxdsct(valores[1:],q1,q2,q3,msg,idx+1)
        totalComC1, msg1 = c1 + aux1[0] , aux1[1] 
        totalComC2, msg2 = c2 + aux2[0], aux2[1]
        totalComC3, msg3 = c3 + aux3[0], aux3[1]
        totalSemC, msg4 = aux4[0], aux4[1]
        
        if (totalComC1 >= totalComC2) and (totalComC1>=totalComC3) and (totalComC1>=totalSemC) and totalComC1!=0 and q1>0 and valores[0]>=z1:
            msg1+="Compra "+str(idx+1)+": Cupom 1\n"
            return totalComC1, msg1
        elif (totalComC2 > totalComC1) and (totalComC2>=totalComC3) and (totalComC2>=totalSemC) and totalComC2!=0 and q2>0:
            msg2+="Compra "+str(idx+1)+": Cupom 2\n"
            return totalComC2, msg2
        elif (totalComC3 > totalComC1) and (totalComC3>totalComC2) and (totalComC3>=totalSemC) and totalComC3!=0 and q3>0 and valores[0]>=z3:
            msg3+="Compra "+str(idx+1)+": Cupom 3\n"
            return totalComC3, msg3
        elif (totalSemC>=totalComC1) and (totalSemC>=totalComC2) and (totalSemC>=totalComC3) or (q1==q2==q3==0):
            return totalSemC, msg4
        else:
            return 0, ""



# Impressão da resposta
msg=""
aux = maxdsct(compras,q1,q2,q3,msg,0)[1]
aux = aux.split("\n")
aux.reverse()
i = poped = 0

while i<(len(aux)):
    if aux[i]=="":
        aux.pop(i)
        poped+=1
    i+=1

toPrint="\n".join(aux)
print(toPrint)
