def inversion(amount, interest, años):
    list_años=str(f"En el año {años}: {amount}€\n")
    print(list_años)
    
    for años in range(1, años+1):
        amount *= 1+(interest/100)
        list_años=(f"En el año {años}: {amount}€\n")
        print(list_años)
    return

def main():
    amount=float(input("Introduzca una cantidad a invertir: "))
    interest=float(input("Introduzca el porcentaje de interés anual: "))
    años=int(input("Indique los años que va a invertir ese dinero: "))
    
    print(inversion(amount, interest, años))

if __name__ == "__main__":
    main()