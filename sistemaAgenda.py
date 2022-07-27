from menuPrograma import menu
from controlador import *
while True:
    opc=menu()
    if opc == 1:
        adicionarContatos()
    elif opc == 2:
        listarContatos()
    elif opc == 3:
        procurarContatos()
    elif opc == 4:
        deletarContato()
    elif opc == 5:
        editarContato()
    elif opc == 6:
        print('Programa encerrado')
        break
    else:
        print('Opção Inválida')
        print('\n')

#Executar Esse Arquivo