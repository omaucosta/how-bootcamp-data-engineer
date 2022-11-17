import datetime
import math
from typing import List

class Pessoa:
    def __init__(
        self, 
        nome: str, 
        sobrenome: str, 
        data_de_nascimento:datetime) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property # com esse decorator o método idade vira uma propriedade
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome}, tem {self.idade} anos"


class Curriculo:
    def __init__(self, pessoa: Pessoa, experiencias: List[str]):
        self.pessoa = pessoa
        self.experiencias = experiencias

    @property
    def quantidade_experiencia(self) -> int:
        return len(self.experiencias)

    @property
    def cargo_atual(self) -> str:
        return self.experiencias[-1]

    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self) -> str:
        return f'{self.pessoa.nome} tem {self.pessoa.idade} e teve {self.quantidade_experiencia} na sua carreira, sendo elas {self.experiencias}, atualmente trabalha como {self.cargo_atual}'


mau = Pessoa(nome='Mau', sobrenome='Costa', data_de_nascimento=datetime.date(1995, 5, 6))
print(mau)

curriculo_mau = Curriculo(
    pessoa=mau, experiencias= ['AEVO - Customer Sucess Intern', 'GUPY - Data Analytic Intern', 'GUPY - Integration Engineer'])

print(curriculo_mau)

curriculo_mau.adiciona_experiencia('GUPY - Data Engineer')

class Vivente:
    def __init__(self, nome:str, data_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento

    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)
