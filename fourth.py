class Usuarios:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def login(self, senha_user):
        if senha_user == self.senha:
            print("Login com sucesso. "+self.nome+", bem-vindo")
        else:
            print("Senha incorreta")


usuario1 = Usuarios("Mike","abcd")
usuario2 = Usuarios("Tom","efgh")

senha_user = input("Senha: ")
usuario1.login(senha_user)
