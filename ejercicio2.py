def leer_tabla_multiplicar():
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    
    if 1 <= numero <= 10:
        nombre_fichero = f"tabla-{numero}.txt"
        
        try:
            with open(nombre_fichero, "r") as archivo:
                contenido = archivo.read()
                print(f"\n--- Contenido de {nombre_fichero} ---")
                print(contenido)
        except FileNotFoundError:
            print(f"El fichero {nombre_fichero} no existe. Ejecuta primero el Ejercicio 1 para crearlo.")
    else:
        print("Error: Debes introducir un número estrictamente entre 1 y 10.")

leer_tabla_multiplicar()