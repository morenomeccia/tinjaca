Arquitectura del Sistema
========================


Diseño de la Arquitectura
-------------------------

El sistema Tinjaca está basado en la plataforma de código abierto de aplicaciones de gestión Odoo.

Desde el punto de vista de su funcionamiento sigue el patrón de diseño de tres capas:

 * *Capa de presentación*: Es una aplicación web, por lo tanto ofrece una interfaz web basada en HTML5 y CSS3, y un
 cliente javascript que se comunica con las otras capas del sistema. Una característica clave es el uso intensivo de XML
 para describir las interfaces: ventanas, menúes, reportes, plantillas, etc.

 * *Capa de aplicación*: Mediante código Python se maneja el enrutamiento HTTP, la lógica del negocio y las
 notificaciones. Contempla controladores en Python y Javascript que recogen solicitudes de la interfaz, realiza
 consultas a la base de datos, procesa la información recibida y envía los resultados a la interfaz.

 * *Capa de datos*: Se especifican los modelos de datos como clases de Python que realiza una transformación
 objeto-relacional (ORM) hacia una base de datos PostgreSQL. Los mecanismos de persistencia de datos funcionan entonces
 sobre el sistema manejador de bases de datos relacionales PostgreSQL.

Desde el punto de vista del despliegue de la aplicación se trata de una aplicación cliente servidor. El sistema
Tinjaca deber ser puesto en producción considerando:

 * Un servidor proxy que maneje las conexiones SSL entrantes para contar con conexiones HTTPS seguras, que las
  desencripte para transmitirlas al servidor.

 * El sistema contará con servidores multiproceso HTTP incorporados bajo un sistema de balanceo de carga que incrementan
  la estabilidad y la capacidad de respuesta del sistema. El servidor HTTP multiproceso permite monitorizar los procesos
  y establecer límites en el uso de los recursos. El número de procesos recomendado es proporcional a la cantidad de
  núcleos del procesador. También se contemplan servidores Cron encargados de automatizar tareas de mantenemiento y
  monitorización sobre los servidores HTTP.

 * Una o mas bases de datos PostgreSQL, pueden funcionar varias bases de datos integradas. Por ejemplo, una base de datos
 del propio sistema y otra para un sitio web creado con el Gestor de Contenidos de Odoo, ambas aplicaciones estarían
 perfectamente integradas. También permite contar con una base de datos de pruebas/desarrollo distinta de la base de
 datos de producción.


Descripción de la Descomposición
--------------------------------

Va a estar constituido por los módulos..., : solicitudes, aprobacion,...

Justificación del Diseño
------------------------

Se plantea desarrollar un modulo para cada uno de los procesos planteados en el informe 1 ya que esto refleja la forma natural de como se llavanm a cabo las actividades del FOMDES.

