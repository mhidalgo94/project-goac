# Grupo Optica Admosferica

## Primero paso
Debes tener en cuenta que esta escrito en python 3.7.3, instalar en caso de no tener esta version Python

## Instalar paquete Entorno virtual
Luego debe instalar la versión más reciente del paquete :command:`virtualenv` desde el repositorio :term:`PyPI`, entonces debe instalar con el siguiente comando:
```
$ pip3 install virtualenv
```

## Crear entorno virtual
Para crear entorno virtual
```
$ pip3 virtualenv nombreEntorno
```

## Instalar requisitos
Para instalar esta lista de dependencias en cualquier otra instalación de Python puedes ejecutar
```
pip3 install -r requisitos.txt
```

## Iniciar Servidor
Para iniciar el servidor debes ejecutar con python archivo manage.py con el argumento runserver..
```
$ python3 manage.py runserver
```
En caso de especificar el puerto del servidor

```
$ python3 manage.py runserver puerto
```

## Crear Super Usuario
En caso no existir el super usuario para el panel administrativo ejecutar este comando y seguir con los procedimientos para crear el usuario
```
$ python3 manage.py createsuperuser
```
# Servicios
## Configuracion Actino
### Archivos CSV y Historicos
En el settings.py hay una variable "ACTINO_ROOT" donde se encuentra los archivos CSV del servicio actino esta se modifica donde esten los .csv, por defecto viene "(BASE_DIR, 'static/servicios/actino/csv')" ya para cuando este incluido se borraria esta carpeta del repo.
Los archivos Historicos no se actualizan a menudo se pueden dejar donde esta o moverlos a donde desees solo debes modificar  la varibale "ACTINO_HISTORICOS_ROOT" donde esten ubicados estos.

Con respecto a los log solo debes tener en cuenta "LOG_ERROR_ACTINO" y "FOLDER_LOG_ROOT"
Este LOG_ERROR_ACTINO es donde se guardan los logs de servidor del actino, esta para ver que ocurre desde la web en caso este en fallo el servicio, este esta ubicado en la carpeta "FOLDER_LOG_ROOT" que donde estan no es necesario cambiarlos(OPCIONAL) solo este archivo o carpeta deben tener los permisos para que el servidor haga la lectura de este asi poder verlos desde la web.
 
