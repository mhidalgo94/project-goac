# Grupo Optica Admosferica


## Primero paso
Debes tener en cuenta que esta escrito en python 3.7.3, instalar en caso de no tener esta version Python

## Instalar paquete Entorno virutal
Luego debe instalar la versión más reciente del paquete :command:`virtualenv` desde el repositorio :term:`PyPI`, entonces debe instalar con el siguiente comando:
```
$ pip3 install virtualenv
```

## Crear entorno virtual
Para crear entorno virutal
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


