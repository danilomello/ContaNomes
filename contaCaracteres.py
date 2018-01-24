#Este código conta a quantidade de caracteres de um nome

def qntLetrasNome(nome):
    qntCaracteres = len(nome)
    print("Seu nome é " + nome + " e possui " + str(qntCaracteres) + " caracteres")

def mostraMaiorNome(listaDeNomes):
    maiorNome = ""
    qntCaracteres = 0
    for i in range(len(listaDeNomes)):
        if len(listaDeNomes[i]) > qntCaracteres:
            qntCaracteres = len(listaDeNomes[i])
            maiorNome = listaDeNomes[i]

    print("O maior nome é " + maiorNome + " e possui " + str(qntCaracteres) + " caracteres")
