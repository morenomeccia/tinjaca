Diseño de modulos
=================

Modulo "Recepción y Evaluación de Solicitudes" 
==============================================

Descripción: Procedimientos asociados con la recepcion y validacion de la propuesta de financiamiento, validacion de recaudos para solicitud de crédito y generación del listado de expedientes sugeridos para aprobación de créditos.
Dependencia responsable: Gerencia de Crédito
Unidad(es) Ejecutora(s): Usuario, Información de Crédito, Estadística y Evaluación de Riesgos, Análisis Jurídico, Análisis Económico.

Procedimientos
--------------

- Ingreso de datos del solicitante.
- Ingreso de datos de la propuesta de financiamiento y generacion del código de la misma (usuario responsable: Analista de credito).
- Asignacion de la viabilidad de la propuesta segun las normativas del FOMDES (usuario responsable: Analista de credito).
- Incluir al solicitante en la lista del “Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario” (usuario responsable: Analista de credito). 
- Asignacion de la validez de los requisitos (usuario responsable: Analista de credito).
- Creacion de expediente con codigo por sector (usuario responsable: Analista de credito).
- Asignacion de la validez legal de la garantía (usuario responsable: Analista Jurídico).
- Generacion de rutas para visitar la unidad de produccion (usuario responsable: Analista Económico).
- Asignacion de la viabilidad económica de la unidad de producción (usuario responsable: Analista Económico).
- Ingreso de los resultados de la inspección (usuario responsable: Analista Económico).
- Ingreso de los resultados del avalúo (usuario responsable: Analista Económico).
- Ingreso del informe técnico de la garantia (usuario responsable: Analista Económico).
- Incluir el expediente en la lista para consideración del Consejo Directivo 
- Enviar expediente a la Secretaria ejecutiva (usuario responsable: Gerente de credito).

Campos modificados de cada entidad
----------------------------------

- Solicitante: 

	* Todos los campos del Solicitante

- Potencial beneficiario:

	* Todos los campos del Potencial beneficiario
	
- beneficiario:

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

Modulo "Aprobación de Créditos" 
===============================

Descripción: Procedimientos asociados con la recepción de la lista de expedientes sugeridos para aprobación de crédito, la elaboración del Documento de Crédito y constitución de la empresa (de requerirse) para cada uno de los beneficiarios(as).
Dependencia responsable: Presidencia
Unidad(es) Ejecutora(s): Secretaría Ejecutiva, Presupuesto, Consejo Directivo

Procedimientos
--------------

- Ordenado de la lista de expedientes (usuario responsable: Secretaría Ejecutiva): este procedimiento consiste en la modificacion de un campo que representa la prioridad del expediente. 
- Certificado de la disponibilidad presupuestaria y financiera del credito (usuario responsable: Secretaría Ejecutiva): este procedimiento consiste en la modificacion de un campo que representa la disponibilidad presupuestaria y financiera del credito.
- Creacion de la convocatoria al consejo directivo con agenda de expedientes priorizados (usuario responsable: Secretaría Ejecutiva).
- Ingreso del documento de crédito (o documento de la empresa) al expediente (usuario responsable: Secretaría Ejecutiva): este procedimiento consiste en el llenado de uno o mas campos o de un archivo que este asociado al expediente y que represente o identifique el documento de credito. 

Campos modificados de cada entidad
----------------------------------

- Expediente:

	* Prioridad
	* Estatus

- Documento de credito:

	* Todos los campos

- Agenda con la lista de expedientes priorizados para consideración del Consejo Directivo.

Modulo "Liquidación y liberacion de Créditos" 
=============================================

Descripción: Procedimientos relacionados con la consignación de los documentos notariados por parte de los beneficiarios hasta la entrega del cheque respectivo y con la liberación de los créditos.
Dependencia responsable: Administración y Finanzas
Unidad(es) Ejecutora(s): Secretaria Ejecutiva, Presupuesto, Administración, Presidencia, Consultoría Jurídica.

Procedimientos
--------------

- Certificado de la disponibilidad para liquidación del crédito (usuario responsable: Administracion): este procedimiento consiste en la modificacion de un campo que representa la disponibilidad para liquidación del crédito.
- Creacion de tabla de cuentas por cobrar y tabla de amortización del credito (usuario responsable: Administracion).  
- Creacion del estado de cuenta del credito.
- Generacion de la orden de liquidación y del cheque.
- Enviar expediente a la unidad de Acompañamiento y Asistencia Técnica.
- Generar documento de liquidación del crédito.

Campos modificados de cada entidad
----------------------------------

- Expediente

	* Disponibilidad para liquidación del crédito.
	* Orden de liquidacion y cheque.

- Estado de cuentas:

	* Todos los campos 
	
Modulo "Inspección de Inversiones" 
==================================

Descripción: Procedimientos asociados a la verificación de la ejecución del plan de inversión por parte del beneficiario.
Dependencia responsable: Gerencia de Crédito y Gerencia de Recuperaciones.
Unidad(es) Ejecutora(s): Acompañamiento y Asistencia Técnica, Consultoría Jurídica, Archivo.

Procedimientos
--------------

- Ingreso de los datos asociados a la verificación de la inversión.
- Recomendación del beneficiario para liquidaciones sucesivas en caso de que pase la inspeccion: Asignacion de un campo que representa la recomendacion del beneficiario para liquidaciones sucesivas.  
- Generacion de solicitud de reintegro del crédito en caso de que el beneficiario no cumpla con el plan de inversión.
- Ingreso del código del expediente a la lista de Archivo.
- Enviar expediente a la unidad de Recuperaciones.

Entidades modificadas
---------------------

- Expediente

Campos modificados de cada entidad
----------------------------------

- Expediente:

	* Recomendación del beneficiario para liquidaciones sucesivas (un campo que dice si el beneficiario se recomienda o no para futuras liquidaciones).
	* Numero de archivo.

- Informe de verificación de la inversión:

	* Todos los campos.
	
Modulo "Caja" 
============

Descripción: Procedimientos asociados con las actividades de recepción de pagos y actualización de estados de cuenta de
beneficiarios(as)
Dependencia responsable: Administración y Finanzas
Unidad(es) Ejecutora(s): Caja, Consultoría Juridica

Procedimientos
--------------	

- Registrar pago y actualizar estado de cuenta. 
- Generar recibo de pago y guardar copia en expediente.
- En caso de ultimo pago (cancelación total del crédito): generar solicitud de liberación a la unidad de Consultoría Jurídica.

Campos modificados de cada entidad
----------------------------------

- Pagos:
	
	* Todos los campos (nuevos registros)


Modulo "Recuperaciones" 
=======================

Descripción: Procedimientos asociados con las actividades de recepción de pagos, actualización de estados de cuenta de
beneficiarios y trámite y gestión de recuperación de pagos caídos por parte de beneficiarios.
Dependencia responsable: Administración y Finanzas, gerencia de Recuperaciones.
Unidad(es) Ejecutora(s): Caja, Consultoría Juridica, Recuperaciones.

Procedimientos
--------------

- En caso de estado extrajudicial por mora: generar solicitud de entrevista con un abogado de la unidad de Recuperaciones.
- Generar informe de seguimiento al beneficiario.
- Consultar estado de cuenta. Este procedimiento muestra una letra que identifica el estado de cuenta actual de modo que el usuario  de la unidad de Recuperaciones pueda tomar las acciones respectivas.
- Cambiar estatus a demanda en el caso que lo amerite.

Campos modificados de cada entidad
----------------------------------

- Expediente

	* Estatus
	
Modulo "Liberacion del credito" 
===============================

Descripción: Procedimientos asociados con las actividades relativas a la liberación de los créditos.

Procedimientos
--------------

- Generacion del documento de liberación del crédito.
- Cambio del estatus del expediente.
- Registro de la entrega del documento de liberación del crédito.
- Envio del expediente a archivo.

Campos modificados de cada entidad
----------------------------------

- Expediente

	* Estatus
	
