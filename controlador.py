lstContatos=[]

def adicionarContatos():
    while True:
        print('-'*26)
        nome=str(input('Nome: '))
        sobrenome=str(input('Sobrenome: '))
        telefone=str(input('Telefone: '))
        endereco=str(input('Endereco: '))
        email=str(input('Email: '))
        for i, contato in enumerate(lstContatos):
            if contato[4] == email:
                print('Email já cadastrado')
                return
        contato=[nome, sobrenome, telefone, endereco, email]
        lstContatos.append(contato)
        sair=int(input('Deseja fazer mais outro cadastro ?\n [1]-Sim / [2]-Não :  '))
        if sair==2:
            break
        
    
def listarContatos():
    print('--------------------------')
    print('Nome\t\t\tTelefone')
    for i in range(0,len(lstContatos)):
        print(lstContatos[i][0],lstContatos[i][1]+'\t\t'+lstContatos[i][2])
    print('\n')

def procurarContatos():
    print('--------------------------')
    opcoes=int(input('Deseja procurar contato por:\n [1]-Nome / [2]-Endereço: '))
    if opcoes==1:
        procurar=input('Digite nome: ')
        print('--------------------------')
        contato = []
        for i, contato in enumerate(lstContatos):
            if contato[0]==procurar:
                    print(lstContatos[i][0],lstContatos[i][1]+'\t\t'+str(lstContatos[i][2]))
                    print(lstContatos[i][3]+'\t\t'+str(lstContatos[i][4]))
                    print('--------------------------')
        return
    elif opcoes==2:
        procurar=input('Digite endereço: ')
        print('--------------------------')
        contato = []
        for i, contato in enumerate(lstContatos):
            if contato[3]==procurar:
                    print(lstContatos[i][0],lstContatos[i][1]+'\t\t'+lstContatos[i][3])
                    print('--------------------------')
            return
    print('Contato não encontrado.')
    print('\n') 

def deletarContato():
    print('--------------------------')
    excluir=input('Digite email do contato: ')
    contato=[]
    for i, contato in enumerate(lstContatos):
        if contato[4]==excluir:
           opcao=int(input('Deseja remover esse contato ? [1]-Sim / [2]-Não :  '))
           if opcao==1:
               lstContatos.pop(i)
               print('Contato deletado com sucesso')
               print('\n')
               return
           elif opcao==2:
               print('Contato não deletado')
               print('\n')
               return   
    print('Contato não encontrado')

def editarContato():
    print('--------------------------')
    editar=input('Digite email do contato: ')
    contato = []
    for i, contato in enumerate(lstContatos):
        if contato[4]==editar:
            opcao=int(input('Deseja editar o nome ?: [1]-Sim / [2]-Não: '))
            if opcao==1:
                nome = input('Digite nome: ')
                contato[0]=nome
            opcao=int(input('Deseja editar o sobrenome?: [1]-Sim / [2]-Não: '))
            if opcao==1:
                sobrenome = input('Digite sobrenome: ')
                contato[1]=sobrenome
            opcao=int(input('Deseja editar o telefone ?: [1]-Sim / [2]-Não: '))
            if opcao==1:
                telefone = input('Digite telefone: ')
                contato[2]=telefone
            opcao=int(input('Deseja editar endereço?: [1]-Sim / [2]-Não: '))    
            if opcao==1:
                endereço = input('Digite endereço: ')
                contato[3]=endereço
            opcao=int(input('Deseja editar o email?: [1]-Sim / [2]-Não: '))
            if opcao==1:
                email = input('Digite email: ')
                contato[4]=email
            lstContatos[i]=contato
            print('Contato Editado com sucesso.')