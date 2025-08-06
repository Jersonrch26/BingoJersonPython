import random
# Función para pedir un número del 1 al 100
def pedir_numero():
    entrada = input("Digite un número del 1 al 100 o 's' para salir: ")
    if entrada != "s":
        entradaint = int(entrada)
        if 1 <= entradaint <= 100:
            return entradaint
        else:
            print("¡Número fuera de rango!")
            return None
    else:
        print("Saliendo del programa...")
        return "s"

# Función para llenar el cartón del bingo
def llenar_carton():
    carton = []
    print("\n Llenar cartón (10 números únicos entre 1 y 100):")
    while len(carton) < 10:
        numero = pedir_numero()
        if numero == "s":
            return []
        elif numero is not None:
            if numero not in carton:
                carton.append(numero)
                print(f"Número añadido. Cartón actual: {carton}")
            else:
                print(" Ese número ya está en el cartón.")
    print("✅ Cartón lleno:", carton)
    return carton

# Función para reiniciar el juego
def reiniciar():
    print("\n Reiniciando partida...\n")
    return [], [], 0

# Función para realizar el sorteo de numero aleatorio
def sorteo(carton, numeros_sorteados, aciertos):
    if len(carton) < 10:
        print("Debe llenar el cartón antes de jugar.")
        return numeros_sorteados, aciertos

    numero = random.randint(1, 100)
    while numero in numeros_sorteados:
        numero = random.randint(1, 100)

    print(f" Número sorteado: {numero}")
    numeros_sorteados.append(numero)

    if numero in carton:
        aciertos += 1
        print(f" ¡Acierto! Total aciertos: {aciertos}/10")
    else:
        print(" No hay acierto.")

    if aciertos == 10:
        print("\n ¡Felicidades! Has completado el bingo con éxito.\n")

    return numeros_sorteados, aciertos

carton = []
numeros_sorteados = []
aciertos = 0

while True:
    print("\n🧾 MENÚ PRINCIPAL:")
    print("1. Llenar cartón")
    print("2. Realizar sorteo")
    print("3. Reiniciar partida")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        carton = llenar_carton()
    elif opcion == "2":
        numeros_sorteados, aciertos = sorteo(carton, numeros_sorteados, aciertos)
    elif opcion == "3":
        carton, numeros_sorteados, aciertos = reiniciar()
    elif opcion == "4":
        print(" Gracias por jugar. ¡Hasta luego!")
        break
    else:
        print(" Opción inválida.")

