frutas = ['maçã','banana','limão','laranja']
frutas = [fr.capitalize() for fr in frutas]
print(frutas)

frutas.pop(0)

print(frutas)

cidades = {'Astana','Almaty','Seoul','Incheon','Busan','Moscow'}
cidades2 = {'Almaty','Astana','Busan','Moscow','Seoul','Incheon'}

def verificarIgualdade():
    if cidades == cidades2:
        return True
    else:
        return False

def main():
    if verificarIgualdade():
        print("Igual")
    else:
        print("Falso")

main()