import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Función para leer el archivo y procesar los datos del primer código
def leer_datos_v1(archivo):
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

# Función para leer el archivo y procesar los datos del segundo y tercer código
def leer_datos_v2(archivo):
    datos = []
    with open(archivo + '.txt', 'r') as f:
        for linea in f:
            partes = linea.strip().split(',')
            if len(partes) == 2:
                tiempo = datetime.strptime(partes[0].strip(), '%H:%M:%S')
                ubicacion = partes[1].strip()
                datos.append((tiempo, ubicacion))
    return datos

# Definir el hash del dispositivo directamente en el código
hash_dispositivo = "95df0edc8d88234e4bbe0812e75c2aed5d4bcb436b21f6bc99f7450fb3df858a"

# Leer datos de los dos archivos para el primer código
datos_lagos_v1 = leer_datos_v1('lagos_2b')
datos_127_v1 = leer_datos_v1('127_2b')

# Leer datos del archivo para el segundo código
datos_v2 = leer_datos_v2('xi9')

# Leer datos del archivo para el tercer código
datos_teo = leer_datos_v2('teo_2b')

# Ajustar el tamaño del gráfico
plt.figure(figsize=(16, 12))

# Función para graficar líneas entre los puntos
# Modifica la función para aceptar un argumento de grosor de línea
def graficar_lineas(tiempos_lagos, tiempos_127, color, label, marker_style='o', linewidth=2):
    tiempos = sorted(tiempos_lagos + tiempos_127)
    y = [0 if tiempo in tiempos_lagos else 1 for tiempo in tiempos]
    plt.plot(tiempos, y, color=color, label=label, marker=marker_style, linewidth=linewidth)


# Graficar los datos del primer código si el hash_dispositivo está en ambos conjuntos de datos
if hash_dispositivo in datos_lagos_v1 and hash_dispositivo in datos_127_v1:
    tiempos_lagos_v1 = datos_lagos_v1[hash_dispositivo]
    tiempos_127_v1 = datos_127_v1[hash_dispositivo]
    graficar_lineas(tiempos_lagos_v1, tiempos_127_v1, 'r', 'Sistema Principal')

# Graficar los datos del segundo código
tiempos_lagos_v2 = [t for t, u in datos_v2 if u == 'lagos']
tiempos_127_v2 = [t for t, u in datos_v2 if u == '127']
graficar_lineas(tiempos_lagos_v2, tiempos_127_v2, 'g', 'Sistema Complementario')

# Graficar los datos del tercer código sin marcar los puntos específicos (linea continua)
tiempos_lagos_teo = [t for t, u in datos_teo if u == 'lagos']
tiempos_127_teo = [t for t, u in datos_teo if u == '127']
graficar_lineas(tiempos_lagos_teo, tiempos_127_teo, 'b', 'Traza Teórica', marker_style=None)

# Formatear el eje de tiempo
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator())
plt.xticks(rotation=45, fontsize=12)
plt.yticks([0, 1], ['Lagos', '127'], fontsize=12)

# Aumentar tamaño de los títulos y etiquetas
plt.title('Comparación de Movimientos', fontsize=16)
plt.xlabel('Tiempo', fontsize=14)
plt.ylabel('Ubicación', fontsize=14)


plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()
plt.show()

#############################################################
def tiempo_total(datos):
    """Calcula el tiempo total desde la primera captura hasta la última."""
    return datos[-1][0] - datos[0][0]

# Estos tiempos son los que el usuario puede modificar según lo necesite.
tiempo_teorico_lagos = timedelta(minutes=11)  # Ejemplo: 17 minutos para lagos. Modificar según necesidad.
tiempo_teorico_127 = timedelta(minutes=11)  # Ejemplo: 18 minutos para 127. Modificar según necesidad.

# Cálculo del tiempo total teórico
tiempo_total_teorico = tiempo_teorico_lagos + tiempo_teorico_127 + timedelta(minutes=6)

# Tiempos totales
tiempo_total_principal = tiempo_total([(time, loc) for time, loc in zip(tiempos_lagos_v1 + tiempos_127_v1, ['lagos'] * len(tiempos_lagos_v1) + ['127'] * len(tiempos_127_v1))])
tiempo_total_complementario = tiempo_total([(time, loc) for time, loc in zip(tiempos_lagos_v2 + tiempos_127_v2, ['lagos'] * len(tiempos_lagos_v2) + ['127'] * len(tiempos_127_v2))])

# Calcular tiempo en cada estación para cada sistema
tiempo_principal_lagos = tiempo_total_principal - tiempo_teorico_127
tiempo_principal_127 = tiempo_total_principal - tiempo_teorico_lagos

tiempo_complementario_lagos = tiempo_total_complementario - tiempo_teorico_127
tiempo_complementario_127 = tiempo_total_complementario - tiempo_teorico_lagos

# Restar 4 minutos a las sumas ponderadas
ajuste = timedelta(minutes=6)
tiempo_principal_total = tiempo_principal_lagos + tiempo_principal_127 - ajuste
tiempo_complementario_total = tiempo_complementario_lagos + tiempo_complementario_127 - ajuste

# Calcular precisión
def calcular_precision(teorico, practico):
    return (practico.total_seconds() / teorico.total_seconds()) * 100

precision_principal = calcular_precision(tiempo_total_teorico, tiempo_principal_total)
precision_complementario = calcular_precision(tiempo_total_teorico, tiempo_complementario_total)

print("Porcentaje de precisión (Sistema Principal):", precision_principal)
print("Porcentaje de precisión (Sistema Complementario):", precision_complementario)

########################################################

## 1. Unir la información del sistema principal y el sistema complementario
tiempos_lagos_unidos = tiempos_lagos_v1 + tiempos_lagos_v2
tiempos_127_unidos = tiempos_127_v1 + tiempos_127_v2

# Ordenar por tiempo
tiempos_lagos_unidos.sort()
tiempos_127_unidos.sort()

# 2. Calcular la precisión de la gráfica unida
tiempo_total_unido = tiempo_total([(time, loc) for time, loc in zip(tiempos_lagos_unidos + tiempos_127_unidos, ['lagos'] * len(tiempos_lagos_unidos) + ['127'] * len(tiempos_127_unidos))])
tiempo_unido_lagos = tiempo_total_unido - tiempo_teorico_127
tiempo_unido_127 = tiempo_total_unido - tiempo_teorico_lagos
precision_unida = calcular_precision(tiempo_total_teorico, (tiempo_unido_lagos + tiempo_unido_127 - timedelta(minutes=6)))

print("Porcentaje de precisión (Sistema Unido):", precision_unida)

# 3. Graficar la gráfica unida y la teórica
plt.figure(figsize=(16, 12))

graficar_lineas(tiempos_lagos_teo, tiempos_127_teo, 'b', 'Traza Teórica', marker_style=None)
graficar_lineas(tiempos_lagos_unidos, tiempos_127_unidos, 'm', 'Sistema Unido')

# Formatear el eje de tiempo
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator())
plt.xticks(rotation=45, fontsize=12)
plt.yticks([0, 1], ['Lagos', '127'], fontsize=12)

# Aumentar tamaño de los títulos y etiquetas
plt.title('Comparación de Movimientos: Teórico vs Unido', fontsize=16)
plt.xlabel('Tiempo', fontsize=14)
plt.ylabel('Ubicación', fontsize=14)

plt.legend(fontsize=12, loc='upper left')
plt.tight_layout()
plt.show()

# Función para graficar solo puntos sin unirlos con una línea
# Función modificada para incluir zorder
def graficar_puntos(tiempos_lagos, tiempos_127, color, label, grosor_borde=8, zorder=3):
    # Combinar las listas de tiempos y ubicaciones
    tiempos_y_ubicaciones = [(tiempo, 'Lagos') for tiempo in tiempos_lagos] + [(tiempo, '127') for tiempo in tiempos_127]
    # Ordenar por tiempo
    tiempos_y_ubicaciones.sort()
    # Separar tiempos y ubicaciones después de ordenar
    tiempos_ordenados, ubicaciones_ordenadas = zip(*tiempos_y_ubicaciones)
    # Convertir ubicaciones a valores numéricos para la graficación
    y = [0 if ubicacion == 'Lagos' else 1 for ubicacion in ubicaciones_ordenadas]
    plt.scatter(tiempos_ordenados, y, color=color, label=label, linewidths=grosor_borde, zorder=zorder)


# Asumiendo que tiempos_lagos_teo y tiempos_127_teo son listas de objetos datetime
# que representan los tiempos teóricos en los que se debería estar en cada ubicación.
tiempo_minimo = min(tiempos_lagos_teo[0], tiempos_127_teo[0])
tiempo_maximo = max(tiempos_lagos_teo[-1], tiempos_127_teo[-1])

# Asegúrate de llamar a la función después de graficar la traza teórica


# ... código existente ...
plt.figure(figsize=(14, 10))
# Graficar la traza teórica
# Llama a la función con un grosor de línea específico
# Llama a la función con un grosor de línea específico

graficar_lineas(tiempos_lagos_teo, tiempos_127_teo, '#ADD8E6', 'Traza Teórica', marker_style='None', linewidth=8)

# Graficar los puntos unidos para el sistema unido sin unirlos con una línea
graficar_puntos(tiempos_lagos_unidos, tiempos_127_unidos, '#FF66FF', 'Sistema Unido',grosor_borde=5)
# Formatear el eje x para mostrar las fechas correctamente
plt.gcf().autofmt_xdate()  # Autoformato para las fechas en el eje x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=2))  # Ajusta el intervalo si es necesario

# Añadir título y etiquetas de ejes
plt.title('Traza de movimiento sistema unido Samsung A71 background', fontsize=24)
plt.xlabel('Tiempo (H:M)', fontsize=22)
plt.ylabel('Estación de Transmilenio', fontsize=22)
plt.yticks([0, 1], ['lagos', '127'], fontsize=18)
plt.xticks(fontsize=15)
#plt.gcf().autofmt_xdate()
# Ajustar la leyenda
plt.legend(loc='upper left',fontsize=15)

# Mostrar la gráfica
plt.tight_layout()  # Asegura que todo el contenido se ajuste correctamente en la figura


plt.text(0.01, 0.88, 'Precisión sistema ', fontsize=14, transform=plt.gca().transAxes)
plt.text(0.01, 0.85, 'unido de 83%', fontsize=14, transform=plt.gca().transAxes)
plt.show()
