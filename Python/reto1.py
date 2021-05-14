def get_area():
    base = float(input("Cuál es la base del triángulo?: "))
    hight = float(input("Cuál es la altura del triángulo?: "))
    return (base * hight) / 2

def get_sides():
    sides=list(map(float, input("Cuáles son los 3 lados?: ").split(',')))
    print(f"""
    El primer lado es: {sides[0]}
    El segundo lado es: {sides[1]}
    El tercer lado es: {sides[2]}
    """)
    confirmation = input("Los lados son correctos?: (Y/N)").upper()
    if confirmation == "Y":
        get_type_triangle(sides)
    else:
        get_sides()

def get_type_triangle(sides):
    if sides[0] == sides[1] and sides[1] == sides[2]:
        print("El triángulo es Equilátero")
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        print("El triángulo es Isósceles")
    else:
        print("El triángulo es Escaleno")

if __name__ == "__main__":
    print("Bienvenido al reto 1".center(50,"="))
    print(f"su área es: {get_area()} \n")
    get_sides()
