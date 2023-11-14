def impar(n):
    cad_impar=""
    for n in range(1, n+1):
        if n%2!=0:
            cad_impar+=str(f"{n},")
    cad_impar =cad_impar[:-1]
    return cad_impar

def main():
    n=int(input("Introduzca un numero entero positivo: "))
    
    print(impar(n))

if __name__ == "__main__":
    main()