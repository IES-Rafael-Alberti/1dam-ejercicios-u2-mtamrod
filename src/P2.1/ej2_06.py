def grupo(sexo, nombre):
    nombre = nombre.upper()
    sexo = sexo.upper()
    if (sexo=="F" and nombre<"M") or (sexo=="M" and nombre>"N"):
        return "Grupo A"
    else:
        return "Grupo B"
        
    
def main():
    sexo=input("Indique su sexo (F / M): ")
    nombre=input("Introduzca su nombre: ")
    
    print(grupo(sexo, nombre))

if __name__ == "__main__":
   main()