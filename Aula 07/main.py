class Pessoa:
    especie = "humano"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudar(self):
        print(f'Olá {self.nome}, voce tem {self.idade} anos')

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    @classmethod
    def descricao(cls):
        print(f"Teste de descricao {cls.especie}")


pessoa = Pessoa('Leo', '30')
pessoa.setNome('joao')
pessoa.saudar()
print(pessoa.especie)

Pessoa.descricao()
