class SistemaBancario:
    def __init__(self):
       self.numero_saque = 0
       self.limite_saque = 3
       self.saldo = 0
       self.listagem_geral = []

    def deposito(self, value):
        if value >= 0:
            self.saldo += value
            self.listagem_geral.append(f'Depósito: R$ {value:.2f}')
        else:
            raise ValueError
        
    def saque(self, value):
        if value <= 500 and self.numero_saque < self.limite_saque and value <= self.saldo:
            self.saldo -= value
            self.numero_saque += 1
            self.listagem_geral.append(f'Saque: R$ -{value:.2f}')

        elif self.saldo < 0 or self.saldo < value:
            print('Não será possivel sacar o valor por falta de saldo')

        elif self.limite_saque == self.numero_saque:
            print('Limite de saque excedido, volte amanhã')

    def extrato(self):
        print('EXTRATO BANCARIO')
        for i in self.listagem_geral:
            print(i)
        print(f'R$: {self.saldo:.2f}')

#Testes
sistema = SistemaBancario()
sistema.deposito(1000)
sistema.extrato()
sistema.saque(300)
sistema.extrato()
sistema.deposito(400)
sistema.extrato()
sistema.saque(400)
sistema.saque(500)
sistema.extrato()
sistema.saque(200)
sistema.extrato()