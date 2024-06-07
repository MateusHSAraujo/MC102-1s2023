###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Tradutor de Código Morse
# Nome: Mateus Henrique Silva Araújo
# RA: 184940
###################################################

# Leitura da frase
frase = input().split("  ")

morse = {
    ".-":"A",
    "-...":"B",
    "-.-.":"C",	
    "-..":"D",	
    ".":"E",
    "..-.":"F", 	
    "--.":"G",
    "....":"H",
    "..":"I",
    ".---":"J",
    "-.-":"K",
    ".-..":"L",
    "--":"M",
    "-.":"N",
    "---":"O",
    ".--.":"P",
    "--.-":"Q",
    ".-.":"R",
    "...":"S",
    "-":"T",
    "..-":"U",
    "...-":"V",
    ".--":"W",
    "-..-":"X",
    "-.--":"Y",
    "--..":"Z"
}

msg=""

# Conversão para letras
for palavra in frase:
    letras = palavra.split()
    for letra in letras:
        if not("*" in letra):
            msg+= morse[letra]            
        else:
            msg+="["
            prefixo=letra[:len(letra)-1]
            for chave in morse.keys():
                if chave.startswith(prefixo):
                    msg+=morse[chave]
            msg+="]"
    msg+=" "
msgF=msg[:len(msg)-1]

# Impressão da frase traduzida
print(msgF)