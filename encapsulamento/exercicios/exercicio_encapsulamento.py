# Encapsulamento

# muitas (todas?) das propriedades deveriam ser privadas, para serem acessadas somente dentro da classe
# e por meio de metodos, getters, setters


# 1 Classe Conta 

# 1 - Crie uma classe chamada ContaBancaria que representa uma conta bancária. 
# A classe deve ter atributos privados para o número da conta, o saldo e o titular da conta, 
# além de métodos públicos para depositar, sacar e verificar o saldo da conta.

# ABC: nao serve p/ ser instanciada
# é abstract class

# from abc import ABC

# class ContaBancaria(ABC):
    
#     def __init__(self, banco, numero, saldo_inicial, titular):
#         self.banco = banco
#         self.__numero = numero
#         self.__titular = titular
#         self.__saldo = saldo_inicial
        
#     def sacar(self, val):
#         self.__saldo -= val
    
#     def depositar(self, val):
#         self.__saldo += val
        
#     def print_saldo(self):
#         print('Conta {} possui saldo de {}'.format(self.tipo, self.__saldo))


# V2 da ContaBancaria
# properties: pack together methods for getting, setting, deleting and documenting the underlying data
# properties are special attributes w/ additional behavior

from abc import ABC

class ContaBancaria(ABC):
    
    def __init__(self, banco, numero, titular, saldo_inicial):

        self.__banco = banco
        self.__numero = numero
        self.__titular = titular
        self.__saldo_inicial = saldo_inicial

    @property
    def banco(self):
        return self.__banco
    
    @banco.setter
    def banco(self, novo_nome):
        self.__banco = novo_nome.upper()
        
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, novo_num):
        if isinstance(novo_num, str):
            self.__numero = novo_num
        else:
            print("Insira um número de conta válido")
       
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_nome):
        self.__titular = novo_nome.upper()
    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
  

    def sacar(self, val):
        self.__saldo_inicial -= val
    
    def depositar(self, val):
        self.__saldo_inicial += val
        
    def print_saldo(self):
        print('Conta {} possui saldo de {}'.format(self.banco, self.__saldo_inicial))

        
my_account = ContaBancaria('bbrasil', '12345', 'josefina', 500)
my_account.titular
my_account.numero
my_account.saldo_inicial
my_account.sacar(200)
my_account.print_saldo()
my_account.titular = 'joao'

my_account.numero(2000) # pq nao da a msg de erro?


# 2 Classe Pessoa

# 2 - Crie uma classe chamada Pessoa que representa uma pessoa. 
# A classe deve ter atributos privados para o nome, idade e endereço da pessoa, 
# além de métodos públicos para obter e definir esses atributos.

from abc import ABC

class Pessoa(ABC):

    def __init__(self, nome: str, idade: int, endereco = str) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print("Insira um nome válido")
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade: int):
        if nova_idade > 0 and isinstance(nova_idade, int):
            self.__idade = nova_idade
        else:
            print("Insira uma idade válida")
        
    @property
    def endereco(self):
        return self.__endereco
                
    @endereco.setter
    def endereco(self, novo_endereco):
        if isinstance(novo_endereco, str):
            self.__endereco = novo_endereco
        else:
            print("Insira um endereço válido")
    
    @nome.deleter
    def nome(self):
        del self.__nome
        print('Você deletou o nome. Por favor, insira um novo nome.')
        
pessoa = Pessoa('adelaide', 30, 'rua 10')        
pessoa.nome # queria que ja retornasse o nome em upper
pessoa.nome = 1234
pessoa.idade
pessoa.endereco
pessoa.idade = '43' # erro
del pessoa.nome
pessoa.nome 
pessoa.endereco = 'rua 30'

    
# 3
# 3 - Crie uma classe chamada CarrinhoDeCompras que representa um carrinho de compras de um cliente
# em um site de comércio eletrônico. A classe deve ter um atributo privado para os itens no carrinho,
# além de métodos públicos para adicionar e remover itens, calcular o total da compra e finalizar a compra.      

class CarrinhoDeCompras:
    
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__itens = {}
        self.__total = 0
           
    def addAoCarrinho(self, nome, preco, qtidade =1):
        
        self.__total += preco * qtidade            
        self.__itens.update({nome: qtidade})
        print('Você tem em seu carrinho: {}'.format(self.__itens))
        
    def rmvDoCarrinho(self, nome, preco, qtidade=1):
        if nome in self.__itens:
            if qtidade < self.__itens[nome] and qtidade > 0:
                self.__itens[nome] -= qtidade
                self.__total -= preco * qtidade
                print('Produto removido.'\
                      'Você tem em seu carrinho: {}'.format(self.__itens))
        elif qtidade > self.__itens[nome]:
            self.__total -= preco * self.__itens[nome]
            del self.__itens[nome]
            print('Quantidade a remover maior que quantidade de produtos')
            
    def finalizaCompra(self, saldo):
        if saldo >= self.__total:
            
            print('Obrigado por comprar conosco {}. Volte sempre.'\
                .format(self.__cliente))
            return saldo - self.__total
        else:
            print('Saldo insuficiente')
        
    
my_cart = CarrinhoDeCompras('Adelaide')    
my_cart.addAoCarrinho('xampu', 10, 2)
my_cart.addAoCarrinho('azeitonas', 20, 1)
my_cart.addAoCarrinho('queijo', 25, 1)
my_cart.rmvDoCarrinho('xampu', 10, 1)
my_cart.finalizaCompra(100)


# 4
#4 - Crie uma classe chamada Animal que representa um animal. 
# A classe deve ter atributos privados para o nome, a espécie e a idade do animal,
# além de métodos públicos para obter e definir esses atributos. 
# Além disso, a classe deve ter um método público para emitir um som característico do animal.

from abc import ABC

class Animal(ABC):
    def __init__(self, nome: str, especie: str,  idade: int, som=None):
        self.__nome = nome
        self.__especie = especie
        self.__idade = idade
        self.__som = som
        self.__reino = 'Animalia'
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print("Insira um nome válido")
    
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__especie = novo_nome
        else:
            print("Insira um nome válido")
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, novo_val):
        if isinstance(novo_val, int):
            self.__idade = novo_val
        else:
            print("Insira uma idade válida")
            
    def emitir_som(self):
        if self.__som != None:
            print('Sou um {} e meu som característico é {}'.format(self.__nome, self.__som))
        else:
            print('Inserir som característico do {}'.format(self.__nome))
            
    def descreve_animal(self):
        print('Sou um ser vivo do reino {}, meu nome popular é {}, e'\
            ' o nome científico de minha espécie é {}'.format(self.__reino, self.__nome, self.__especie))

    
mamute = Animal('mamute', 'Mammuthus africanavus', 7000)
mamute.nome = 'mamute sul-africano'
mamute.nome
mamute.idade
mamute.idade = '20'
mamute.emitir_som()
mamute = Animal('mamute', 'Mammuthus africanavus', 7000, 'UAAAA')
mamute.emitir_som()
mamute.descreve_animal()


# 5

# 5 - Crie uma classe chamada Livro que representa um livro. 
# A classe deve ter atributos privados para o título, o autor e o número de páginas do livro, 
# além de métodos públicos para obter e definir esses atributos. 
# Além disso, a classe deve ter um método público para imprimir as informações do livro em um formato legível.

class Livro(ABC):
    
    def __init__(self, titulo, autor, npags, editora, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__npags = npags
        self.__editora = editora
        self.__ano = ano
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, novo_val):
        self.__titulo = novo_val
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, novo_val):
        self.__autor = novo_val
                
    @property
    def npags(self):
        return self.__npags
    
    @npags.setter
    def npags(self, novo_val):
        self.__npags = novo_val
        
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, novo_val):
        self.__editora = novo_val
        
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, novo_val):
        self.__ano = novo_val
        
    def infos_livro(self):
        print('Informações sobre o livro: \n Título: {} \n Autor: {} \n'\
            'Número de páginas: {} \n Editora: {} \n Ano de publicação: {}'\
                ''.format(self.__titulo, self.__autor, self.__npags, self.__editora, self.__ano))
        
natureza_t_m = Livro('A Natureza da Terra-média', 'J.R.R. Tolkien', 592, 'HarperCollins Brasil', 2021)
natureza_t_m.infos_livro()