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

## Using python's subprocess library to run bluetooth in raspberry:

### Executing commands:
To execute a command, you can use subprocess.run() or subprocess.Popen().

subprocess.run(): Runs a command and waits for it to complete. It's simpler but less flexible for interactive processes.

subprocess.Popen(): Provides more control, allowing you to interact with the process in real-time (e.g., sending input and reading output).

```python
import subprocess

result = subprocess.run([])
```

### Code:

```python
import subprocess

# Used to sens a command to a process
def send_command(command):
    process.stdin.write(command + "\n")
    process.stdin.flush()
    # Read the output line by line
    output = []
    while True:
        line = process.stdout.readline()
        if not line.strip():  # Stop reading if the line is empty
            break
        output.append(line.strip())
    return output

# Start bluetoothctl in interactive mode
process = subprocess.Popen(["bluetoothctl"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

response = send_command("advertise on")
print(response)
```