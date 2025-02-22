
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor 
        # self.saldo + valor #

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    
    def get_saldo(self):
        return self.saldo 
    
contaBruna = ContaBancaria(1000)

contaBruna.sacar(700)
contaBruna.depositar(1200)

print(contaBruna.get_saldo())



