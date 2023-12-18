Este Dockerfile debe de tener su contexto en la raíz del repositorio.
Para construir la imagen desde esta carpeta:

``
docker build ../.. -t tu/etiqueta -f Dockerfile
``

Otra forma de hacerlo es, desde la raíz del repositorio:

``
docker build . -t tu/etiqueta -f packaging/docker/Dockerfile
``

### Variables de entorno de la imagen

Y sus valores por defecto:

Establecidos a la hora de construir la imagen:

```
DJANGO_SUPERUSER_USERNAME=$DJANGO_SUPERUSER_USERNAME (depende del argumento con el mismo valor dado a la hora de construir)
DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL (depende del argumento con el mismo valor dado a la hora de construir)
DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD (depende del argumento con el mismo valor dado a la hora de construir)
DB_USE_SQLITE=1 (en caso de que no exista o sea 0, se usará PostgreSQL que deberá configurarse en un
contenedor aparte)

Por defecto:

ARG DJANGO_SUPERUSER_USERNAME=decide
ARG DJANGO_SUPERUSER_EMAIL=admin@decide.org
ARG DJANGO_SUPERUSER_PASSWORD=decide
```

A utilizar durante la ejecución:

```
DB_NAME='data/decide.sqlite3' (Si DB_USE_SQLITE=1, si no 'decide')
DB_USER: Sin establecer (Si DB_USE_SQLITE=1, si no 'decide')
DB_PASSWORD: Sin establecer (Si DB_USE_SQLITE=1, si no 'decide')
DB_HOST: Sin establecer (Si DB_USE_SQLITE=1, si no 'postgresql')
DB_PORT: Sin establecer (Si DB_USE_SQLITE=1, si no '5432')
```
