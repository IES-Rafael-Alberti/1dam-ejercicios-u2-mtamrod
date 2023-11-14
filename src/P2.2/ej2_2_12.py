def frase_func(frase, letra):
    frase=frase.lower()
    letra=letra.lower()
    n_letra=frase.count(letra)
    return n_letra

def main():
    frase=input("Introduzca una frase sin tildes: ")
    letra=input("Introduzca una letra: ")
    
    print(f"La frase '{frase}' tiene {frase_func(frase, letra)} letras {letra}")

if __name__ == "__main__":
    main()