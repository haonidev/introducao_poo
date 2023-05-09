
# 1. Criar classe Pessoa 
# superclass

class Pessoa:
    
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco
        
    def andar(self):    
        print('estou andando')
        
    def falar(self): 
        print('estou falando')
            
# subclasse funcionario
# superclass as parameter
# initializing the superclass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, sexo, endereco, empresa): # metodo construtor
        self.empresa = empresa
        super().__init__(nome, idade, sexo, endereco)
    
    def trabalhar(self):
        print('Estou trabalhando')
        
    def empregador(self):
        print('Trabalho na empresa {}'.format(self.empresa))

# subclasse cliente

class Cliente(Pessoa):
    def __init__(self, nome, idade, sexo, endereco, plano_fidelidade):
        self.plano_fidelidade = plano_fidelidade
        super().__init__(nome, idade, sexo, endereco)
    
    def ir_as_compras(self):
        print('Estou fazendo compras')
        
    def plano(self):
        print('Possui o plano fidelidade: {}'.format(self.plano_fidelidade))
        
            
funcionario = Funcionario('Adão', 50, 'masculino', 'rua 10', 'google')
funcionario.empregador()
cliente = Cliente('Adelaide', 40, 'feminino', 'rua 25', 'sim')
cliente.ir_as_compras()        
cliente.plano() 

# 2. Classe Carro
# superclass

class Carro:
    
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
    def ligar(self):
        print('O {} está ligado'.format(self.modelo))
        
    def desligar(self):
        print('O {} está desligado'.format(self.modelo))
        
    def quebrar(self):
        print(' :( O {} quebrou'.format(self.modelo))

# subclasse Esportivo

class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, ano, cor, vmax, t_aceler):
        self.vmax = vmax
        self.t_aceler = t_aceler
        super().__init__(marca, modelo, ano, cor)
        
    def velocidade_maxima(self):
        print('O {} consegue atingir {} km/h'.format(self.modelo, self.vmax))
        # print('O x consegue atingir {} km/h'.format(self.modelo, self.vmax))
        
    def tempo_de_aceleracao(self):
        print('O {} leva {} segundos de 0-100 km/h'.format(self.modelo, self.t_aceler))
        
porsche = CarroEsportivo('porsche', 'porsche 911 Turbo', '2015', 'preto', '330', '2')
porsche.velocidade_maxima()
porsche.tempo_de_aceleracao()
        
class CarroSUV(Carro):
    def __init__(self, marca, modelo, ano, cor, engine, size):
        self.engine = engine
        self.size = size
        super().__init__(marca, modelo, ano, cor)
    
    def engine_power(self):
        print('O {} tem um motor de {} hp'.format(self.modelo, self.engine))
        
    def suv_size(self):
        print('O {} é uma SUV de tamanho {}.'.format(self.modelo, self.size))
        
volvo = CarroSUV('volvo', 'XC90', '2023', 'cinza', '450', 'grande')
volvo.engine_power()
volvo.suv_size()

# 3. Classe Animal
# superclass

class Animal:
    def __init__(self, classe, especie, habitat):
        self.reino = 'Animalia'
        self.classe = classe
        self.especie = especie
        self.habitat = habitat

    def alimentar(self):
        print('O animal está se alimentando')
        
    def dormir(self):
        print('O animal está dormindo')
        


class Mamifero(Animal):
    def __init__(self, especie, habitat, ninhada, desmame, classe = 'Mammalia', reino = 'Animalia'):
        # self.classe = 'Mammalia' # como deixar isso fixo?
        self.ninhada = ninhada
        self.desmame = desmame
        self.classe = classe
        super().__init__(classe, especie, habitat, reino)
    
    def num_filhotes(self): # nome diferente do atributo
        print('O {} é um animal que tem em média {} filhotes'.format(self.especie, self.ninhada))
        
    def tempo_desmame(self):
        print('O {} é um animal que leva em média {} meses para o desmame'.format(self.especie, self.desmame))

ornitorrinco = Mamifero('O.anatinus', 'semiaquatico', '2', '4')
ornitorrinco.num_filhotes() # erro
ornitorrinco.tempo_desmame() # erro
ornitorrinco.alimentar()
ornitorrinco.reino
ornitorrinco.classe

class Ave(Animal):
    def __init__(self, especie, habitat, voa, nada, classe = 'Aves', reino = 'Animalia'):
        self.voa = voa
        self.nada = nada
        self.classe = classe
        super().__init__(classe, especie, habitat, reino)
        
    def voo(self):
        print('O {} é um animal que {} voa'.format(self.especie, self.voa))
        
    def nadar(self):
        if self.nada == 'sim':
            print('O {} é um animal que nada'.format(self.especie))
        else:
            print('O {} é um animal que não consegue nadar'.format(self.especie))

pinguim_imperador = Ave('Aptenodytes forsteri', 'semiaquatico', 'não', 'sim')
pinguim_imperador.voo()    
pinguim_imperador.nadar() 
pinguim_imperador.classe
pinguim_imperador.reino

# 4. Classe Produto

class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.__list = []
        self.__estoque = []
    
    def adicionarAoCarrinho(self, val):
        self.__list.append(val)
        return self.__list
        print('Adicionados {} {} ao carrinho'.format(self.val, self.nome)) # pq nao printa?

    
    def removerDoEstoque(self, val):
        self.__estoque.append(val)
        return self.__estoque
        print('{} {} foram removidos do estoque'.format(self.val, self.nome))
        
       
sorvete = Produto('sorvete', 'sorvete de chocolate', '30', 'sim')
sorvete.adicionarAoCarrinho(3)

class Livro(Produto):
    def __init__(self, nome, descricao, preco, genero, numpag, autor):
        self.genero = genero
        self.numpag = numpag
        self.autor = autor
        super().__init__(nome, descricao, preco)
        
    def genero_livro(self):
        print('O {} é um livro do genero de {}'.format(self.nome, self.genero))
        
    def numpag(self):
        print('O {} é um livro com {} páginas'.format(self.nome, self.numpag))
        
    def autor_livro(self):
        print('O {} é um livro escrito por {}'.format(self.nome, self.autor))
        
livro = Livro('Harry Potter e a Pedra Filosofal', 'livro de fantasia', '60', 'ficção', '350', 'J.K.Rowling')
livro.autor_livro()
livro.genero_livro()    
    
    
# 5. Class Conta
# superclass

class Conta:
    def __init__(self, tipo, banco, numero, saldo_inicial):
        self.tipo = tipo
        self.banco = banco
        self.__numero = numero
        self.saldo = saldo_inicial

    def sacar(self, val):
        self.saldo -= val
    
    def depositar(self, val):
        self.saldo += val
        
    def print_saldo(self):
        print('Conta {} possui saldo de {}'.format(self.tipo, self.saldo))
        

minha_conta = Conta('c/corrente', 'bbrasil', '576363', 1000)
minha_conta.sacar(100)
minha_conta.print_saldo()
minha_conta.depositar(300)
minha_conta.print_saldo()

class ContaCorrente(Conta):
    def __init__(self, tipo, banco, numero, saldo_inicial, codigo_cc):
        self.__codigo_cc = codigo_cc
        super().__init__(tipo, banco, numero, saldo_inicial)
    
    def codigo_cc(self): # add um check de valores, daí da resposta
        print('O código de contacorrente foi inserido')
        
    def check_saldo(self):
       if self.saldo <= 0:
           print('Saldo de conta corrente insuficiente')
       else:
           print('Você possui saldo de {}'.format(self.saldo))

        
        
minha_cc = ContaCorrente('c/corrente', 'bbrasil', '576363', 1000, 'abcd')
minha_cc.codigo_cc()
minha_cc.check_saldo()