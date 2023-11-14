def años(edad):
    for edad in range(1, edad+1):
        print(edad)
    return ""

def main():
    edad=int(input("Introduzca su edad: "))
    
    años(edad)

if __name__ == "__main__":
    main()