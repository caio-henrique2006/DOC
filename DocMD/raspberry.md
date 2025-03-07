# Raspberry on command line

## Basic commands (UNIX):
```shell

```

## Send files and directories:
```shell
# scp <source> <destiny>
# Do pc para o raspberry pi
scp <pc_file_abs_path> <user>@<ip>:<raspberry_abs_path> # Enviar arquivo
scp -r <pc_directory_abs_path> <user>@<ip>:<raspberry_abs_path> # Enviar diretório
# DO raspberry pi para o pc
scp <user>@<ip>:<raspberry_abs_path> <pc_file_abs_path> # Enviar arquivo
scp -r <user>@<ip>:<raspberry_abs_path> <pc_directory_abs_path> # Enviar diretório
```

## Bluetooth commands:

```shell
bluetoothctl # inicia modo bluetooth
power on # liga o adaptador bluetooth
menu advertise # mostra opções de configuração do advertise
advertise on # se mostra visível para conexões
```
