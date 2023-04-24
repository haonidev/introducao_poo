# Exercicio 1
class Pessoa:

    def __init__(self, nome, idade, sexo, endereco):

        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def andar(self):
        print("A pessoa esta andando.")

    def falar(self):
        print("A pessoa esta falando.")


class Funcionario(Pessoa):
    pass


class Cliente(Pessoa):
    pass

# Exercicio 2


class Carro:

    def __init__(self, marca, modelo, ano, cor):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        print("O carro esta ligando.")

    def desligar(self):
        print("O carro esta desligando.")


class CarroEsportivo(Carro):
    pass


class SUV(Carro):
    pass

# Exercicio 3


class Animal:

    def __init__(self, especie, nome, habitat):

        self.especie = especie
        self.nome = nome
        self.habitat = habitat

    def andar(self):
        print("O animal esta andando.")

    def comer(self):
        print("O animal esta comendo.")


class Mamifero(Animal):
    pass


class Reptil(Animal):
    pass

# Exercicio 4


class Produto:
    def __init__(self, nome, descricao, preco, estoque):

        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def adicionarAoCarrinho(self):
        print(f"O produto {self.nome} foi adicionado ao carrinho.")

    def removerDoEstoque(self):
        print(f"O produto {self.nome} foi removido ao carrinho.")


compra1 = Produto("PS5", None, None, None)
compra1.adicionarAoCarrinho()


class Livro(Produto):
    pass


class Eletronico(Produto):
    pass

# Exercicio 5


class Conta:

    def __init__(self, conta, saldo, historico):

        self.conta = conta
        self.saldo = saldo
        self.historico = historico

    def sacar(self):
        print("Foi sacado dinheiro da sua conta.")

    def depositar(self):
        print("Foi depositado dinheiro em sua conta.")


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass
