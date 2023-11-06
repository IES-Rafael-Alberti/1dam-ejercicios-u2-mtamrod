def mayor_func(n, suma):
    for digito in n:
        suma+=int(digito)
    return print(suma)

def main():
    suma=0
    n=str(input("Introduce un numero: "))
    mayor_func(n, suma)

if __name__ == "__main__":
    main()