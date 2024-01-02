print('RU: 3664781')

#Criei um laço, com um contador, para exibir a mesma mensagem até que o usuário pare.
c = 0
while (True):
    print('     CLASSIFICAÇÃO DE ETAPA DE ENSINO     ')

#Fiz duas variáveis para inserir as informações.
    n = input('Nome?')
    i = int(input('Qual a idade?'))

#Utilizei a variável 'i' para comparar em qual ensino está e mostrei ao usuário o resultado. Adicionei o contador aqui, para não ficar repetindo em um loop infinito.
    if(i != 0):
        if (i <= 5):
            print('{} está com {} anos, cursando a educação infantil.' .format(n, i))
        elif (i <= 10):
            print('{} está com {} anos, cursando o ensino fundamental I' .format(n, i))
        elif (i <= 14):
            print('{} está com {} anos, cursando o ensino fundamental II' .format(n,i))
        elif (i >= 15):
            print('{} está com {} anos, cursando o ensino médio' .format(n, i))
    else:
        print('A idade digitada não está inclusa.')
        c += 1

# Aqui também adicionei uma pergunta para caso desejem encerrar o programa ou começar tudo de novo.
    t = input('Deseja continuar o programa (1-Sim   2-Não)?')
    if (t == '1'):
        continue
    else:
        break
