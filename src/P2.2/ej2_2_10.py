def primo_func(n):
    for x in range(n, 2, -1):
        primo=n%x
        if primo == 0:
            x-=1
            primo=n%x
            if primo == 0:
                return print("No es primo")
            #else:
            #    return print("Es primo")
        else:
            return print("Es primo")


        
        

def main():
    n=int(input("Introduzca un numero entero: "))
    
    primo_func(n)

if __name__ == "__main__":
    main()