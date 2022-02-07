import os
from config.settings import SERVICE_CONTROL_PATH,SERVICE_CONTROL_FILE


servicios_archivo = os.path.join(SERVICE_CONTROL_PATH, SERVICE_CONTROL_FILE)

def escribir_estado_servicios(servicios):
    restaurar = {'actino': False, 'met': False, 'seoc': False, 'pyra-par': False}
    with open(servicios_archivo, 'w') as f:
        f.write(str(servicios))
    return servicios


def leer_estado_servicios():
    servicios = dict()
    with open(servicios_archivo,'r') as f:
        content = f.read()
        servicios = eval(content)
    return servicios