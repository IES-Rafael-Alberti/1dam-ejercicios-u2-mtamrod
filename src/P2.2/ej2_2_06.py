def piramide(n):
    cad_piramide=""
    for n in range(1, n+1):
        cad_piramide+=("*")
        print(cad_piramide)
    return ""

def main():
    n=int(input("Introduzca un numero entero: "))
    
    piramide(n)

if __name__ == "__main__":
    main()