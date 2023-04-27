




class Pessoa():

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__cabelo = "preto"

    def dizer_o_proprio_nome(self):
        self.__usar_dinheiro()
        print(f"Meu nome é {self.__nome}")

    def __usar_dinheiro(self):
        pass


class Programador(Pessoa):

    def __init__(self, nome: str, linguagem: str) -> None:
        super().__init__(nome)
        self.__linguagem = linguagem

    def programar(self):
        print(f"Estou programando em {self.__linguagem}")


if __name__ == "__main__":

    pessoa = Pessoa("Felipe")
    print(pessoa.dizer_o_proprio_nome())
    # pessoa.__usar_dinheiro()


    # haoni = Programador("Haoni", "Python")
    # haoni.__cabelo = "verde"
    # print(haoni.__cabelo)

    # print(haoni.__linguagem)
