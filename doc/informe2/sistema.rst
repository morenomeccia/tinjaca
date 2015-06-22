************************
Arquitectura del Sistema
************************

Diseño de la Arquitectura
=========================

El sistema Tinjaca está basado en la plataforma de código abierto de aplicaciones para la gestión
 administrativa *Odoo*.

Desde el punto de vista de su funcionamiento sigue el patrón de diseño de tres capas:

 * *Capa de presentación*: *Odoo* es una aplicación web, por lo tanto ofrece una interfaz web basada
   en HTML5 y CSS3, y un cliente javascript que se comunica con las otras capas del sistema. Una
   característica clave es el uso intensivo de XML para describir las interfaces: ventanas, menúes,
   reportes, plantillas, etc.

 * *Capa de aplicación*: Mediante código Python se maneja el enrutamiento HTTP, la lógica del negocio y las
   notificaciones. Incluye controladores en Python y Javascript que recogen solicitudes de la
   interfaz, realizan consultas a la base de datos, procesa la información recibida y envía los
   resultados a la interfaz de usuario.

 * *Capa de datos*: Permite la especificación de los modelos de datos como clases de Python que realizan una
   transformación objeto-relacional (ORM) hacia una base de datos PostgreSQL. Los mecanismos de persistencia de datos
   funcionan entonces sobre el sistema manejador de bases de datos relacionales PostgreSQL.

Desde el punto de vista del despliegue de la aplicación se trata de una aplicación cliente servidor. El sistema
Tinjaca deber ser puesto en producción considerando:

 * Un *servidor proxy* que maneje las conexiones SSL entrantes para contar con conexiones HTTPS seguras, que las
   desencripte para transmitirlas al servidor.

 * El sistema contará con *servidores HTTP multiproceso* incorporados bajo un mecanismo de balanceo de carga que
   incrementan la estabilidad y la capacidad de respuesta del sistema. El servidor HTTP multiproceso permite monitorizar
   los procesos y establecer límites en el uso de los recursos. El número de procesos recomendado es proporcional a la
   cantidad de núcleos del procesador. También se contemplan *servidores Cron* encargados de automatizar tareas de
   mantenimiento y monitorización sobre los servidores HTTP.

 * Una o mas *bases de datos PostgreSQL*, pueden funcionar varias bases de datos integradas. Por ejemplo, una base de
   datos del propio sistema y otra para un sitio web creado con el Gestor de Contenidos de Odoo, ambas aplicaciones
   estarían perfectamente integradas. También permite contar con una base de datos de pruebas/desarrollo distinta de la
   base de datos de producción.

Descripción de la Descomposición
================================

La descomposición en módulos del sistema Tinjacá responde a los distintos procesos descritos en el *Informe de
Requerimientos y Nudos Críticos de los Sistemas Actuales*.

En este sentido, los módulos serían:

 * Módulo Solicitudes
 * Módulo Aprobación
 * Módulo Administración
 * Módulo Acompañamiento
 * Módulo Caja
 * Módulo Recuperaciones
 * Módulo Consultoría Jurídica
 * Modulo Archivo
 * Módulo Presidencia
 * Módulo Atención

En la sección *Diseño de Módulos* se encuentra una descripción detallada de cada uno.

Justificación del Diseño
========================

Se plantea desarrollar un módulo para cada uno de los procesos planteados en el primer informe realizado en el marco de
este proyecto ya que esto refleja la forma natural de como se llevan a cabo las actividades del FOMDES. Debe
considerarse como una primera versión de la definición del sistema en módulos a ser validado con el personal de FOMDES
en términos estrictos de usabilidad y uso por parte de sus usuarios finales.

La presente propuesta no abarca las funcionalidades asociadas a la contabilidad debido a que la complejidad de la
configuración de las cuentas contables que implicaría incluir módulos de gastos, almacén, nómina entre otros, lo que
haría inviable la realización del proyecto en los lapsos establecidos.