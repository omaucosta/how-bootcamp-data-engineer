import datetime
import math

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento:datetime):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property # com esse decorator o método idade vira uma propriedade
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome}, tem {self.idade} anos"

mau = Pessoa(nome='Mau', sobrenome='Costa', data_de_nascimento=datetime.date(1995, 5, 6))

print(mau)
print(mau.nome)
print(mau.sobrenome)
print(mau.data_de_nascimento)
print(mau.idade)