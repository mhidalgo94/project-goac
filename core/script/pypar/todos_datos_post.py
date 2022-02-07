# Este script enviar datos de todos los archivos de de una carpeta
# Tener en cuenta las lib instaladas
#------------------------------------------------------------
# debes insertar el path de la carpeta donde existen
# los archivo que tienen los datos en la variable nombre 'PATH_FILES'

import os, re
import requests

# DOMINIO de la web 
PATH_FILES = '/home/goac/goac-app/scripts/pypar/datos_txt/LBox_com6'

# Dominio de la web
URL_BASE =  'http://goac.caonao.cu'
# Api key para el post seguro
API_KEY = 'b0581e1c4ccf78b61f8704e73e5562538551a909'
# URL Completa
ROOT_URL = f'{URL_BASE}/servicios/pyra-par/api/create/{API_KEY}/'

HEADERS = {'content-type' : 'application/json'}


# En esta variable donde debes incluir el path del directorio de los datos
# PATH_FILES = 'C:\\Users\\PC-GREY\\Documents\\python-test\\test'
PATH_FILES = '/home/goac/goac-app/scripts/pypar/ayer'

# Variables si quieres multiplicar por factores
FACTOR_PYRA = True
FACTOR_PAR = True

# Factorizar PYRA
def fact_pyra(pyra):
    if FACTOR_PYRA:
        calc = pyra / 11.04
        data = '{:9.3f}'.format(calc) # Redondear a 3 valores despues de la coma
        return float(data)
    return pyra
# Factorizar  PAR
def fact_par(par):
    if FACTOR_PAR:
        calc = par * 9.06
        data = '{:9.3f}'.format(calc) # Redondear a 3 valores despues de la coma
        return float(data)
    return par


def enviar_post(**kwargs):
    '''
    Funcion para enviar los datos al server
    '''
    print(kwargs)
    s = requests.post(ROOT_URL ,json=kwargs)
    print(s.status_code, s.json())

def datos(files):
    data = dict()
    with open(files) as doc:
        lines = doc.readlines()[3:]
        char = re.compile(' | |   |   |/')
        for line in lines:
            if line !='\n':
                x = char.split(line)
                t = x[3] or x[4] or x[5] or x[6]
                pyra = float(t)
                y = x.index(t)
                par = float(x[y+1] or x[y+2] or x[y+3] or x[y+4])
                fech = str(x[0]) # Fecha 
                time = str(x[1]) # Tiempo
                # time_mint = str(x[1][0:5])
                fech_compl = '{} {}'.format(fech, time)
                data['fecha'] = fech_compl
                data['pyra'] = fact_pyra(pyra)
                data['par'] =  fact_par(par)
                enviar_post(**data)
            else:
                pass
                # print('Espaciado entre lineas')
                
listdir = os.listdir(PATH_FILES)
for f in listdir:
	path_file = os.path.join(PATH_FILES, f)
	datos(path_file)
