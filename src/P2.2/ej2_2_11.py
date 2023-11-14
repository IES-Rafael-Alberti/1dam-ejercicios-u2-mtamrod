def frase_func(frase):
    letra=""
    n_letra=str(frase.count(letra))
    letra=list(frase[::-1])

    for letra in letra:
        print(letra)


def main():
    frase=input("Introduzca una frase: ")
    
    frase_func(frase)

if __name__ == "__main__":
    main()