*************************
Requerimientos de TINJACA
*************************

Desde el punto de vista del despliegue de la aplicación se trata de una aplicación cliente
servidor. El sistema Tinjaca deber ser puesto en producción considerando:

# Un servidor proxy que maneje las conexiones SSL entrantes para contar con conexiones HTTPS
seguras, que las desencripte para transmitirlas al servidor.

# El sistema contará con servidores HTTP multiproceso incorporados bajo un mecanismo de balanceo
de carga que incrementan la estabilidad y la capacidad de respuesta del sistema. El servidor HTTP
multiproceso permite monitorizar los procesos y establecer límites en el uso de los recursos. El
número de procesos recomendado es proporcional a la cantidad de núcleos del procesador. También se
contemplan servidores Cron encargados de automatizar tareas de mantenimiento y monitorización
sobre los servidores HTTP.

# Una o mas bases de datos PostgreSQL, pueden funcionar varias bases de datos integradas. Por
ejemplo, una base de datos del propio sistema y otra para un sitio web creado con el Gestor de
Contenidos de Odoo, ambas aplicaciones estarían perfectamente integradas. También permite contar
con  una base de datos de pruebas/desarrollo distinta de la base de datos de producción.
