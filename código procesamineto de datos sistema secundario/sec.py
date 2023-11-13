# Abre el archivo de entrada en modo lectura y especifica la codificación utf-8
with open('xi_2a.txt', 'r', encoding='utf-8') as infile:
    # Abre o crea un archivo de salida en modo escritura y especifica la codificación utf-8
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        # Itera sobre cada línea en el archivo de entrada
        for line in infile:
            # Divide la línea por comas
            parts = line.split(',')

            # Extrae el hash y la marca de tiempo
            hash_id = parts[0].strip()
            timestamp = parts[1].strip()

            # Convierte la marca de tiempo a un objeto datetime y extrae solo la hora
            from datetime import datetime
            timestamp_dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
            hour_only = timestamp_dt.strftime("%H:%M:%S")

            # Encuentra la posición de los corchetes y extrae los nombres de las redes wifi
            start = line.find('[') + 1
            end = line.find(']', start)
            wifi_names = line[start:end].strip()

            # Busca los nombres de las redes wifi deseadas en la lista de nombres de wifi
            if 'Familia-perdomo-patino-5Gz' in wifi_names or 'MI 9' in wifi_names:
                # Escribe solo la hora y el nombre de la red wifi en el archivo de salida
                outfile.write(f'{hour_only}, Familia-perdomo-patino-5Gz\n' if 'Familia-perdomo-patino-5Gz' in wifi_names else f'{hour_only}, MI 9\n')

# Define los nombres originales y sus reemplazos
replacements = {
    "MI 9": "lagos",
    "Familia-perdomo-patino-5Gz": "127"
}

# Abre el archivo de entrada en modo lectura y especifica la codificación utf-8
with open('output.txt', 'r', encoding='utf-8') as infile:
    # Abre o crea un archivo de salida en modo escritura y especifica la codificación utf-8
    with open('output2.txt', 'w', encoding='utf-8') as outfile:
        # Itera sobre cada línea en el archivo de entrada
        for line in infile:
            # Realiza los reemplazos en la línea
            for original, replacement in replacements.items():
                line = line.replace(original, replacement)
            
            # Escribe la línea modificada en el archivo de salida
            outfile.write(line)





import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Función para leer el archivo y procesar los datos
def leer_datos(archivo):
    datos = []
    with open(archivo + '.txt', 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 2:
                tiempo = datetime.strptime(partes[0].strip(), '%H:%M:%S')
                ubicacion = partes[1].strip()
                datos.append((tiempo, ubicacion))
    return datos

# Leer datos del archivo
datos = leer_datos('output2')

# Preparar los datos para graficar
tiempos_lagos = [t for t, u in datos if u == 'lagos']
tiempos_127 = [t for t, u in datos if u == '127']

# Ajustar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Graficar los datos en color verde
plt.plot(tiempos_lagos, [0]*len(tiempos_lagos), 'go', label='Lagos')
plt.plot(tiempos_127, [1]*len(tiempos_127), 'go', label='127')

# Formatear el eje de tiempo
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator())
plt.xticks(rotation=45, fontsize=12)  # Aumentar tamaño de las etiquetas del eje X
plt.yticks([0, 1], ['Lagos', '127'], fontsize=12)  # Aumentar tamaño de las etiquetas del eje Y

# Aumentar tamaño de los títulos y etiquetas
plt.title('Movimiento entre Lagos y 127', fontsize=14)
plt.xlabel('Tiempo', fontsize=12)
plt.ylabel('Ubicación', fontsize=12)

plt.legend(fontsize=12)
plt.tight_layout()  # Asegura que todo encaje correctamente
plt.show()










