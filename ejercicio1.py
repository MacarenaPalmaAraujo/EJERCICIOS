def guardar_tabla_multiplicar():
    numero = int(input("Introduce un número entero entre 1 y 10: "))
    
    if 1 <= numero <= 10:
        nombre_fichero = f"tabla-{numero}.txt"
        
        with open(nombre_fichero, "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
                
        print(f"¡Hecho! La tabla del {numero} se ha guardado en el archivo '{nombre_fichero}'.")
    else:
        print("Error: Debes introducir un número estrictamente entre 1 y 10.")

guardar_tabla_multiplicar()