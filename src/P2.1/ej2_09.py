def cobro(edad):
    if (edad<0) or (edad>150):
        return "¡¡¡ERROR DE EDAD!!!"
    elif (edad>0) and (edad<4):
        return "0€"
    elif (edad>=4) and (edad<18):
        return "5€"
    elif (edad>=18):
        return "10€"
       
def main():
   edad=int(input("Introduzca su edad: "))

   print(f"El coste de la entrada es {cobro(edad)}")

if __name__ == "__main__":
   main()