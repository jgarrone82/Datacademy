def conversor():
    MILLA = 1.609344

    menu = """
    Conversor de distancias 

    1 - Kilómetros a Millas
    2 - Millas a Kilómetros
    
    Elige tu opción: 
    """
    opcion = int(input(menu))

    if opcion == 1:
        kilometros = float(input("ingresa la cantidad de kilómetros: "))
        resultado = round(kilometros / MILLA, 2)
        print(f"{kilometros} Km son {resultado}  millas")
    elif opcion == 2:
        millas = float(input("ingresa la cantidad de millas: "))
        resultado = round(millas * MILLA, 2)
        print(f"{millas} millas son {resultado}  Km")
    else:
        print("Selecciona alguna opción del menu")

if __name__ == "__main__":
    print("Bienvenido al reto 3".center(50,"="))
    conversor()
    