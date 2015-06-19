Arquitectura del Sistema
========================


Diseño de la Arquitectura
-------------------------

El sistema Tinjaca está basado en la plataforma de código abierto de aplicaciones para la gestión
 administrativa *Odoo*.

Desde el punto de vista de su funcionamiento sigue el patrón de diseño de tres capas:

 * *Capa de presentación*: *Odoo* es una aplicación web, por lo tanto ofrece una interfaz web basada
  en HTML5 y CSS3, y un cliente javascript que se comunica con las otras capas del sistema. Una
  característica clave es el uso intensivo de XML para describir las interfaces: ventanas, menúes,
  reportes, plantillas, etc.

 * *Capa de aplicación*: Mediante código Python se maneja el enrutamiento HTTP, la lógica del negocio y las
 notificaciones. Incluye controladores en Python y Javascript que recogen solicitudes de la
 interfaz, realiza consultas a la base de datos, procesa la información recibida y envía los
 resultados a la interfaz de usuario.

 * *Capa de datos*: Permite la especificación de los modelos de datos como clases de Python que
 realiza
 una transformación
 objeto-relacional (ORM) hacia una base de datos PostgreSQL. Los mecanismos de persistencia de datos funcionan entonces
 sobre el sistema manejador de bases de datos relacionales PostgreSQL.

Desde el punto de vista del despliegue de la aplicación se trata de una aplicación cliente servidor



Descripción de la Descomposición
--------------------------------

Va a estar constituido por los módulos..., : solicitudes, aprobacion,...

Justificación del Diseño
------------------------

Se plantea desarrollar un modulo para cada uno de los procesos planteados en el informe 1 ya que esto refleja la forma natural de como se llavanm a cabo las actividades del FOMDES.

