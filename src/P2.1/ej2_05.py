def tributar(edad, ingresos):
    if edad<=16 or ingresos<100:
        return "No tributa."
    else:
        return "Si tributa."

def main():
    edad=int(input("Introduce tu edad: "))
    ingresos=float(input("Introduce tus ingresos mensuales: "))
    print(tributar(edad, ingresos))

if __name__ == "__main__":
   main()