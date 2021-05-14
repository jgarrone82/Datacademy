import math
def convertidor():
    i=0
    while i==0:
        opcion=int(input("Por favor,ingre el numero de la opcion que quiera :"))       
        if opcion == 1:
            altura=float(input("Ingrese la altura del cilindro:"))
            radio=float(input("Ingrese el radio del cilindro:"))
            volumen=math.pi*(radio**2)*altura
            print("El volumen del cilindro es :", volumen)
        elif opcion == 2:
           lado=float(input("Ingrese un lado del cubo:"))
           volumen=lado ** 3
           print("El volumen del cubo es :", volumen)
        elif opcion == 3:
            radio=float(input("Ingrese el radio de la esfera:"))
            volumen=math.pi*(radio**3)*(4/3)
            print("El volumen de la esfera es :", volumen)
        elif opcion == 4:
            break
        else:
            print("ingresa una opcion valida")    
                
def main():
    print("""Selecione la figura la cual quiere obtener el volumen :

    1): cilindro 
    2): cubo
    3): Esfera
    4): Salir

    """)
    convertidor()

if  __name__=="__main__":
   main()