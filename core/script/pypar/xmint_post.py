# Este script enviar solo los datos de la ultima linea del utimo archivo
# Tener en cuenta las lib instaladas
#------------------------------------------------------------
# debes insertar el path de la carpeta donde existen
# los archivo que tienen los datos en la variable nombre 'PATH_FILES'

import json
import requests
import os, re

PATH_FILES = '/home/goac/goac-app/scripts/pypar/datos_txt/LBox_com6'


# Dominio de la web
URL_BASE =  'http://127.0.0.1:8000'
# Api key para el post seguro
API_KEY = '85a01ce3e90de7321ac1a21b12907118c4ae735c'
# URL Completa
ROOT_URL = f'{URL_BASE}/servicios/pyra-par/api/create/{API_KEY}/'


# Factores
FACTOR_PYRA = 11.04
FACTOR_PAR = 9.06

def last_file():
    # path = En esta variable inserte la carpeta de los datos
    path = PATH_FILES
    listdir = os.listdir(path)
    list_file = [os.path.join(path, basename) for basename in listdir]
    ult_archivo = max(list_file, key=os.path.getmtime)
    data = dict()
    # Lectura del archivo
    print(ult_archivo)
    with open(ult_archivo) as doc:
        lines = doc.readlines()[-2:-1]
        char = re.compile(' | |   |   |/')
        for line in lines:
            x = char.split(line)
            t = x[3] or x[4] or x[5] or x[6]
            pyra = float(t)
            y = x.index(t)
            par = float(x[y+1] or x[y+2] or x[y+3] or x[y+4])
            fech = str(x[0])
            time = str(x[1])
            time_mint = str(x[1][0:5])
            fech_compl = '{} {}'.format(fech, time)
            data['fecha'] = fech_compl
            data['pyra'] = pyra
            data['factor_pyra'] = FACTOR_PYRA
            data['par'] =  par
            data['factor_par'] =  FACTOR_PAR
    return data

datos = last_file()

try:
    djson = json.dumps(datos)
    print(djson)
    s = requests.post(ROOT_URL , data=datos)
    
    print(s.status_code)
    print(s.json())
except requests.exceptions.ConnectionError:
    print('Error de conexion: No se ha podido conectar al servidor')



