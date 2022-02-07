import json
import requests
import re
import os
from datetime import datetime

KEY = ['fecha','pr','ta','hr','vv','dv','ri','hi']

# Path de los archivos csv
MET_ROOT = '/home/goac/goac-app/scripts/file_met'


HEADERS = {
    "Content-type": "application/json"
}

# Estrucutra url para envio de datos
URL_ROOT = 'http://localhost'
URL_API = '/servicios/met/api/create/'
API_KEY = 'f7c8d81e166b048a17425f3903534b7ee757bfd7'+ '/'

URL = f'{URL_ROOT}{URL_API}{API_KEY}'

ACTIVE_LOG = True

LOG_ROOT = '/home/goac/goac-app/scripts/logs'
NAME_FILE_LOG = 'met_log.txt'

# Nombre archivo diario
hoy_to_str = datetime.now().strftime('%Y%m%d') 
#ARCHIVO = f'CN16{hoy_to_str}0000A.met'
ARCHIVO = 'cn16.met'

# Salvar Log
def save_log(texto):
    if ACTIVE_LOG:
        path_log_file = os.path.join(LOG_ROOT, NAME_FILE_LOG)
        fecha = datetime.now().strftime('%d-%m-%Y %H:%M')
        if os.path.isfile(path_log_file):
            with open(path_log_file,'a') as doc:
                doc.write("\n"+fecha+" "+texto)
        else:
            with open(path_log_file,'w') as doc:
                doc.write("# Archivo log de SEOC\n"+fecha+" "+texto)
    else:
        print(texto)


# Funcion para guardar los datos via post 
def request_post(data):
    data = data
    print('verificand')
    try:
        js = json.dumps(data)
        fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        s = requests.post(URL ,data=js, headers=HEADERS)
        status_code = s.status_code
        if status_code in range(200, 299):
            text = f'{fecha_hora} POST {status_code}: Envio de datos correctamente: {ARCHIVO}'
            print(text)
            save_log(text)
        else:
            info = s.json()
            print(info)
            text = f'POST {status_code}: {info}'
            save_log(text)
            s.connection.close()
    except requests.exceptions.ConnectionError:
        text = 'Error de conexion: No se ha podido conectar al servidor'
        save_log(text)


def vinc_data(*lista):
    '''
    Primero vincula los datos de la lista con el diccionario  luego
    integra los datos de anio, mes, dias, horas, minutos y segundos en un datetime llamado fecha
    para enviar los datos via web metodo post al servidor, alli el servidor los valida para guradarlos
    si la fecha(datatime) existe en la base datos retornara error de validacion
    '''
    v_lista = dict(zip(KEY,lista))
    str_format = "%Y-%m-%d %H:%M:%S"

    # # Integrando fecha
    fecha_ = datetime.strptime(v_lista['fecha'],str_format)
    fecha = fecha_.strftime("%Y-%m-%dT%H:%M:%S")

    vv = float(v_lista['vv'])*3.6
    v_lista['vv'] = float('{:9.2f}'.format(vv))
    v_lista['pr'] = float(v_lista['pr'])
    v_lista['ta'] = float(v_lista['ta'])
    v_lista['hr'] = float(v_lista['hr'])
    v_lista['dv'] = float(v_lista['dv'])
    v_lista['ri'] = float(v_lista['ri'])
    v_lista['hi'] = float(v_lista['hi'])
    v_lista['rc'] = float(v_lista['ri'])/10
    v_lista['hc'] = float(v_lista['hi'])/10
    v_lista['fecha'] = fecha
    request_post(v_lista)


def redondear_lista(lista):
    cantidad_redondear = len(lista)
    fecha = list()
    lista_5 = list()
    lista_sumar_valores = list()
    lista_final = list()
    for i in lista:
        fecha.append(i.pop(0))
        list_to_float = list(map(float, i))
        lista_5.append(list_to_float)
    for index, nombre in enumerate(lista_5):
        if index == 0:
            lista_sumar_valores = nombre
        else:
            lista_sumar_valores = [x+y for x,y in zip(lista_sumar_valores, nombre)]

    for m in lista_sumar_valores:
        promediar = m/cantidad_redondear
        formato = '{:.4f}'.format(promediar)
        lista_final.append(formato)
    
    lista_final.insert(0, fecha[0])
    print(lista_final)
    vinc_data(*lista_final)
        

def iniciar_():
    
    path_archivo = os.path.join(MET_ROOT, ARCHIVO)
    # Lectura del archivo 
    todas_listas = list()
    contar_lista = int()
    with open(path_archivo, 'r') as f:
        lines = f.readlines() # Lectura de lineas de archivo
        char = re.compile(' ') 
        contar_lista= len(lines)
        for line in lines[15:]:
            x = char.split(line) # Separa los datos por comas
            del_enter = [s.strip('\n') for s in x] # Eliminar el \n de la lista
            del_espacios = [elemento for elemento in del_enter if elemento != ""] # Crear una lista sin espaciones en blanco
            # fecha_str es crear la fecha de los datos en datetime
            fecha_str = "20{}-{}-{} {}:{}:{}".format(del_espacios[0],del_espacios[1],del_espacios[2],del_espacios[3], del_espacios[4],del_espacios[5]) 
            # este for es para eliminar los datos de fechas que estan separado ya que los integre en un datetime (fecha_str)
            for i in range(6): 
                del_espacios.pop(0)
            del_espacios.insert(0,fecha_str) # Aqui se agrega la fecha datetime (fecha_str) al inicio de cada lista
            todas_listas.append(del_espacios) # Agregar a la lista de todas las listas 

    # Separar la lista de 5 en 5 hasta que llegue al final
    d = 0 # D para seleccionar el inicio de la lista
    c = 5 # C es para seleccionar hasta a lista 5
    while c < contar_lista:
        lista_5 = todas_listas[d:c]
        x = len(lista_5) # Contar si la lista_5 tiene datos

        d = c
        c =  d + 5
        # Si la lista no tiene datos terminar el bucle while
        if x == 0:
            break
        redondear_lista(lista_5)



if __name__ == '__main__':
    iniciar_()
    
