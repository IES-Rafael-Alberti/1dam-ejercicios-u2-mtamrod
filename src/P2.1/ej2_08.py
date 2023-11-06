def evaluacion(punt):
    if (punt<0.4) and (punt>=0):
        return "Puntuación inaceptable."
    
    elif (punt>=0.4) and (punt<0.6):
        return "Puntuación aceptable."
    
    elif (punt>0.6) and (punt<=1):
        return "Puntuación meritoria."
    
    else:
        return "Puntuación inválida introduzca una puntuación entre 0 y 1."

def main():
    punt=float(input("Introduzca su puntuación (0-1): "))

    print(evaluacion(punt))

if __name__ == "__main__":
   main()