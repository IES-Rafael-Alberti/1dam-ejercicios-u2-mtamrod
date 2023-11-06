def es_primo(n):
    if n<=1 and n>=-1:
        return print("No es primo")
    
    for i in range(2, n):
        primo=n%i

        if primo==0:
            return print("No es primo")
        else:
            return print("Es primo")      

def main():
    n=int(input("Introduzca un numero entero: "))
    
    es_primo(n)

if __name__ == "__main__":
    main()