def contraseña(intento, cad_contraseña):
    if cad_contraseña!=intento:
        print("¡¡¡Contraseña incorrecta!!!")
        main()
    else:
        print("¡¡¡Contraseña correcta!!!")

def main():
    intento=input("Introduzca la contraseña: ")
    
    cad_contraseña="hola1234"
    
    contraseña(intento, cad_contraseña)

if __name__ == "__main__":
    main()