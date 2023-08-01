class SistemaBancario:
    def __init__(self):
       self.numero_saque = 0
       self.limite_saque = 3
       self.saldo = 0
       self.listagem_geral = []
       self.usuario = []
       self.contas = []
       self.num_conta = 0

    def deposito(self, value, /):
        if value >= 0:
            self.saldo += value
            self.listagem_geral.append(f'Depósito: R$ {value:.2f}')
        else:
            raise ValueError
        
    def saque(self, *, value):
        if value <= 500 and self.numero_saque < self.limite_saque and value <= self.saldo:
            self.saldo -= value
            self.numero_saque += 1
            self.listagem_geral.append(f'Saque: R$ -{value:.2f}')

        elif self.saldo < 0 or self.saldo < value:
            print('Não será possivel sacar o valor por falta de saldo')

        elif self.limite_saque == self.numero_saque:
            print('Limite de saque excedido, volte amanhã')

    def extrato(self):
        print('\nEXTRATO BANCARIO')
        for i in self.listagem_geral:
            print(i)
        print(f'R$: {self.saldo:.2f}\n')

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):    
        # Formato do endereço = logradouro, nro - bairro - cidade/estado
        for i in self.usuario:
            if i['CPF'] == cpf:
                print('Usuário já cadastrado')
                return
                
        self.usuario.append({'Nome': nome, 'Data Nascimento': data_nascimento, 'CPF':cpf, 'Endereço': endereco})
        print('Usuário Cadastrado')
                            
    def listar_usuarios(self):
        print('LISTA DE USUÁRIOS')
        for us in self.usuario:
            print(f"Nome: {us['Nome']}, Data Nascimento: {us['Data Nascimento']}, CPF: {us['CPF']}, Endereço: {us['Endereço']}")
        print()
            
    def criar_conta_corrente(self, cpf):
        usuario_encontrado = None
        AGENCIA = '0001'
        for us in self.usuario:
            if us['CPF'] == cpf:                
                usuario_encontrado = us
                break

        if usuario_encontrado:
            self.num_conta += 1
            self.contas.append({'Agência': AGENCIA, 'Número da Conta': self.num_conta, 'Usuário': usuario_encontrado})
            print('Conta criada com sucesso!')
        else:
            print('Usuário não cadastrado!')
        
    def listar_contas(self):
        print('LISTA DE CONTAS')
        for cont in self.contas:
            print(f"Agência: {cont['Agência']}, Número da Conta: {cont['Número da Conta']}, Usuário: {cont['Usuário']}")
        print()

