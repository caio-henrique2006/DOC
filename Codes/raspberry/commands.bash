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
