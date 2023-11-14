def pizza_tipo(tipo):
    tipo.lower()

    if tipo=="vegetariana":
        return "Igredientes vegetarianos: Pimiento y tofu"
    elif tipo=="no vegetariana":
        return "Igredientes no vegetarianos: Peperoni, Jamón y Salmón"
    else:
        return "No existe ese tipo de pizza."
    
def pizza_ing(ingrediente):

    if ingrediente=="peperoni":
        return "Su pizza es de tomate, mozzarella y peperoni"
    elif ingrediente=="jamon":
        return "Su pizza es de tomate, mozzarella y jamon"
    elif ingrediente=="salmon":
        return "Su pizza es de tomate, mozzarella y salmon"

def pizzaveg_ing(ingrediente):

    if ingrediente=="tofu":
        return "Su pizza es de tomate, mozzarella y tofu"
    elif ingrediente=="pimiento":
        return "Su pizza es de tomate, mozzarella y pimiento"

def main ():
    tipo=input("Introduzca el tipo de pizza que quiere (vegetariana/no vegetariana): ")
    print(pizza_tipo(tipo))

    ingrediente=input("Indique el ingrediente deseado (SOLO 1): ")
    ingrediente.lower()
    if tipo=="vegetariana":
        print(pizzaveg_ing(ingrediente))
    elif tipo=="no vegetariana":
        print(pizza_ing(ingrediente))
   
if __name__ == "__main__":
   main()