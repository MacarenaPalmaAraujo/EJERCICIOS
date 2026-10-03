def mostrar_linea_tabla():
    # Pedimos los dos números al usuario
    n = int(input("Introduce el número n (tabla entre 1 y 10): "))
    m = int(input("Introduce el número m (línea entre 1 y 10): "))
    
    if 1 <= n <= 10 and 1 <= m <= 10:
        nombre_fichero = f"tabla-{n}.txt"
        
        try:
            with open(nombre_fichero, "r") as archivo:
                lineas = archivo.readlines()
                print(f"\nLínea {m} del fichero {nombre_fichero}:")
                print(lineas[m - 1].strip())
        except FileNotFoundError:
            print(f"El fichero {nombre_fichero} no existe. Ejecuta primero el Ejercicio 1 para ese número.")
    else:
        print("Error: Ambos números deben estar entre 1 y 10.")

mostrar_linea_tabla()