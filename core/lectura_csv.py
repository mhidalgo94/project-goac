# Estructura en clase
from datetime import datetime

# path_file = 'D20210222.csv'

class Lectura_csv:
    
    def __init__(self,path=None, fecha=None, estacion=None):
        if fecha is None:
            self.fecha = datetime.today()
        else:
            self.fecha = fecha
        if estacion is None:
            self.estacion = ["D","F", "J", "T"]
        else:
            self.estacion = estacion
        self.path = path
        self.dicc = {}
        self.key = ['version', 'fecha', 'salida_sol', 'puesta_sol', 'desconocido', 'id', 'nombre', 'cargo', 'fecha_nac', 'xp']
        self.columnas_tabla = 'desconocido','hora', 'min', 'fenom', 'nubosidad', 'temp_aire', 'temp_suelo', 'humedad_relativa', 'disco_solar','directa','difusa','global', 'albedo',	'vel_viento', 'coseno_ang_cenital', 'notas'

    # Hace una lectura el csv
    def read_csv(self):
        with open(self.path, 'r') as doc:
            value = doc.readlines()
            value = [s.strip('\n') for s in value]
            return value

    # Retorna los los datos de la cabezera del csv
    def get_info(self):
        value = self.read_csv()
        self.dicc = dict(zip(self.key, value))
        return self.dicc
    
    # Retorna un diccionario solo con los datos sin cabezera
    def get_dict_datos(self):
        value = self.read_csv()
        dat = value[10:]
        listas = list()
        dict_datos = list()
        for x in dat:
            listas.append(x.split(sep=','))
        for lista in listas:
            dict_datos.append(dict(zip(self.columnas_tabla, lista)))
        return dict_datos

    def csv_today(self, estacion):
        dicc = dict()
        dicc['estacion'] = datetime.today().strftime(""+estacion+"%Y%m%d.csv")
        return dicc


    # Fecha insertada
    def csv_fecha(self,estacion, fecha):
        dicc = dict()
        dicc[estacion] = self.fecha.strftime(""+estacion+"%Y%m%d.csv")
        return dicc