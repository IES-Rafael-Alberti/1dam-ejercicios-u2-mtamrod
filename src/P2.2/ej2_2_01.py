def repetir(palabra):
    for i in range(10):
        print(palabra)
    return ""

    
    
def main():
    palabra=(input("Introduzca una palabra a repetir: "))
    
    print(repetir(palabra))

if __name__ == "__main__":
    main()