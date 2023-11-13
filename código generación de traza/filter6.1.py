import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Función para leer el archivo y procesar los datos
def leer_datos(archivo):
    datos = {}
    with open(archivo + '.txt', 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 2:
                tiempo = datetime.strptime(partes[0], '%H:%M:%S')
                hash_ = partes[1]
                if hash_ not in datos:
                    datos[hash_] = []
                datos[hash_].append(tiempo)
    return datos

# Definir el hash del dispositivo directamente en el código
#hash_dispositivo = "39f550c7f92cf87c097c4acf98d287dc9a114edf8c3b1e7ebb928d448fbb5286" #xiaomi mi9lte
#hash_dispositivo = "e5dca78cb46fbb446470922c1f5782a413fa9c97a88d2ba1cb472a4d8d44913d" #samsung s22
hash_dispositivo = "95df0edc8d88234e4bbe0812e75c2aed5d4bcb436b21f6bc99f7450fb3df858a" #samsung s6

# Leer datos de los dos archivos
datos_lagos = leer_datos('lagos')
datos_127 = leer_datos('127')

# Verificar si el hash está en ambos conjuntos de datos
if hash_dispositivo in datos_lagos and hash_dispositivo in datos_127:
    # Preparar los datos para graficar
    tiempos_lagos = datos_lagos[hash_dispositivo]
    tiempos_127 = datos_127[hash_dispositivo]
    
    # Ajustar el tamaño del gráfico
    plt.figure(figsize=(10, 6))
    
    # Graficar los datos
    plt.plot(tiempos_lagos, [0]*len(tiempos_lagos), 'ro', label='Lagos')
    plt.plot(tiempos_127, [1]*len(tiempos_127), 'bo', label='127')
    
    # Formatear el eje de tiempo
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator())
    plt.xticks(rotation=45, fontsize=12)  # Aumentar tamaño de las etiquetas del eje X
    plt.yticks([0, 1], ['Lagos', '127'], fontsize=12)  # Aumentar tamaño de las etiquetas del eje Y
    
    # Aumentar tamaño de los títulos y etiquetas
    plt.title('Movimiento de Dispositivo entre Lagos y 127', fontsize=14)
    plt.xlabel('Tiempo', fontsize=12)
    plt.ylabel('Ubicación', fontsize=12)
    
    plt.legend(fontsize=12)
    plt.tight_layout()  # Asegura que todo encaje correctamente
    plt.show()

else:
    print("Hash no encontrado en los archivos.")

