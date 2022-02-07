import os
from datetime import datetime

# path_log_file = os.path.join(LOG_ERROR_ACTINO, 'actino_log.txt')

def save_log(path_log_file,texto):
    fecha = datetime.now().strftime('%d-%m-%Y %H:%M')
    if os.path.isfile(path_log_file):
        with open(path_log_file,'a') as doc:
            doc.write("\n"+fecha+" "+texto)
    else:
        with open(path_log_file,'w') as doc:
            doc.write("# Archivo para salvar log de peticiones de actino\n# Se incluyen los archivos borrados desde el panel\n"+fecha+" "+texto)
    

def read_log_error(path_log_file):
    try:
        with open(path_log_file, 'r') as doc:
            read = doc.readlines()
        return read
    except:
        return False
    
def estado_log(path_log_file):
    info = dict()
    try:
        file_modif = os.path.getmtime(path_log_file)
        date_modif = datetime.fromtimestamp(file_modif)
        size_file = os.path.getsize(path_log_file)
        info = {'fecha_modif': date_modif, 'tamano_archivo': size_file, 'lectura_log': read_log_error(path_log_file)}
    except:
        with open(path_log_file,'w') as doc:
            doc.write("# Archivo para salvar log")
            estado_log(path_log_file)
    
    return info
