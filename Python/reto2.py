def eleccion():
    menu = """
    1 - Piedra
    2 - Papel
    3 - Tijeras

    Elige una opción: """

    opcion = int(input(menu))

    if opcion == 1:
        return "Piedra"
    elif opcion == 2:
        return "Papel"
    elif opcion == 3:
        return "Tijeras"
    else:
        print('Ingresa una opción correcta por favor')

    

def resultado(jugador1, jugador2):
    if jugador1 == jugador2:
        return "Ha salido un empate"
    elif jugador1 == "Piedra":
        if jugador2 == "Tijeras":
            return "Gana el jugador 1"
        else:
            return "Gana el jugador 2"
    elif jugador1 == "Papel":
        if jugador2 == "Piedra":
            return "Gana el jugador 1"
        else:
            return "Gana el jugador 2"
    elif jugador1 == "Tijeras":
        if jugador2 == "Papel":
            return "Gana el jugador 1"
        else:
            return "Gana el jugador 2"                

def ppt():
    print("Que elige el jugador 1?:")    
    jugador1 = eleccion()
    print("\nQue elige el jugador 2?:")
    jugador2 = eleccion()    
    
    print("\n" + resultado(jugador1, jugador2))
    

if __name__ == "__main__":
    print("Bienvenido al reto 2".center(50,"="))    
    print("Jugaremos piedra 💎 papel 📋 o tijeras ✂  ")
    ppt()
