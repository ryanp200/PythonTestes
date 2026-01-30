class Continente:
    def __init__(self, nome_continente):
        self.continente = nome_continente
    def __str__(self):
        return self.continente
    
class Pais:
    def __init__(self,nome_pais,nome_continente):
        self.nome = nome_pais
        self.continente = nome_continente
    def __str__(self):
        return f"\nPaís: {self.nome}\nContinente: {self.continente}\n"

asia = Continente("Ásia")
america = Continente("América")

paises = {
    "coreia_do_sul": Pais("Coreia do Sul",asia),
    "china": Pais("China",asia),
    "brasil": Pais("Brasil",america)
}

pesquisa = input("Pesquisa: ")
pesquisa = pesquisa.lower().replace(' ','_')
if pesquisa in paises:
    print(paises[pesquisa])
else:
    print("País não encontrado")