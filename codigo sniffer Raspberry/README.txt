Para el rtc necesitas tener estos comandos antes de correr el codigo en python.

sudo apt-get update
sudo raspi-config
sudo apt-get install python3-smbus i2c-tools


Raspberry Pi 4.
Módulo RTC DS3231
Pasos para la Configuración del Hardware
Conecta el módulo RTC a tu Raspberry Pi:

VCC del RTC al pin 5V del Raspberry Pi.
GND del RTC al pin GND.
SDA del RTC al pin SDA (GPIO 2).
SCL del RTC al pin SCL (GPIO 3).