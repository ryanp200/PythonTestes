palavra = input("Digite uma palavra: ")
print('A palavra "'+palavra+'" contém '+str(len(palavra))+' letras')
for i in range(0,len(palavra)):
    print(palavra[i]+" é a "+str(i+1)+"ª letra")
