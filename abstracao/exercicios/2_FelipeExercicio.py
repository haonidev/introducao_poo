
#3 - Crie uma classe que saiba dirigir um carro.

class GenericCar:    
    def __init__(self, modelo, piloto, combustivel):
        self.__modelo      = modelo
        self.__piloto      = piloto
        self.__combustivel = combustivel
    
    @property
    def modelo(self):
        return self.__modelo

    @property
    def piloto(self):
        return self.__piloto

    @property
    def combustivel(self):
        return self.__combustivel

    @combustivel.setter
    def combustivel(self,value):
        self.__combustivel = value
        return self.__combustivel
    
class DoggeRam(GenericCar):

    def __init__(self, modelo, piloto, combustivel):
        super().__init__(modelo, piloto, combustivel)
        self.carroceria = 250

    @property
    def combustivel(self):
        return self.__combustivel

    @combustivel.setter
    def combustivel(self,value):
        self.__combustivel = value
        return self.__combustivel

    def ligar(self):
        print("Ligou o carro")
        
    def acelerar(self):
        print("Acelerou o carro")
    
    def abastecer(self,litros):
        self.combustivel = litros
        print("Acelerou o carro")

    
class Motorista(GenericCar):
    


    def __init__(self):
        super().__init__(None, None, None)
        self.__combustivel = 0
        self.carteira = "carteira"
        
    def ligar(self,carro):
        print("Ligou o carro")
        
    def acelerar(self,carro):
        print("Acelerou o carro")
    
    def abastecer(self,carro,litros):
        carro.combustivel = litros
        print("Acelerou o carro")

    def pegar_carteira(self) -> str:
        return self.carteira


if __name__ == "__main__":
    
    piloto      = "Juca",
    modelo      = "Fiesta" 
    combustivel = 20

    carro = GenericCar(modelo, piloto, combustivel)
    carro.modelo = "Fusca"
    carro.combustivel += 10
    
    print(carro.combustivel)
    
    carro.piloto = "Arruda"
    
    motorista = Motorista() 
    motorista.ligar(carro)
    motorista.acelerar(carro)
    motorista.pegar_carteira()
    
    motorista.abastecer(carro,10) 
    
    print(carro.combustivel)
    
    