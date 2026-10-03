import urllib.request

def contar_palabras_url(url):
    try:
        with urllib.request.urlopen(url) as respuesta:
            contenido = respuesta.read().decode('utf-8')
            
            palabras = contenido.split()
            
            print(f"El fichero en la URL contiene un total de {len(palabras)} palabras.")
            
    except Exception as e:
        print(f"Ocurrió un error al intentar acceder a la URL: {e}")

url_ejemplo = "https://www.gutenberg.org/files/11/11-0.txt"
contar_palabras_url(url_ejemplo)