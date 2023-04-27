

# 1 - Crie uma classe chamada ContaBancaria que representa uma conta bancária. 
# A classe deve ter atributos privados para o:
#     número da conta, 
#     o saldo e 
#     o titular da conta, 

# além de métodos públicos para 
#     depositar, 
#     sacar e 
#     verificar o saldo da conta.


class ContaBancaria:

    def __init__(self, numero, saldo, titular):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = titular
        self.taxa = 0.5

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def verificarSaldo(self):
        self.__saldo -= self.taxa
        print(f"Saldo: {self.__saldo}")


class ContaPoupanca(ContaBancaria):
    
    def __init__(self, numero, saldo, titular, taxaRendimento):
        super().__init__(numero, saldo, titular)
        self.__taxaRendimento = taxaRendimento

    @property
    def taxaRendimento(self):
        return self.__taxaRendimento

    def render(self):
        self.__saldo += self.__saldo * self.__taxaRendimento

    def verificarSaldo(self):
        print(f"Saldo: {self.saldo}")


class ContaSalario(ContaBancaria):
    
    def __init__(self, numero, saldo, titular, taxaRendimento):
        super().__init__(numero, saldo, titular)

        self.taxaRendimento = taxaRendimento

    def verificarSaldo(self):
        print(f"Saldo: {self.saldo}")



if __name__ == "__main__":
    
    contaBancaria = ContaBancaria(123, 1000, "Felipe")
    contaBancaria.depositar(100)
    contaBancaria.sacar(200)
    contaBancaria.verificarSaldo()

    contaPoupanca = ContaPoupanca(123, 1000, "Felipe", 0.05)
    contaPoupanca.depositar(100)
    contaPoupanca.sacar(200)
    contaPoupanca.verificarSaldo()

    contaSalario = ContaSalario(123, 1000, "Felipe", 0.05)
    contaPoupanca.depositar(100)
    contaPoupanca.sacar(200)
    contaPoupanca.verificarSaldo()
    
