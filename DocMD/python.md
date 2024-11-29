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
