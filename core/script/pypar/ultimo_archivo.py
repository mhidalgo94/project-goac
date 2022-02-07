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
URL_BASE =  'http://goac.caonao.cu'
# Api key para el post seguro
API_KEY = 'b0581e1c4ccf78b61f8704e73e5562538551a909'
# URL Completa
ROOT_URL = f'{URL_BASE}/servicios/pyra-par/api/create/{API_KEY}/'

HEADERS = {'content-type' : 'application/json'}

# Variables si quieres multiplicar por factores
FACTOR_PYRA = 11.04
FACTOR_PAR = 9.06



def enviar_post(data):
    '''
    Funcion para enviar los datos al server
    '''
    jsn = json.dumps(data)
    print(data)
    s = requests.post(ROOT_URL ,json=data, headers=HEADERS)
    print(s.status_code, s.json())

def last_file():
    path = PATH_FILES
    listdir = os.listdir(path)
    list_file = [os.path.join(path, basename) for basename in listdir]
    ult_archivo = max(list_file, key=os.path.getmtime)
    print(ult_archivo)
    data = dict()
    # Lectura del archivo
    with open(ult_archivo) as doc:
        lines = doc.readlines()[3:]
        char = re.compile(' | |   |   |/')
        for line in lines:
            if line !='\n':
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
                enviar_post(data)

            else:
                pass
                # print('Espaciado entre lineas')

last_file()

