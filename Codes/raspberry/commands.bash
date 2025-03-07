# https://punchthrough.com/creating-a-ble-peripheral-with-bluez/

bluetoothctl

manu advertise
manufacturer 0xffff 0x12 0x34
name myDevice

back
advertise on

menu gatt
register-service uuid
register-characteristic 0x1234 read
register-characteristic 0x4567 read,write

sudo hciconfig hci0 up # Liga o dispositivo bluetooth 0
sudo hciconfig hci0 piscan # Determina o dispositivo bluetooth como advertise e conect ao mesmo tempo

sudo systemctl status bluetoothc # Checa se o bluetooth está funcionando no raspberry