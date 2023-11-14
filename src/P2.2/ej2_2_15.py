def sumatorio_func(suma):
    n=int(input("Introduce un numero: "))
    while n!=0:
        if n>0:
            suma+=n
        n=int(input("Introduce un numero: ")) 
    return suma

def main():
    suma=0
    print(f"El resultado de la suma es: {sumatorio_func(suma)}")

if __name__ == "__main__":
    main()