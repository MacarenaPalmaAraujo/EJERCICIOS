import csv

def cargar_cotizaciones(nombre_fichero):
    columnas = ["Nombre", "Final", "Máximo", "Mínimo", "Volumen", "Efectivo"]
    diccionario = {col: [] for col in columnas}
    
    with open(nombre_fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        
        for linea in lineas[1:]:
            partes = linea.split()
            if len(partes) >= 6:
                nombre = " ".join(partes[:-5])
                valores = partes[-5:]
                
                diccionario["Nombre"].append(nombre)
                
                for i, col in enumerate(columnas[1:]):
                    num_limpio = valores[i].replace(".", "").replace(",", ".")
                    diccionario[col].append(float(num_limpio))
                    
    return diccionario


def generar_resumen_csv(diccionario, archivo_salida="resumen_cotizacion.csv"):
    resumen = {}
    
    for col, valores in diccionario.items():
        if col == "Nombre":
            continue
        
        resumen[col] = {
            "Mínimo": min(valores),
            "Máximo": max(valores),
            "Media": sum(valores) / len(valores)
        }
        
    with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Columna", "Mínimo", "Máximo", "Media"])
        
        for col, stats in resumen.items():
            escritor.writerow([col, stats["Mínimo"], stats["Máximo"], round(stats["Media"], 2)])
            
    print(f"¡Listo! Se ha creado el archivo '{archivo_salida}' con el resumen.")


datos = cargar_cotizaciones("cotizacion.csv")
generar_resumen_csv(datos)