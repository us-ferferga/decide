## Como utilizar el nuevo frontend

La vista de booth ya está configurado para utilizar el nuevo frontend.Simplemente es necesario construirlo
y copiar la salida en las carpetas correspondientes.

El nuevo frontend está preparado para poder desplegarse en otros entornos y servido
por otro servidor que no sea el propio Decide. Por defecto, comprobará si está servido por
el propio Decide o por otro servidor. Si está servido por el propio decide, se conectará automáticamente
y sólo solicitará el ID de la votación.

Estas son las rutas:

`{url}/booth/` - Nuevo frontend
`{url}/booth/old/:id` - Frontend antiguo (este requiere obligatoriamente un ID)
`${url}/booth/api` - Endpoint REST que siempre devuelve 200 OK, sirve para hacer ping
`${url}/booth/api/:id` - Devuelve los datos de la votación con el ID especificado en JSON.

### Despliegue

Podemos ejecutar el comando ``deploy_frontend.sh`` (solo para Bash) o seguir los siguiente pasos.
Es necesario un entorno con Node LTS 18 o superior. Este repositorio cuenta con un devcontainer
para configurar las dependencias correctamente.

Se asume que todos los comandos se ejecutan desde la carpeta en la que se encuentra este archivo

1. Instalamos dependencias: ``npm -w @decide/booth ci``
2. Construimos el cliente: ``npm -w @decide/booth run build``
3. Mezclamos los contenidos de ``frontend/dist/static`` con ``static`` de Django:
4. Movemos ``frontend/dist/index.html`` a ``templates/new`` de Django.
