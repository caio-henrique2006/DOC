# Python

## files

### get file names
```python
import os
files = [f[0:44] for f in os.listdir() if os.path.isfile(f)] # nomes de arquivos dentro da pasta
```
## CSV e Excel

### get column csv
```python
import csv
file = open('m.csv')

csvreader = csv.reader(file)

lista_excel = []
for row in csvreader:
  lista_excel.append(row)
```

## Create virtual enviroment
```shell
python3 -m venv <virtual_enviroment_name> # It is gonna display it self like a folder
```

## Python Bleak BLE:
### Código de teste:
```python
# https://getwavecake.com/blog/reading-your-phones-battery-level-over-bluetooth-ble-with-python-bleak/
import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover(5.0, return_adv=True)
    for d in devices:
        print(d)

asyncio.run(main())
```