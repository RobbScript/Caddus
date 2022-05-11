from xml.dom.expatbuilder import parseString
from Dados import *
from pygame import *
import time
import os
funciopt4 = 'Error'
user_u = 'User'
funcionalidade = False
def AcionLT():
    time.sleep(1)
    os.system ('clear') or None
while True:
    os.system ('clear') or None
    print('///' * 8)
    print('CADDUS Nano (Alpha)')
    quem1 = (str(input('quem é você? ')))
    if (quem1 == 'rob'):
     while True:
        senha1 = (str(input('digite seu código: ')))
        if (senha1 == '8642'):
            user_u = 'Dev'
            AcionLT()
            print(f'olá {quem1}!...')
            AcionLT()
            break
        if (senha1 != '8642'):
            AcionLT()
            print('Verificando...')
            AcionLT()
            print('senha incorreta')
            AcionLT()
            print('tente novamente: ')
            pass
    if (quem1 != 'rob'):
        user_u = ('User')
        pass
    if (quem1 == 'rob'):
        print('bem vindo ao Caddus Nano, Rob!')
    if (quem1 != 'rob'):
        print(f'Olá {quem1}! bem vindo ao Caddus Nano')
    AcionLT()
    while True:
        print('Caddus Nano (Menu)')
        print('options: ')
        print('-sysinfo (sistema)')
        print('-l (logoff)')
        print('-0 (Sair)')
        print('-1 (membros)')
        print('-2 (projetos)')
        print('-3 informações')
        respmen1 = (str(input(f'{quem1}@{user_u}: ')))
        if (respmen1 == 'sysinfo'):
            funcionalidade = True
            os.system ('clear') or None
            for k in Sysinfos:
                print (k)
                time.sleep(0.5)
            nada = str(input('digite Enter para voltar...'))
            os.system ('clear') or None
            pass
        if (respmen1 == 'l'):
            os.system ('clear') or None
            break
        if (respmen1 == '1'):
            funcionalidade = True
            os.system ('clear') or None
            for i in Membros:
                print (i)
                time.sleep(0.5)
            nada = str(input('digite Enter para voltar...'))
            os.system ('clear') or None
            pass
        if (respmen1 == '2'):
            funcionalidade = True
            os.system ('clear') or None
            for j in Projetos:
                print (j)
                time.sleep(0.5)
            nada = str(input('digite Enter para voltar...'))
            os.system ('clear') or None
            pass
        if (respmen1 == '3'):
            funcionalidade = True
            os.system ('clear') or None
            print('informações:')
            print('-Yan')
            print('-Rapha')
            print('-Vini')
            resp3mem = str(input('Qual membro?: '))
            os.system ('clear') or None
            if (resp3mem == 'yan'):
                for x in YanDados:
                    print (x)
                    time.sleep(0.5)
                nada = str(input('digite Enter para voltar...'))
                pass
            if (resp3mem == 'vini'):
                for x in ViniDados:
                    print (x)
                    time.sleep(0.5)
                nada = str(input('digite Enter para voltar...'))
                pass
            if (resp3mem == 'rapha'):
                for x in RaphaDados:
                    print (x)
                    time.sleep(0.5)
                nada = str(input('digite Enter para voltar...'))
                pass
            else:
                print('digite algo válido')
                AcionLT()
                pass
            os.system ('clear') or None
        if( respmen1 == '0'):
            exit()
        if (funcionalidade == False):
            os.system ('clear') or None
            print('digite algo válido')
            AcionLT()
            pass
pass

    

