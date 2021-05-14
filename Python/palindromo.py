def palindromo():
    text = input("Ingresa un texto: ").lower().replace(" ", "")
    text_pali = text[::-1]

    if text == text_pali:
        return True
    else:
        return False


def run():

    if palindromo():
        print("Si es un palindromo")
    else: 
        print("NO es un palindromo")

if __name__ == "__main__":
    run()