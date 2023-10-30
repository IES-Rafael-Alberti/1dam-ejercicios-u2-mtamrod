def division(n1, n2):
    if n2!=0:
        division=n1/n2
        return division
    else:
        return "erróneo"
    

def main():
    n1=float(input("Introduce un número: "))
    n2=float(input("Introduce un número: "))
    print(f"El resultado de la división es {division(n1, n2)} .")

if __name__ == "__main__":
   main()