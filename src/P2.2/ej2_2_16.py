def mayor_func():
    n=int(input("Introduce un numero: "))
    mayor=n
    while n!=0:
        if n>mayor and n!=0:
            mayor=n
        n=int(input("Introduce un numero: ")) 
    return mayor

def main():
    print(f"El mayor es: {mayor_func()}")

if __name__ == "__main__":
    main()