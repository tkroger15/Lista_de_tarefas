from time import sleep

escolha = 0
lista_de_tarefas = []
ultima_tarefa = ''


def linha():
    print('-' * 30)


def master():
    def cabecalho():
        linha()
        print('Lista de tarefas'.center(30))
        linha()
        print('''[1] Adicionar tarefa\n[2] Desfazer tarefa \n[3] Refazer tarefa\n[4] Listar tarefas\n[5] encerrar ''')
        linha()
    return cabecalho()


master()
while escolha != 5:
    try:
        escolha = input("O que deseja fazer? ")
        escolha = int(escolha)
    except:
        print('\033[31mIncorreto. Digite novamente.\033[m')
    else:
        if 1 < escolha > 5:
            print('\033[31mIncorreto. Digite novamente.\033[m')
        else:
            if escolha == 1:
                adicionar_tarefa = input('Adcione a tarefa: ')
                lista_de_tarefas.append(adicionar_tarefa)
                print('\033[32mAdcionando...\033[m')
                sleep(1)
                print('\033[32mTarefa adcionada!\033[m')
                linha()
            elif escolha == 2:
                if len(lista_de_tarefas) >= 1:
                    ultima_tarefa = lista_de_tarefas[-1]
                    lista_de_tarefas.pop()
                    print('\033[31mRemovendo...\033[m')
                    sleep(1)
                    print('\033[31mTarefa removida!\033[m')
                else:
                    print('\033[31mEI! sua lista está vazia\033[m')
                linha()
            elif escolha == 3:
                if len(ultima_tarefa) >= 1:
                    lista_de_tarefas.append(ultima_tarefa)
                    ultima_tarefa = ''
                    print('\033[32mAdcionando...\033[m')
                    sleep(1)
                    print('\033[32mTarefa adcionada!\033[m')
                else:
                    print('\033[32mParece que você não removeu nada\033[m')
                linha()
            elif escolha == 4:
                if len(lista_de_tarefas) == 0:
                    print('\033[31mSua lista está vazia!\033[m')
                else:
                    print('\033[32mListando tarefas...\033[m')
                    sleep(1)
                    linha()
                    for c in range(len(lista_de_tarefas)):
                        print(f'{c + 1}º {lista_de_tarefas[c]}')
                linha()
else:
    print('\033[32mObrigado por usar meu bloco de notas! volte sempre!\033[m')
