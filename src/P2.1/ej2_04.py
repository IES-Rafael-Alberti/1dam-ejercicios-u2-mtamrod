def parimpar(numero):
    if numero%2==0:
        return "Par"
    else:
        return "Impar"
    
def main():
    numero=int(input("Introduce un número: "))
    print(parimpar(numero))
    
    

if __name__ == "__main__":
   main()