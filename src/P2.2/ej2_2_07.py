def tablas(n):
    cad_mult=""
    for i in range(0, 11):
        result=n*i
        print(f"{n}x{i}={result}")
    return ""

def main():
    n=int(input("Introduzca un numero entero positivo: "))
    
    print(tablas(n))

if __name__ == "__main__":
    main()