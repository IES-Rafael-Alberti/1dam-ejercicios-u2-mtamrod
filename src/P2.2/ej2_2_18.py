def sumatorio(n):
    suma2=0
    while n!="-1":
        suma=0
        for digito in n:
            suma+=int(digito)

        suma2+=int(suma)
        n=str(input("Introduce un numero: ")) 
    return suma2
    
def main():
    n=str(input("Introduce un numero: ")) 
    
    print(f"La suma es: {sumatorio(n)}")

if __name__ == "__main__":
    main()