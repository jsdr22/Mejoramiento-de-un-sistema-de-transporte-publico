sleep 30
ip link set wlan0 down
ip link set wlan1 down 
iw wlan1 set monitor none 
ip link set wlan1 up 
fecha=$(date +"%Y-%m-%d_%H-%M-%S")
tshark -i wlan1 -Y "wlan.fc.type_subtype == 0x04" -Q -T fields -e frame.time_epoch -E separator=, -e wlan_radio.signal_dbm -E separator=, -e wlan.sa -E separator=, -e wlan.tag.number > /home/pi/paquetes/paquetes_${fecha}.txt

