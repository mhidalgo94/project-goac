import ephem
from datetime import datetime, timezone
from django.utils import timezone as tzdj

def convert_localtime(utc_time):
    lt_ = ephem.Date(utc_time - 5 * ephem.hour) #tiempo local

    (y, mn, d, h, mint, s) = lt_.tuple()
    convert = datetime(y, mn, d, h, mint, 0, 0)#, tzinfo=tzdj.utc)

    return convert
    

def salida_puesta(fecha=None):
    if fecha:
        formato = '%Y-%m-%d'
        fecha_local = datetime.strptime(fecha, formato)
    else:
        fecha_local = datetime.now().strftime('%Y-%m-%d')

    #defining an observer
    obs = ephem.Observer()
    
    #defining position de Camaguey
    default_long = '-77.9184'
    default_lat = '21.3789'
    
    # obs.long = ephem.degrees(str(long))
    # obs.lat = ephem.degrees(str(lat))
    obs.long = default_long
    obs.lat = default_lat
    
    
    #defining date
    # obs.date = ephem.Date(date)
    obs.date = fecha_local
    
    #defining an astronomic object; Sun in this case
    sun = ephem.Sun(obs)
    
    r1 = obs.next_rising(sun) # salida sol
    s1 = obs.next_setting(sun) # puesta sol

    salida = convert_localtime(r1)
    puesta = convert_localtime(s1)

    return {"salida":salida, "puesta":puesta}

