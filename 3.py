print('RU: 3664781')

#Fiz um contador para usar no laço.
c = 0

#Uma função com algumas informações sobre o jogo, inclui alguns espaços.
def frente():
    print('\n HOTEL DE ANIMAIS \n' )
    print('*Os quartos são:')
    print('[1, 2, 3, 4]')
    print('[5, 6, 7, 8]\n')
    print('*As regras são:')
    print('O RATO não pode estar ao lado do GATO.')
    print('O CÃO não pode estar ao lado do OSSO.')
    print('O GATO não pode estar ao lado do CÃO.')
    print('O QUEIJO não pode estar ao lado do RATO.\n')

#Essa é a fase um do jogo, só inclui alguns 'prints' para mostrar ao usuário. Nas outras fases não mu-dei a estrutura, só fiz algumas mudanças nas listas, nomes e outras partes que precisavam.
def f1():
    print('Que os jogos comecem!')
    print('  Fase 1')
    print('Escolha em qual posição o RATO e o GATO devem ficar:')
    f = ['*', '*', ' ', 'G']
    ff = ['R', ' ', '*', '*']
    print(f)
    print(ff)

def f2():
    print('  Fase 2')
    print('Escolha em qual posição o CÃO, OSSO e o CÃO devem ficar:')
    f = [' ', '*', '*', '*']
    ff = ['*', 'C', ' ', ' ']
    print(f)
    print(ff)

def f3():
    print('  Fase 3')
    print('Escolha em qual posição o GATO, OSSO e o RATO devem ficar:')
    f = [' ', '*', '*', '*']
    ff = [' ', 'G', ' ', '*']
    print(f)
    print(ff)

def f4():
    print('  Fase 4')
    print('Escolha em qual posição o QUEIJO, OSSO e o QUEIJO devem ficar:')
    f = [' ', ' ', ' ', '*']
    ff = ['*', 'R', '*', '*']
    print(f)
    print(ff)

#Criei um laço para adicionar os passos do que é para executar.
while (True):
    c +=1
    frente()

#Na fase 1, adicionei umas variável e com elas o 'if'’ foi estruturado com as respostas e o que deve acontecer se acertarem. Não mudei tantas coisas nas seguintes fases. O 'if' e os 'print' foram os que sofreram mais mudanças, pois cada fase é diferente e necessita de comandos distintos
    f1()
    r = int(input('Em qual lugar o RATO deve ficar?'))
    g = int(input('Em qual lugar o GATO deve ficar?'))
    if ((r == 6) and (g == 3)):
        print('   VOCÊ GANHOU!\n')
    else:
        print('   VOCÊ PERDEU!\n')
        break

    f2()
    c = int(input('Em qual lugar o CÃO deve ficar?'))
    cc = int(input('Em qual lugar o outro CÃO deve ficar?'))
    o = int(input('Em qual lugar o OSSO deve ficar?'))
    if ((o == 1) and (c==8 or cc==8) and (c==7 or cc==7)):
        print('   VOCÊ GANHOU!\n')
    else:
        print('   VOCÊ PERDEU!\n')
        break

    f3()
    gg = int(input('Em qual lugar o GATO deve ficar?'))
    rr = int(input('Em qual lugar o RATO deve ficar?'))
    oo = int(input('Em qual lugar o OSSO deve ficar?'))
    if ((rr==1) and (oo==5) and (gg==7)):
        print('   VOCÊ GANHOU!\n')
    else:
        print('   VOCÊ PERDEU!\n')
        break

    f4()
    q = int(input('Em qual lugar o QUEIJO deve ficar?'))
    qq = int(input('Em qual lugar o outro QUEIJO deve ficar?'))
    ooo = int(input('Em qual lugar o OSSO deve ficar?'))
    if ((ooo == 2) and (q==1 or qq==1) and (q==3 or qq==3)):
        print('   PARABÉNS! VOCÊ CHEGOU A FASE FINAL.')
        break
    else:
        print('   VOCÊ PERDEU!')
        break
