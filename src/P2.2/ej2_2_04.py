def cuenta(n):
    cad_cuenta=""
    for n in range(n, -1, -1):
        cad_cuenta+=(f"{n},")
    cad_cuenta=cad_cuenta[:-1]
    return cad_cuenta

def main():
    n=int(input("Introduzca un numero entero positivo: "))
    
    print(cuenta(n))

if __name__ == "__main__":
    main()