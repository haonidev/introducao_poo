
# 1
# 1 - Pensando como acontece no mundo real, crie uma classe de pessoa
# que saiba realizar pagamento de boleto no caixa do banco.





# 2
#2 - Crie uma classe para emular
# aquele joguinhos de pegar ursinho que tem nos shoppings.

from typing import Type

class PegaUrsinho:
    
    def __init__(self, cor_ursinho):
        self.__cor_ursinho = cor_ursinho
        # self.__num_fichas = num_fichas
        
    def __pega_ursinho(self): # como deixar esse metodo privado e acessado somente pela pessoa?
        print('Movendo o  controlador...'\
            'Pegando o ursinho {}'.format(self.__cor_ursinho))


class Pessoa:
    
    def __init__(self, num_fichas=0):
        self.num_fichas = num_fichas
    
    def inicia_jogo (self, jogo: Type[PegaUrsinho]):
        if self.num_fichas <= 0:
            print('Você não tem fichas para jogar. Compre uma ficha.')
        else:
            print('Iniciando o jogo...')
            jogo._PegaUrsinho__pega_ursinho() # acessa o private method da classe
            self.__finaliza_jogo()
        
    def __finaliza_jogo(self):
        print('Jogo finalizado. Insira uma ficha para iniciar o jogo')

eu = Pessoa(1)
eu.num_fichas
jogo1 = PegaUrsinho('azul') 
dir(jogo1)
jogo1.__pega_ursinho() # aqui n faz tt sentido comandar o jogo por essa classe, mas sim pela da pessoa??
eu.inicia_jogo(jogo1)








# 3
# 3 - Crie uma classe que saiba dirigir um carro.

from abc import ABC

class Carro(ABC):
    
    def __init__(self, marca, modelo, ano, kilometragem, meses_da_ultima_revisao):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__kilometragem = kilometragem
        self.__meses_da_ultima_revisao = meses_da_ultima_revisao
        
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, new_val):
        self.__marca = new_val
                        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, new_val):
        self.__modelo = new_val
            
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, new_val):
        self.__ano = new_val
            
    @property
    def kilometragem(self):
        return self.__kilometragem
    
    @kilometragem.setter
    def kilometragem(self, new_val):
        if new_val > 0 and isinstance(new_val, int):
            self.__kilometragem = new_val
        else:
            print("Insira um valor de kilometragem válido")
            
    @property
    def meses_da_ultima_revisao(self):
        return self.__meses_da_ultima_revisao
    
    @meses_da_ultima_revisao.setter
    def meses_da_ultima_revisao(self, new_val):
        if new_val > 0 and isinstance(new_val, int):
            self.__meses_da_ultima_revisao = new_val
        else:
            print("Insira um período em número de meses")
                      
    def __carro_quebra(self):
        if self.__meses_da_ultima_revisao >= 24:
            print('O carro apresentou um problema. Levar ao mecânico.')
        else:
            p = 24 - self.__meses_da_ultima_revisao
            print('Sua última revisão foi há {} meses. Faça outra revisão antes de atingir 24 meses.'.format(self.__meses_da_ultima_revisao))    
        
    def carro_andando(self):
        print('O carro está andando')
        self.__carro_quebra()
        
    def carro_para(self):
        print('O carro está parado')
        
my_car = Carro('ford', 'bronco', 2023, 100, 0)
# my_car.carro_andando()
my_car2 = Carro('fiat', 'uno', 2015, 150000, 26)
# my_car2.carro_andando()
# my_car2.__carro_quebra()

class Motorista(Carro):
    
    def __init__(self, marca, modelo, ano, kilometragem, meses_da_ultima_revisao, nome, cnh):
        self.__nome = nome
        self.__cnh = cnh
        super().__init__(marca, modelo, ano, kilometragem, meses_da_ultima_revisao)
           
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, new_val):
        self.__nome = new_val
 
    @property
    def cnh(self):
        return self.__cnh
    
    @cnh.setter
    def cnh(self, new_val):
        self.__cnh = new_val
        

motorista1 = Motorista('ford', 'bronco', 2023, 100, 0, 'Mafalda', '7563738')
motorista2 = Motorista('fiat', 'uno', 2015, 150000, 26, 'Josué', '5728270')
motorista1.carro_andando()
motorista2.carro_andando()

## Carro e motorista v.2
# objetivo: simplificar a quantidade de properties e setters dos atributos
# solucao: function que define a property e a retorna
# source: python cookbook p.382


from abc import ABC

def typed_property(name, expected_type):
        storage_name = '__' + name
        
        @property
        def prop(self):
            return getattr(self, storage_name)
        
        @prop.setter
        def prop(self, value):
            if not isinstance(value, expected_type):
                raise TypeError('{} must be a {}'.format(name, expected_type))
            setattr(self, storage_name, value)
        return prop


class Carro(ABC):
    
    marca = typed_property('marca', str)
    modelo = typed_property('modelo', str)
    ano = typed_property('ano', str)
    kilometragem = typed_property('kilometragem', int)
    meses_da_ultima_revisao = typed_property('meses_da_ultima_revisao', int)
    
    
    def __init__(self, marca, modelo, ano, kilometragem, meses_da_ultima_revisao):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.kilometragem = kilometragem
        self.meses_da_ultima_revisao = meses_da_ultima_revisao

    def __carro_quebra(self):
        if self.meses_da_ultima_revisao >= 24:
            print('O carro apresentou um problema. Levar ao mecânico.')
        else:
            p = 24 - self.meses_da_ultima_revisao
            print('Sua última revisão foi há {} meses. Faça outra revisão antes de atingir 24 meses.'.format(self.meses_da_ultima_revisao))    
        
    def carro_andando(self):
        print('O carro está andando')
        self.__carro_quebra()
        
    def carro_para(self):
        print('O carro está parado')


class Motorista(Carro):
    
    nome = typed_property('nome', str)
    cnh = typed_property('cnh', str)
            
    def __init__(self, marca, modelo, ano, kilometragem, meses_da_ultima_revisao, nome, cnh):
        self.nome = nome
        self.cnh = cnh
        super().__init__(marca, modelo, ano, kilometragem, meses_da_ultima_revisao)
           
           
fiesta = Carro('ford', 'fiesta', '2004', 180000, 23)
fiesta.ano 
fiesta.ano = '2003'
fiesta.carro_andando()
fiesta.carro_para()
dir(fiesta)
fiesta.marca # nao esta privado, pq?

motorista1 = Motorista('ford', 'bronco', '2023', 100, 0, 'Mafalda', '7563738')
motorista2 = Motorista('fiat', 'uno', '2015', 150000, 26, 'Josué', '5728270')
motorista1.carro_andando()
motorista2.carro_andando()