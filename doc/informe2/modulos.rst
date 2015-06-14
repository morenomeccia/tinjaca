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

- Ingreso de datos del solicitante. Usuario responsable: Analista de crédito.
- Ingreso de datos de la propuesta de financiamiento desde la planilla consignada y la generacion del código de la misma.  Usuario responsable: Analista de crèdito.
- Registro de la viabilidad de la propuesta según las normativas del FOMDES. Usuario responsable: Analista de credito.
- Incluir al solicitante en la lista del “Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario”. Uusuario responsable: Analista de credito. 
- Registro de la validez de los requisitos. Usuario responsable: Analista de credito.
- Creación de expediente con código por sector. Usuario responsable: Analista de credito.
- Registro de la validez legal de la garantía. Usuario responsable: Analista Jurídico.
- Generación de rutas para visitar la unidad de producción. Usuario responsable: Analista Económico.
- Registro de la viabilidad económica de la unidad de producción. Usuario responsable: Analista Económico.
- Ingreso de los resultados de la inspección. Usuario responsable: Analista Económico.
- Ingreso de los resultados del avalúo. Usuario responsable: Analista Económico.
- Ingreso del informe técnico de la garantia. Usuario responsable: Analista Económico.
- Inclusión del expediente en la lista para consideración del Consejo Directivo. Usuario responsable: Gerente de crédito.
- Envío de expediente a la Secretaría ejecutiva. Usuario responsable: Gerente de crédito.

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

- Ordenamiento de la lista de expedientes según sus prioridades. Usuario responsable: Secretaría Ejecutiva.
- Registro de la certificación de disponibilidad presupuestaria y financiera del crédito. Usuario responsable: Secretaría Ejecutiva.
- Creación de la convocatoria al consejo directivo con agenda de expedientes priorizados. Usuario responsable: Secretaría Ejecutiva.
- Ingreso del documento de crédito al expediente. Usuario responsable: Secretaría Ejecutiva.
- Ingreso del documento de documento de la empresa. Usuario responsable: Secretaría Ejecutiva.

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

- Certificación de la disponibilidad para liquidación del crédito. Usuario responsable: Administracion. 
- Creación de tabla de cuentas por cobrar y tabla de amortización del crédito. Usuario responsable: Presupuesto y Administración.  
- Creación del estado de cuenta del credito. Usuario responsable: Administracion. 
- Generacion de la orden de liquidación y del cheque. Usuario responsable: Presupuesto y Administracion.
- Enviar expediente a la unidad de Acompañamiento y Asistencia Técnica. Usuario responsable: Administracion.
- Generación de documento de liquidación del crédito. Usuario responsable: Administración.
- Cambio del estatus del expediente liberado. Usuario responsable: Administración.
- Registro de la entrega del documento de liberación del crédito. Usuario responsable: Administración. 
- Envío del expediente a archivo una vez liberado. Usuario responsable: Administración. 

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

- Ingreso de los datos asociados a la verificación de la inversión. Usuarios responsables: Acompañamiento.
- Recomendación del beneficiario para liquidaciones sucesivas en caso de que pase la inspeccion. Usuarios responsables: Acompañamiento. 
- Ingreso del código del expediente a la lista de Archivo. Usuarios responsables: Acompañamiento.
- Enviar expediente a la unidad de Recuperaciones. Usuarios responsables: Acompañamiento.

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

- Registro de pago y actualización de estado de cuenta. Usuario responsable: Caja, Ejecutivo de cobranza.
- Generación de recibo de pago y copia para expediente. Usuario responsable: Caja, Ejecutivo de cobranza.
- Generación de solicitud de liberación a la unidad de Consultoría Jurídica en caso de último pago (cancelación total del crédito). Usuario responsable: Caja, Ejecutivo de cobranza.

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

- Generación de solicitud de entrevista con un abogado de la unidad de Recuperaciones en caso de estado extrajudicial por mora . Usuario responsable: Gerente de Recuperaciones.
- Generar informe de seguimiento al beneficiario. Usuario responsable: Ejecutivo de cobranza.
- Consultar estado de cuenta filtrando por estado de morosidad. Usuario responsable: Ejecutivo de cobranza.
- Cambiar estatus a demanda en el caso que lo amerite. Usuario responsable: Gerente de Recuperaciones.

Campos modificados de cada entidad
----------------------------------

- Expediente

	* Estatus
	
Módulo Jurídico
===============

Descripción
-----------

Este módulo abarca los procesos asistidos por los consultores jurídicos en: "Liquidación de créditos", "Liberación de créditos" y "Gestión de cobranza". Incluye procedimientos asociados a la redacción de documentos jurídicos y cambio de estatus del expediente.

Usuarios
--------

Consultoría Jurídica.

Procedimientos
--------------

- Generación del documento de liberación del crédito. Usuario responsable: Consultoría Jurídica.
- Generacion de solicitud de reintegro del crédito en caso de que el beneficiario no cumpla con el plan de inversión. Usuario responsable: Consultoría Jurídica.
- Liberación de hipotecas o fianzas para expedientes cancelados en su totalidad. Usuario responsable: Consultoría Jurídica.
- Cambio de estatus de expediente liberado. Usuario responsable: Consultoría Jurídica.

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

Archivólogo.

Procedimientos
--------------

- Ingreso de nuevos expedientes. Usuario responsable: Archivólogo.
- Registro de responsables por expediente solicitado. Usuario responsable: Archivólogo.
- Consulta por código de expediente. Usuario responsable: Archivólogo.
- Consulta lista de expedientes por departamento. Usuario responsable: Archivólogo.

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


Campos modificados de cada entidad
----------------------------------
