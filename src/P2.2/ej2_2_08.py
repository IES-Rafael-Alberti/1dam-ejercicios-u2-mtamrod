def piramide(n):
    cad_piramide=""
    for n in range(1, n+1):
        if n%2!=0:
            cad_piramide+=str(f"{n} ")
            print(cad_piramide[::-1])
        
    return ""

def main():
    n=int(input("Introduzca un numero entero: "))
    
    piramide(n)

if __name__ == "__main__":
    main()