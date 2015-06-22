***********
Descripción
***********

Objetivo del Informe
====================

Proveer una descripción del diseño del sistema suficientemente completo que permita iniciar el desarrollo de software
con una comprensión de lo que se desea hacer y como se espera llevar a cabo. De igual manera, sirve para establecer un
lenguaje común entre el equipo de desarrolladores y el personal de FOMDES.

Bajo ese orden de ideas, se presenta el modelo de integración de los datos así como los distintos módulos previstos para
TINJACÁ, a la luz de las historias de usuario presentadas en el Informe de Requerimientos y Nudos Críticos de los
Sistemas Actuales.

Alcance
=======

El diseño de un sistema informático supone la consideración de distintos elementos que pueden determinar desde su
configuración hasta su posterior instalación y prueba por parte de los usuarios finales y que, por tanto, afectarán de
modo directo la forma en que se logra satisfacer las historias de usuario diagnosticadas.

Trabajando sobre la premisa de optimizar la propuesta y que TINJACÁ sirva efectivamente de apoyo para la realización de
las labores propias del desempeño de FOMDES, la integridad de la información y la simplificación de tareas se evidencian
como elementos clave dentro del diseño final, este documento incluye el modelo lógico de entidad-relación, el diseño de
datos y el diseño de módulos del sistema TINJACÁ.

Adicionalmente se incluye el cronograma propuesto para las fases de desarrollo y de pruebas del sistema TINJACÁ.

Metodología General
===================

Partiendo de las historias de usuario presentadas en el informe diagnóstico, este documento presenta propuestas para el
modelado de datos y del modelo lógico del sistema, todo ello a fin de atender la necesaria resolución de los nudos
críticos identificados con anterioridad.

Estos nudos críticos, como se ha señalado en un informe anterior, tienen que ver con:

 * Problemas de interacción entre las unidades dentro de FOMDES en el ejercicio de sus funciones
 * Mejorar las interfaces de usuario y dinamizar su experiencia e interacción con el sistema
 * Incluir al sistema reportes de gestión de informacion que se llevan en hoja de calculo
 * Mejorar la usabilidad del sistema y precindir de hojas de cálculo para tener control
 * Minimizar los errores e incidencias y optimizar el rendimiento de consultas de actualización
 * Disponer de información oportuna
 * Evitar duplicación de información
 * Generar reportes automáticos que respondan a las necesidades de toma de decisiones por parte de la
   presidencia de la institución.

Referencias
===========

El documento básico al que se hace referencia en este documento es el primer informe de este proyecto:

Ospino Velásquez, H. J. (2015). Informe de Requerimientos y Nudos Críticos del Sistema Actual (Ver No. 1.2). Mérida,
Venezuela. Retrieved from https://github.com/sani-coop/tinjaca/tree/master/doc/informe1

El informe fue preparado siguiendo las pautas y criterios de estándares profesionales internacionales en el tema, a
saber:

Institute of Electrical and Electronics Engineers. (2009). 1016-2009  -  IEEE Standard for Information
Technology--Systems Design--Software Design Descriptions. In IEEE standard for information technology--systems
design--software design descriptions (pp. 1 – 35). New York: IEEE. Retrieved from
http://ieeexplore.ieee.org/servlet/opac?punumber=5167253

Spolsky, J. (2000, Octubre 3). Painless Functional Specifications - Part 2: What’s a Spec? Retrieved from
http://www.joelonsoftware.com/articles/fog0000000035.html




