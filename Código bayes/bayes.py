import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Valores de lambda específicos para cada n (experimentalmente calculados)
#lambdas_experimentales = [10.2037875, 19.51025, 28.350375, 38.12, 47.65, 57.18, 66.71, 76.24, 85.77, 95.3]
lambdas_experimentales = [10.2037875, 19.51025, 28.350375, 38.12]

# paquetes_capturados: representa el número total de paquetes "probe request" 
#                      que se han capturado en el intervalo de tiempo especificado (por ejemplo, 2 minutos).
#                      Ejemplo: Si en 2 minutos capturas 80 paquetes, entonces paquetes_capturados = 80.

# lambda_C: Descripción: Es el parámetro λ de la distribución de Poisson que se utiliza para definir las probabilidades 
#                        a priori de cuántos celulares podrían estar presentes en la estación de transporte.
#                        Representa el número promedio de celulares que esperaríamos encontrar en la estación, basado en 
#                        alguna información previa o alguna consideración.
#                        Ejemplo: Si, basado en observaciones anteriores o alguna otra consideración,
#                        hay 2 celulares en la estación en cualquier intervalo de tiempo dado,
#                        entonces lambda_C = 2.

def inferencia_bayesiana(paquetes_capturados, lambda_C, max_celulares=4):
    # Probabilidades a priori
    # Calcula las probabilidades a priori para tener entre 0 y max_celulares celulares presentes.
    # La lista prioris contendrá estas probabilidades.
    prioris = [poisson.pmf(n, lambda_C) for n in range(1, max_celulares+1)]
    
    # Verosimilitud utilizando los valores experimentales de lambda
    verosimilitud = [poisson.pmf(paquetes_capturados, lam) for lam in lambdas_experimentales]
    
    # Probabilidades a posteriori no normalizadas
    # Multiplica las probabilidades a priori por la probabilidad condicional correspondiente para obtener 
    # las probabilidades conjuntas 
    posteriores_no_normalizados = [priori * vero for priori, vero in zip(prioris, verosimilitud)]
    
    # Normalización
    # Normaliza las probabilidades a posteriori para que sumen 1.
    suma_posteriores = sum(posteriores_no_normalizados)
    posteriores = [post / suma_posteriores for post in posteriores_no_normalizados]
    
    # Estimación del número más probable de celulares presentes
    estimacion_celulares = 1 + np.argmax(posteriores)
    
    return estimacion_celulares, posteriores[estimacion_celulares-1], posteriores

# Ejemplo de uso:
paquetes_observados = 14 # Paquetes por minuto
lambda_C_priori = 12   # Valor de lambda para la probabilidad a priori
max_celulares = 4     # Definimos max_celulares antes de usarlo

estimacion, probabilidad_posteriori, todas_posteriori = inferencia_bayesiana(paquetes_observados, lambda_C_priori, max_celulares)

print(f"Estimación del número de celulares presentes: {estimacion}")
print(f"Probabilidad a posteriori correspondiente: {probabilidad_posteriori:.4f}")

# Graficar probabilidades a posteriori
celulares = np.arange(1, max_celulares + 1)

plt.figure(figsize=(10, 6))
plt.bar(celulares, todas_posteriori, width=0.4, align='center', alpha=0.7)
plt.xlabel('Número de Celulares',fontsize=18)
plt.ylabel('Probabilidad a Posteriori',fontsize=18)
plt.title('Gráfica de probabilidades a posteriori prueba 1 foreground',fontsize=18)
plt.xticks(celulares)
plt.tight_layout()
plt.show()




