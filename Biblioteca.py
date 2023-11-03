class Pessoa:
    def __init__ (self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer (self):
        if self.comendo == True:
            print(f"{self.nome} já está comendo!")

        elif self.falando == True:
            print(f"{self.nome} não pode comer porque está falando!")

        elif self.dormindo == True:
            print(f"{self.nome} não pode comer porque está dormindo!")

        else:
            print(f"{self.nome} está comendo!")
            self.comendo = True


    def falar (self):
        if self.falando == True:
            print(f"{self.nome} já está falando!")

        elif self.comendo == True:
            print(f"{self.nome} não pode falar porque está comendo!")

        elif self.dormindo == True:
            print(f"{self.nome} não pode falar porque está dormindo!")

        else:
            print(f"{self.nome} está falando!")
            self.falando = True


    def dormir (self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo!")

        elif self.falando == True:
            print(f"{self.nome} não pode dormir porque está falando!")

        elif self.comendo == True:
            print(f"{self.nome} não pode dormir porque está comendo!")

        else:
            print(f"{self.nome} bobou!")

            self.dormindo = True

    def apresenta (self):
        print(f" Meu nome é {self.nome}, estou pesando {self.peso}Kg e tenho {self.idade} anos!")

    def pararDeComer (self):
        self.comendo = False
        print(f"{self.nome} Parou de Comer!")


    def acordar (self):
        self.dormindo = False
        print(f"{self.nome}Acordou!")


    def pararDeFalar (self):
        self.falando = False
        print(f"{self.nome} Parou de falar!")


class Banco:
    def __init__(self, numero, saldo, nome, tipo, status, limite):
        self.numero = numero
        self.saldo = 0.00
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = limite

    def ativarconta(self):
        if self.status == True:
            return("A conta está Ativa")

        elif self.status == False:
            return("A conta está Inativa")

    def depositar(self):
        if self.numero == True:
           return("Deposito realizado!")

        elif self.numero == False:
            return("Houve uma falha em seu Deposito.")

    def sacar(self):
        if self.saldo == True:
            return("Saque realizado com Sucesso! o seu saldo é: ")

        elif self.saldo == False:
            return("Houve uma falha em seu Saque.")


    def verificarsaldo(self):
        if self.saldo == True:
            return("Seu saldo é: ")

        elif self.saldo == False:
            return("Houve uma falha em sua verificação.")


class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f" O {self.nome} foi comer...")


class Gato(Animal):
    def __init__ (self, nome, cor):
        super().__init__(nome, cor)

    def emitir(self):
        print(F" O {self.nome} está miando... MIAUUUUU")

class Cachorro(Animal):
    def __init__ (self, nome, cor):
        super().__init__(nome, cor)

    def emitir(self):
        print(F" O {self.nome} está Latindo... AUAUAUh")

class Coelho(Animal):
    def __init__ (self, nome, cor):
        super().__init__(nome, cor)

    def emitir(self):
        print(F" O {self.nome} está ronronando... pishpishpish")

class Vaca(Animal):
    def __init__ (self, nome, cor):
        super().__init__(nome, cor)

    def emitir(self):
        print(F" O {self.nome} está muge")
