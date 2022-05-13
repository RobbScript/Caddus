from Dados1p import *
funciopt4 = 'Error'
print('CADDUS (Beta)')
quem1 = (str(input('quem é você? ')))
print('///' * 8)
print('(Versão Beta 1.0.4)')
print('Bem vindo ao caddus {}'.format(quem1))
user = 'user'
if quem1 == 'rob':
    user = 'dev'
if quem1 == 'user':
    pass
if quem1 == 'rob':
    senha1a = (str(input('qual sua senha? ')))
    if quem1 == 'rob':
        if senha1a != senhaRob:
            print('senha inválida')
            senha1b = (str(input('tente novamente: ')))
            if senha1b != senhaRob:
                exit()
            if senha1b == senhaRob:
                pass
        if senha1a == senhaRob:
            pass
while True:
    print('////////////////////////////////////////')
    funcionalidade = 'Error'
    print('0-opções')
    respostaCad1a = str(input('{}@{}: '.format(quem1, user)))
    print('///' * 8)
    if respostaCad1a == int:
        pass
    if respostaCad1a == 'sysinfo':
        funcionalidade = 'Ok'
        print('Caddus \\ Versão Beta 1.0.4')
        print('OS primário: Linux (Debian "Bullseye")')
        print('SGDA version: SGDA 1.0 (Adam)')
        print('último update: 04/abr/22 19:35')
        print('Systemas de usuário: OK')
        print('Opções: OK')
        print('Importação de arquivos: OK')
        print('Atualizado na nuvem: OK')
    if respostaCad1a == '0':
        funcionalidade = 'Ok'
        print('1- membros')
        print('2- sair')
        print('3- projetos')
        if quem1 == 'rob':
            print('opções espceciais')
            print('4- estatísticas')
    if respostaCad1a == '1':
        funcionalidade = 'Ok'
        print(U99Z)
        print(U99Y)
        print(U99X)
        print(U99V)
        print(U99U)
        print(U99T)
    if respostaCad1a == '2':
        exit()
    if respostaCad1a == '3':
        funcionalidade = 'Ok'
        print('Caddus System')
        print('Katsi System')
        print('Golem Raid (Panir)')
    if respostaCad1a == '4':
        funcionalidade = 'Ok'
        if user == 'dev':
            print('temos essas no momento:')
            print('1- Membros')
            print('2- Fidleress & MicroTrhee')
            print('3- interatividade')
            resp41a = str(input('estatística?: '))
            if resp41a == '1':
                funciopt4 = 'Ok'
                print('temos 7 membros')
                print('3 Devs, 2 Cientistas, 4 membros')
            if resp41a == '2':
                funciopt4 = 'Ok'
                print('Fidleress')
                print('Movimento: Médio')
                print('Membros: Alto')
                print('Projetos: Elevados')
                print('Atividade: Baixa')
                print('MicroTrhee')
                print('Movimento: Baixo')
                print('Membros: Baixo')
                print('Projetos: Nenhum')
                print('Atividade: Nenhuma')
                print('temos {} pessoas do fidleress'.format(fidlemem))
                print('temos {} pessoas do microtrhee'.format(micromem))
            if resp41a == '3':
                funciopt4 = 'Ok'
                print('Fidleress')
                print('interatividade: baixa')
                print('membros ativos: alto')
                print('MicroTrhee')
                print('interatividade: nenhuma')
                print('membros ativos: baixo')
            if funciopt4 == 'Error':
                print('Digite uma opção válida')
            if funciopt4 == 'Ok':
                pass
        if user != 'dev':
            print('você não tem permissão')
    pass
    if funcionalidade == 'Error':
        print('digite algo válido')
