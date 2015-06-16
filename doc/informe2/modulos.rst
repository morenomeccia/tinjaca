Diseño de modulos
=================

Módulo Crédito
==============

Descripción
-----------

Este módulo abarca los procesos de "Recepción de propuestas" y "Recepción y Evaluación de Solicitudes". Incluye procedimientos asociados con la recepción y validación de la propuesta de financiamiento, validación de recaudos para solicitud de crédito y generación del listado de expedientes sugeridos para aprobación de créditos.

Usuarios
--------

Información de Crédito, Análisis Jurídico, Análisis Económico, Gerente de Crédito.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Ingreso de datos del solicitante
         - Analista de crédito
         - Todos los datos del solicitante
       * - Ingreso de datos de la propuesta de financiamiento desde la planilla consignada y la generacion del código de la misma
         - Analista de crèdito
         - Datos de la propuesta de financiamiento y codigo
       * - Registro de la viabilidad de la propuesta según las normativas del FOMDES
         - Analista de credito
         - Viabilidad de propuesta
       * - Consultar el listado de propuestas de financiamiento que son viables
         - Analista de credito
         - Lista de propuestas de financiamiento
       * - Envio por correo eletronico a los potenciales beneficiarios la invitación para la asistencia al taller
         - Analista de credito
         - Registro del envio de requisitos
       * - Incluir al solicitante en la lista del “Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario”
         - Analista de credito
         - Lista del taller
       * - Registro en lista de espera de los potenciales beneficiarios que no asistan al taller
         - Analista de credito
         - Lista de espera
       * - Registro de la validez de los requisitos
         - Analista de credito
         - Validez de los requisitos
       * - Creación de expediente con código por sector
         - Analista de credito
         - ???
       * - Generar informes POA
         - Analista de credito
         - ???
       * - Registro de la validez legal de la garantía
         - Analista Jurídico
         - Validez legal de garantia
       * - Generacion del informe de control previo
         - Analista Jurídico
         - ???
       * - Asignacion el estatus de “CUMPLE”, “NO CUMPLE” o “CUMPLE CONDICIONADO” para las garantías
         - Analista Juridico
         - Estatus de la garantia
       * - Envio del expediente a la estación de Análisis Económico
         - Analisis Juridico
         - ???
       * - Generación de rutas para visitar la unidad de producción
         - Analista Económico
         - ???
       * - Registro de la viabilidad económica de la unidad de producción
         - Analista Económico
         - Viabilidad económica de la unidad de producción
       * - Generacion el informe de inspección (informe técnico) con registro fotográfico
         - Analista Economico
         - Resultados de la inspeccion
       * - Ingreso de fotografías de inspecciones en cada expediente
         - Analista Economico
         - Fotografias de inspeccion
       * - Registro de las minutas que se levantan en campo e inclusion en el informe tecnico
         - Analista Economico
         - Informe tecnico
       * - Ingreso de los resultados del avalúo
         - Analista Económico
         - Resultados del avaluo
       * - Ingreso del informe técnico de la garantia
         - Analista Económico
         - Informe tecnico de la garantia
       * - Especificacion de los lapsos de pago del crédito por el beneficiario
         - Analista Economico
         - Lapsos de pago del credito
       * - Enviar el expediente al Gerente de Crédito
         - Analista Economico
         - Expediente
       * - Inclusión del expediente en la lista para consideración del Consejo Directivo
         - Gerente de crédito
         - Lista para consideración del Consejo Directivo
       * - Modificar las tasas de interés y los montos asignados por sector, rubro o garantía
         - Gerente de credito
         - Tasas de interés
       * - Seleccionar los proyectos que van al consejo directivo
         - Gerente de credito
         - ???
       * - Envío de expediente a la Secretaría ejecutiva
         - Gerente de crédito
         - ???
       * - Generacion de una lista de rezagados en caso de que se termine el presupuesto pautado
         - Gerente de credito
         - ???
       * - Realizar reportes por municipio, por rubro, por estatus y por rango de fechas
         - Gerente de credito
         - ???
       * - Distribucion de los analistas económicos por municipios y parroquias para realizar las inspecciones
         - Gerente de credito
         - Tabla de distribucion de los analistas economicos.
       * - Envio del expediente a la estación de Análisis Jurídico
         - Analista de credito
         - ???
       * - Modificacion de la solicitud de requisitos de acuerdo al sector, a los montos, a los rubros y tipo de empresa.
         - Analista de credito
         - Solicitud del dato

Campos modificados de cada entidad
----------------------------------

- Solicitante: 

	* Todos los campos del Solicitante

- Potencial beneficiario:

	* Todos los campos del Potencial beneficiario
	
- Beneficiario:

	* Todos los campos del Beneficiario
	
- Propuesta de financiamiento:

	* Todos los campos de la Propuesta de financiamiento.
	* Viabilidad de la propuesta

- Expediente:

	* Viabilidad de los requisitos.
	* Validez legal de la garantia.
	* Viabilidad económica de la unidad de producción.
	* Informe de inspección de la unidad de producción.
	* Informe de avalúo de la garantia.
	* Informe técnico de la garantia.

- Lista de convocados al “Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario”

- Lista de expedientes para consideración del Consejo Directivo.

Módulo Secretaría
=================

Descripción
-----------

Este módulo abarca los procesos de "Aprobación de Créditos". Incluye los procedimientos asociados con la recepción de la lista de expedientes sugeridos para aprobación de crédito, la elaboración del Documento de Crédito y constitución de la empresa (de requerirse) para cada uno de los beneficiarios(as).

Usuarios
--------

Secretaría Ejecutiva, Presupuesto, Consejo Directivo, Presidente.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Ordenamiento de la lista de expedientes según sus prioridades
         - Secretaría Ejecutiva
         - Lista de expedientes
       * - Registro de la certificación de disponibilidad presupuestaria y financiera del crédito
         - Secretaría Ejecutiva
         - Certificación de disponibilidad presupuestaria y financiera del crédito
       * - Creación de la convocatoria al consejo directivo con agenda de expedientes priorizados
         - Secretaría Ejecutiva
         - Convocatoria al consejo directivo
       * - Ingreso del documento de crédito al expediente
         - Secretaría Ejecutiva
         - ???
       * - Ingreso del documento de documento de la empresa
         - Secretaría Ejecutiva
         - ???


Campos modificados de cada entidad
----------------------------------

- Expediente:

	* Prioridad
	* Estatus

- Documento de credito:

	* Todos los campos

- Agenda con la lista de expedientes priorizados para consideración del Consejo Directivo.

Modulo Administración 
=====================

Descripción
-----------

Este módulo abarca los procesos de "Liquidación de créditos" y "Liberación de Créditos".
Incluye procedimientos relacionados con la consignación de los documentos notariados por parte de los beneficiarios hasta la entrega del cheque respectivo y con la liberación de los créditos. Procedimientos asociados con las actividades relativas a la liberación de los créditos.

Usuarios
--------

Secretaria Ejecutiva, Presupuesto, Administración, Presidencia.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Certificación de la disponibilidad para liquidación del crédito
         - Administracion
         - Disponibilidad para liquidación del crédito
       * - Creación de tabla de cuentas por cobrar
         - Presupuesto y Administración
         - Tabla de cuentas por cobrar
       * - Creacion de tabla de amortización del crédito
         - Presupuesto y Administración
         - Tabla de amortización del crédito
       * - Creación del estado de cuenta del credito
         - Administracion
         - Estado de cuenta del credito
       * - Generacion de la orden de liquidación
         - Presupuesto y Administracion
         - Orden de liquidación
       * - Generacion de la orden del cheque
         - Presupuesto y Administracion
         - Orden del cheque
       * - Enviar expediente a la unidad de Acompañamiento y Asistencia Técnica
         - Administracion
         - ???
       * - Generación de documento de liquidación del crédito
         - Administración
         - Documento de liquidación del crédito
       * - Cambio del estatus del expediente liberado
         - Administración
         - Estatus del expediente
       * - Registro de la entrega del documento de liberación del crédito
         - Administración
         - ???
       * - Envío del expediente a archivo una vez liberado
         - Administración
         - Registro de envio

Campos modificados de cada entidad
----------------------------------

- Expediente

	* Disponibilidad para liquidación del crédito.
	* Orden de liquidacion y cheque.
	* Estatus

- Estado de cuentas:

	* Todos los campos 
	

Módulo Acompañamiento 
=====================

Descripción
-----------

Este módulo abarca los procesos de "Inspección de Inversiones". Incluye procedimientos asociados a la verificación de la ejecución del plan de inversión por parte del beneficiario.

Usuarios
--------

Acompañamiento y Asistencia Técnica, Archivo, Gerente de Recuperaciones.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Ingreso de los datos asociados a la verificación de la inversión.
         - Acompañamiento
         - Datos asociados a la verificación de la inversión
       * - Recomendación del beneficiario para liquidaciones sucesivas en caso de que pase la inspeccion.
         - Acompañamiento
         - Recomendación del beneficiario para liquidaciones sucesivas.
       * - Ingreso del código del expediente a la lista de Archivo.
         - Acompañamiento
         - Lista de Archivo.
       * - Envio del expediente a la unidad de Recuperaciones.
         - Acompañamiento.
         - Registro de envio.

Campos modificados de cada entidad
----------------------------------

- Expediente:

	* Recomendación del beneficiario para liquidaciones sucesivas.
	* Número de archivo.

- Informe de verificación de la inversión:

	* Todos los campos.
	

Módulo Caja 
===========

Descripción
-----------

Este módulo abarca los procesos de "Pagos". Incluye procedimientos asociados con las actividades de recepción de pagos y actualización de estados de cuenta de beneficiarios o beneficiarias.

Usuarios
--------

Caja, Ejecutivo de cobranza.

Procedimientos
--------------	

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Registro de pago y actualización de estado de cuenta.
         - Ejecutivo de cobranza (caja).
         - Registro de pago.
       * - Generación de recibo de pago y copia para expediente.
         - Ejecutivo de cobranza (caja).
         - Registro de pago.
         - Recibo de pago.
       * - Generación de solicitud de liberación a la unidad de Consultoría Jurídica en caso de último pago (cancelación total del crédito). 
         - Ejecutivo de cobranza (caja).
         - Registro de solicitud de liberacion.
         
Campos modificados de cada entidad
----------------------------------

- Pagos:
	
	* Todos los campos (nuevos registros).


Módulo Recuperaciones 
=====================

Descripción
-----------

Este módulo abarca los procesos de "Gestión de cobranzas". Incluye procedimientos asociados con las actividades de recepción de pagos, actualización de estados de cuenta de beneficiarios y trámites y gestión de recuperación de pagos caídos por parte de los beneficiarios.

Usuarios
--------

Gerente de Recuperaciones, Ejecutivo de cobranza, Administración.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Generación de solicitud de entrevista con un abogado de la unidad de Recuperaciones en caso de estado extrajudicial por mora.
         - Gerente de Recuperaciones..
         - Registro de solicitud de entrevista.
       * - Generar informe de seguimiento al beneficiario. 
         - Ejecutivo de cobranza.
         - Informe de seguimiento.
       * - Consultar estado de cuenta filtrando por estado de morosidad. 
         - Ejecutivo de cobranza.
         - Estado de cuenta
       * - Cambiar estatus del credito a demanda en el caso que lo amerite.
         - Gerente de Recuperaciones.
         - Estatus del credito

Campos modificados de cada entidad
----------------------------------

- Expediente

	* Estatus
	
Módulo Consultoria Jurídica
===========================

Descripción
-----------

Este módulo abarca los procesos asistidos por los consultores jurídicos en: "Liquidación de créditos", "Liberación de créditos" y "Gestión de cobranza". Incluye procedimientos asociados a la redacción de documentos jurídicos y cambio de estatus del expediente.

Usuarios
--------

Consultoría Jurídica.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Generación del documento de liberación del crédito.
         - Consultoría Jurídica.
         - Documento de liberación del crédito.
       * - Generacion de solicitud de reintegro del crédito en caso de que el beneficiario no cumpla con el plan de inversión.
         - Consultoría Jurídica.
         - Registro de solicitud de reintegro del credito.
       * - Liberación de hipotecas o fianzas para expedientes cancelados en su totalidad.
         - Consultoría Jurídica
         - Registro de liberacion de hipotecas.
       * - Cambio de estatus de expediente a liberado.
         - Consultoría Jurídica.
         - Estatus del expediente
       * - Consulta de los expedientes con estatus “demanda” o "liberado"
         - Consultoría Jurídica
         - Todos los datos del expediente seleccionados
       * - Generacion de documento de demanda y documento de liberacion
         - Consultoria Juridica
         - ???
       * - Envio de los expedientes con procesos culminados a Archivo
         - Consultoria Juridica
         - ???


Campos modificados de cada entidad
----------------------------------

- Expediente

	* Estatus
	* Documentos legales asociados

Módulo Archivo
==============

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes", "Inspección de inversiones", "Liberación de créditos", "Gestión de cobranza". Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los distintos departamentos del FOMDES.

Usuarios
--------

Potencial beneficiario, Beneficiario, Solicitante.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Ingreso de nuevos expedientes.
         - Archivólogo.
         - ???
       * - Registro de responsables por expediente solicitado.
         - Archivólogo.
         - Registro de responsables por expediente solicitado.
       * - Consulta por código de expediente.
         - Archivólogo.
         - ???
       * - Consulta lista de expedientes por departamento.
         - Archivólogo.
         - ???

Campos modificados de cada entidad
----------------------------------


Módulo Estadística
==================

Descripción
-----------

Este módulo abarca los procesos que demandan análisis y cálculos estadísticos. Incluye procedimientos de generacion de estadísticas para el apoyo en la toma de decisiones por parte de las gerencias y directiva de FOMDES.

Usuarios
--------

Estadística y Análisis de Riesgo.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - Generar trimestralmente un reporte estadístico de todas las solicitudes ingresadas
         - Analista de credito
         - Solicitudes ingresadas
       * -

Campos modificados de cada entidad
----------------------------------

Módulo Presidencia
==================

Descripción
-----------

Este módulo abarca los procesos en los que interviene la gestión directa del presidente del FOMDES. Incluye procedimientos de evaluación y coordinación con las gerencias para las tomas de decisiones.

Usuarios
--------

Presidente.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados


Campos modificados de cada entidad
----------------------------------

Módulo Beneficiario
===================

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes" y "Recepción de propuestas",  Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los distintos departamentos del FOMDES.

Usuarios
--------

Archivólogo.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Creacion de cuenta de beneficiario
         - Potencial beneficiario, Beneficiario, Solicitante.
         - Datos personales del beneficiario
       * - Edicion de datos personales del beneficiario
         - Potencial beneficiario, Beneficiario, Solicitante.
         - Datos personales del beneficiario
       * - Consulta del estado de mis solicitudes.
         - Potencial beneficiario, Beneficiario, Solicitante.
         - ???
       * - Consulta del estado de mis créditos
         - Beneficiario
         -
       * - Ejecucion de pagos en línea
         - Beneficiario
         - Estado de cuenta
       * - Registro en línea de pagos efectuados mediante transferencia o depósito
         - Beneficiario
         - Estado de cuenta


Módulo Atencion
===============

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes",  Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los distintos departamentos del FOMDES.


Usuarios
--------

Recepcionista.

Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Registro de los datos del solicitante junto con la fecha, hora y destino
         - Recepcionista
         - Datos del beneficiario.
       * - Consulta de la información del estatus de las solicitudes activas
         - Recepcionista
         - Estatus de las solicitudes activas
       * - Consulta de la información del estado de cuenta del beneficiario
         - Recepcionista
         - Estado de cuenta del beneficiario
       * - Generacion de reportes de los visitantes por rango de fecha y cedula
         - Recepcionista
         - Visitantes por rango de fecha y cedula
       * - Generacion de colas por orden de atención y por dependencia
         - Recepcionista
         - ???