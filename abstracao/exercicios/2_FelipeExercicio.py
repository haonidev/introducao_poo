
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

    
class Motorista(GenericCar):
    
    def __init__(self):
        super().__init__(None, None, None)
        
    def ligar(self,carro):
        print("Ligou o carro")
        
    def acelerar(self,carro):
        print("Acelerou o carro")
    
    def abastecer(self,carro,litros):
        carro.combustivel = litros
        print("Acelerou o carro")


if __name__ == "__main__":
    
    piloto      = "Juca",
    modelo      = "Fiesta" 
    combustivel = 20

    carro = GenericCar(modelo, piloto, combustivel)
    
    print(carro.combustivel)
    
    carro.piloto = "Arruda"
    
    motorista = Motorista() 
    motorista.ligar(carro)
    motorista.acelerar(carro)
    
    motorista.abastecer(carro,10) 
    
    print(carro.combustivel)
    
    