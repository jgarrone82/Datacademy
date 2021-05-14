menu = """
Te damos la bienvenida al conversor de monedas 💰😎

1 - Pesos colombianos 
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Euros

Elige tu moneda: 
"""
opcion = int(input(menu))

if opcion == 1:
  moneda = "pesos colombianos"
  valor_cambio = float(3750.4399)
elif opcion == 2:
  moneda = "pesos argentinos"
  valor_cambio = float(93.766347)
elif opcion == 3:
  moneda = "pesos mexicanos"
  valor_cambio = float(19.919911)
elif opcion == 4:
  moneda = "euros"
  valor_cambio = float(0.82201772)
else:
  print("Selecciona alguna opción del menu")

cantidad_monedas = round(float(input("Cuántos " + moneda + " tienes? ")), 2)

dolares = round(float(cantidad_monedas / valor_cambio), 2)

print("Tienes $" + str(dolares) + " dólares")