import smbus
import time
from datetime import datetime

# Configura el bus I2C
bus = smbus.SMBus(1)

# Dirección del RTC DS3231
address = 0x68

# Convierte a formato binario
def bcd_to_dec(bcd):
    return (bcd & 0x0F) + ((bcd >> 4) * 10)

# Lee la hora actual del RTC
def read_time():
    data = bus.read_i2c_block_data(address, 0x00, 7)
    sec = bcd_to_dec(data[0] & 0x7F)
    min = bcd_to_dec(data[1])
    hour = bcd_to_dec(data[2] & 0x3F) # Modo 24 horas
    return hour, min, sec

# Sincroniza la hora del sistema con el RTC
def sync_time():
    hour, min, sec = read_time()
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    time_string = f"{current_date} {hour}:{min}:{sec}"
    print("Sincronizando con: ", time_string)
    os.system(f"sudo date -s '{time_string}'")

# Ejecuta la sincronización
sync_time()
