import string

def verificarPalindromo(frase):
  pontuacoes = set(string.punctuation)
  
  frase = ''.join(letra for letra in frase if letra not in pontuacoes)
  frase = frase.replace(" ","").lower()
  print(frase)

  if frase == frase[::-1]:
    return True
  else:
    return False

def principal():
  frase = input("... ")
  if(verificarPalindromo(frase)):
    print(frase.lower().capitalize()+" é um palíndromo!!")
  else:
    print(frase.lower().capitalize()+" não é palíndromo!!!!!!!")

if __name__== "__main__":
  principal()
