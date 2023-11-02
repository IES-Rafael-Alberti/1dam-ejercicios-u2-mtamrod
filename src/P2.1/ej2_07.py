def rentafinal(renta):
    if renta<=10000:
        return "5%"
    elif (renta>10000) and (renta<=20000):
        return "15%"
    elif (renta>20000) and (renta<=35000):
        return "20"
    elif (renta>35000) and (renta<=60000):
        return "30%"
    else:
        return "45%"
        

def main():
    renta=int(input("Introduzca su renta anual: "))
    print(f"El tipo impositivio para {renta}€ es del {rentafinal(renta)}")

if __name__ == "__main__":
   main()