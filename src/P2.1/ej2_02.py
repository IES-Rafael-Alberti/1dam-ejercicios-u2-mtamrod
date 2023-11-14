def contraseña(contraseña1):
    
    contraseña_guard="illojuan"
    
    contraseña1=contraseña1.lower()
    contraseña_guard=contraseña_guard.lower()
    
    if contraseña_guard==contraseña1:
        return "Correcta"
    
    elif contraseña_guard!=contraseña1:
        return "Incorrecta"
    
def main():
    contraseña1=input("Introduce una contraseña: ")
    print(contraseña(contraseña1))

if __name__ == "__main__":
   main()