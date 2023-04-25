from abc import ABC, abstractmethod

class GenericPerson:    
    def __init__(self, nome, idade, sexo, endereco):
        self.nome     = nome 
        self.idade    = idade 
        self.sexo     = sexo 
        self.endereco = endereco
    
    @abstractmethod
    def andar(self,pessoa):
        print("Pessoa Andando")
    
    @abstractmethod
    def falar(self,pessoa):
        print("Pessoa Falando")

    @abstractmethod
    def comer(self,pessoa):
        print("Pessoa Falando")
    
class Funcionario(GenericPerson):
    
    def __init__(self):
        super().__init__(None, None, None, None)
    
    def andar(self,pessoa):
        print("Funcionario Anda")
        
    def falar(self,pessoa):
        print("Funcionario Falar")

class Cliente(GenericPerson):
    
    def __init__(self):
        super().__init__(None, None, None, None)
    
    def andar(self,pessoa):
        print("Cliente Anda")

    def falar(self,pessoa):
        print("Cliente Falar")

if __name__ == "__main__":
    
    nome     = "Jose",
    idade    = 20 
    sexo     = "masculino" 
    endereco = "Cuiaba"
    pessoa   = GenericPerson(nome, idade, sexo, endereco)
    
    funcionario = Funcionario() 
    
    funcionario.andar(pessoa)
    funcionario.falar(pessoa)
    

    cliente = Cliente() 
    
    cliente.andar(pessoa)
    cliente.falar(pessoa)