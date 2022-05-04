class ContaBancaria:
    num_contas = 0
    def __init__(self,agencia,numero,saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
    def _del_(self):
        ContaBancaria.num_contas -= 1
    def depositar(self,valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor
    def consultarSaldo(self):
        return self.saldo