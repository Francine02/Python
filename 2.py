print('RU: 3664781')

#Uma variável para receber a informação e depois usar ela em outras partes. Também usei 'import' para indicar o que desejo usar.

n = input('Qual seu nome?')
import re

#Defini uma função para caso o usuário escreva em minúsculo mudar a letra para maiúscula
def m ():
    if (n.lower()):
        mm = n.upper()
        print('{}' .format(mm))

#Outra função, essa para mudar as vogais para símbolos, usei o 'find' para buscar a vogal que queria encontrar e depois que fosse achada usei outro comando para substituir a vogal por um símbolo.
def s():
    if (n.lower()):
        mm = n.upper()
        if (mm.find('A')):
            mm = re.sub('A', '@', mm)
        if (mm.find('E')):
            mm = re.sub('E', '&', mm)
        if (mm.find('I')):
            mm = re.sub('I', '!', mm)
        if (mm.find('O')):
            mm = re.sub('O', '#', mm)
        if (mm.find('U')):
            mm = re.sub('U', '*', mm)
        print(mm)

#Chamei as funções para executar e elas apareceram na tela já que tinham 'print' dentro da função.
m()
s()
