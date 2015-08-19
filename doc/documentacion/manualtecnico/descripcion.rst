******************************
Descripción General de TINJACÁ
******************************

TINJACA es el Sistema Integrado para el Control Administrativo del Fondo Merideño para el
Desarrollo Económico Sustentable (FOMDES). Constituye un software desarrollado con tecnologías
libres y hecho con consideraciones a las particularidades propias de un ente regional como el
FOMDES.

Su arquitectura es modular, lo cual facilita la incorporación posterior de dispositivos dentro
del software para dar cuenta de otras necesidades del FOMDES.

Está basado en Odoo v8 (http://odoo.com ) que es un software orientado a satisfacer necesidades
empresariales y de instituciones en procesos de planificación de recursos empresariales
(Enterprise Resource Planning ERP).

El manejador de base de datos utilizado por Odoo v8 es Postgre Sql, cuyo funcionamiento es
gestionado a través de un ORM propio.

Desde el punto de vista de su funcionamiento TINJACA sigue el patrón de diseño de tres capas:

# Capa de presentación: Odoo es una aplicación web, por lo tanto ofrece una interfaz web basada en
 HTML5 y CSS3, y un cliente javascript que se comunica con las otras capas del sistema. Una
 característica clave es el uso intensivo de XML para describir las interfaces: ventanas, menúes,
 reportes, plantillas, etc.

# Capa de aplicación: Mediante código Python se maneja el enrutamiento HTTP, la lógica del negocio
 y las notificaciones. Incluye controladores en Python y Javascript que recogen solicitudes de la
 interfaz, realizan consultas a la base de datos, procesa la información recibida y envía los
 resultados a la interfaz de usuario.

# Capa de datos: Permite la especificación de los modelos de datos como clases de Python que
realizan una transformación objeto-relacional (ORM) hacia una base de datos PostgreSQL. Los
mecanismos de persistencia de datos funcionan entonces sobre el sistema manejador de bases de
datos relacionales PostgreSQL.

La implementación de Odoo se ha adaptado para dar cuenta de las características propias de FOMDES
 para la adecuada gestión de las solicitudes de créditos a las unidades productivas del estado.