class Cidades():
    def __init__(self,nome,regiao,pais,nivel):
        self.nome = nome
        self.regiao = regiao
        self.pais = pais
        self.nivel = nivel
    def evoluir(self,evolucao):
        self.nivel += evolucao
    def __str__(self):
        return "{} é nível {}".format(self.nome,self.nivel)
    def __repr__(self):
        return "\n---------------\n{} \nlevel {}\n---------------".format(self.nome,self.nivel)

cidade1 = Cidades('Astana','Akmola','Kazakhstan',0)

print(cidade1.nivel)
cidade1.evoluir(int(input('Quantos níveis: ')))

print(cidade1.nome,'agora é nível',cidade1.nivel)

print(type(cidade1.nome))

print(cidade1) #vai executar o def __str__

repr(cidade1)