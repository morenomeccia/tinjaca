Diseño de modulos
=================

Módulo Solicitudes
==================

Descripción
-----------

Este módulo abarca los procesos de "Recepción de propuestas" y "Recepción y Evaluación de Solicitudes". Incluye procedimientos asociados con la recepción y validación de la propuesta de financiamiento, validación de recaudos para solicitud de crédito y generación del listado de expedientes sugeridos para aprobación de créditos.

Procedimientos de ingreso de datos
----------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Campos accedidos o modificados
       * - Ingreso de datos del solicitante
         - Analista de crédito
         - Todos los datos del solicitante
       * - Ingreso de datos de la propuesta de financiamiento a partir de la planilla consignada y la generacion del código de la misma
         - Analista de crèdito
         - Datos de la propuesta de financiamiento y su codigo
       * - Registro de la viabilidad de la propuesta según las normativas del FOMDES
         - Analista de credito
         - viabilidad de propuesta
       * - Registro del envio de requisitos
         - Analista de credito
         - Chequeo del envio de requisitos
       * - Incluir al solicitante en la lista del “Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario”
         - Analista de credito
         - Codigo de asignacion de taller
       * - Registro de la validez de los requisitos
         - Analista de credito
         - Validez de los requisitos
       * - Creación de expediente con código por sector
         - Analista de credito
         - Codigo de expediente
       * - Envio del expediente a la estación de Análisis Jurídico
         - Analista de credito
         - Estacion del expediente
       * - Registro de la validez legal de la garantía
         - Analista Jurídico
         - Validez legal de garantia
       * - Asignacion del estatus de “CUMPLE”, “NO CUMPLE” o “CUMPLE CONDICIONADO” para las garantías
         - Analista Juridico
         - Estatus de la garantia
       * - Envio del expediente a la estación de Análisis Económico
         - Analisis Juridico
         - Estacion actual del expediente
       * - Registro de la viabilidad económica de la unidad de producción
         - Analista Económico
         - Viabilidad económica de la unidad de producción
       * - Ingreso de fotografías de inspecciones en cada expediente
         - Analista Economico
         - Codigo de las fotografias
       * - Ingreso de los resultados de la inspeccion
         - Analista Economico
         - Datos de la inspeccion
       * - Ingreso de los resultados del avalúo
         - Analista Económico
         - Datos del avaluo
       * - Especificacion de los lapsos de pago del crédito por el beneficiario
         - Analista Economico
         - Lapsos de pago del credito
       * - Enviar el expediente al Gerente de Crédito
         - Analista Economico
         - Estacion del expediente
       * - Inclusión del expediente en la lista para consideración del Consejo Directivo
         - Gerente de crédito
         - Codigo de lista para aprobacion
       * - Asignacion de las tasas de interés por sector, rubro o garantía
         - Gerente de credito
         - Tasas de interés
       * - Asignacion de los montos por sector, rubro o garantía
         - Gerente de credito
         - Monto
       * - Asignacion de los meses de gracia por sector, rubro o garantía
         - Gerente de credito
         - Meses de gracia
       * - Envío de expediente a Secretaría ejecutiva
         - Gerente de crédito
         - Estacion del expediente
	   * - Consulta de expedientes rechazados
         - Gerente de crédito
		 - lista de expedientes rechazados

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida
	   * - Consultar el listado de propuestas de financiamiento que son viables
		 - Analista de credito
		 - Lista de propuestas de financiamiento
	   * - Generacion de la planilla de requisitos e invitación para la asistencia al taller
		 - Analista de credito
		 - Planilla de requisitos, invitacion de asistencia al taller
	   * - Incluir al solicitante en la lista del “Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario”
		 - Analista de credito
		 - Lista de potenciales beneficiarios asignados al taller
	   * - Registro en lista de espera de los potenciales beneficiarios que no asistan al taller
		 - Analista de credito
		 - Lista de espera de potenciales beneficiarios
	   * - Generar informes POA
		 - Analista de credito
		 - Informe POA
       * - Generacion del informe de control previo
         - Analista Jurídico
         - Informe control previo
       * - Generación de rutas para visitar la unidad de producción
         - Analista Económico
         - Lista de rutas
       * - Generacion del informe de inspección con registro fotográfico
         - Analista Economico
         - Informe de inspeccion	 
       * - Ingreso del informe técnico de la garantia
         - Analista Económico
         - Informe tecnico de la garantia
       * - Generacion del informe tecnico
         - Analista Economico
         - Informe tecnico
       * - Generacion de la lista para consideración del Consejo Directivo
         - Gerente de crédito
         - Lista para consideración del Consejo Directivo
       * - Generacion de una lista de rezagados en caso de que se termine el presupuesto pautado
         - Gerente de credito
         - Lista de potenciales beneficiarios
       * - Realizar reportes por municipio, por rubro, por estatus y por rango de fechas
         - Gerente de credito
         - Reporte de expedientes
       * - Distribucion de los analistas económicos por municipios y parroquias para realizar las inspecciones
         - Gerente de credito
         - Lista de distribucion de los analistas economicos.



Módulo Aprobacion
=================

Descripción
-----------

Este módulo abarca los procesos de "Aprobación de Créditos". Incluye los procedimientos asociados con la recepción de la lista de expedientes sugeridos para aprobación de crédito, la elaboración del Documento de Crédito y constitución de la empresa (de requerirse) para cada uno de los beneficiarios(as).

Procedimientos de ingreso de datos
----------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

		* - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
		* - Ingreso de datos del documento de crédito
          - Secretaría Ejecutiva
          - Datos del documento de crédito			
		* - Ingreso de datos del documento de la empresa
          - Secretaría Ejecutiva
          - Datos del documento de la empresa
		* - Asignacion de la prioridad de los expedientes
          - Secretaría Ejecutiva
          - Prioridad
		* - Certificación de disponibilidad presupuestaria y financiera del crédito
          - Jefe de presupuesto
          - Certificación de disponibilidad presupuestaria y financiera del crédito
        * - Registro de aprobacion del documento del crédito
          - Secretaria ejecutiva
		  - Aprobacion del consejo directivo
		* - Asignacion del estatus de la solicitud de crédito en base a lo discutido en el consejo directivo
          - Secretaria ejecutiva
		  - Estatus de la solicitud de credito
        * - Rechazo del crédito en los casos en que los cheques no se retiren o los créditos se rechacen por los beneficiarios
          - Secretaria ejecutiva
		  - Estatus del credito
        * - Envio al gerente de crédito de los expedientes rechazados
          - Secretaria ejecutiva
		  - Estacion del expediente
        * - Envio de los documentos notariados a la gerencia de administración
          - Secretaria ejecutiva
		  - Estacion del expediente
        * - Envio de expedientes liquidados a Acompañamiento
          - Secretaria ejecutiva
		  - Estacion del expediente

Procedimientos de generacion de reportes
----------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida
		* - Generacion del documento de crédito
          - Secretaría Ejecutiva
          - Documento de crédito			
		* - Generacion del documento de la empresa
          - Secretaría Ejecutiva
          - Documento de la empresa
		* - Generacion de la lista de expedientes priorizados
          - Secretaría Ejecutiva
          - Lista de expedientes priorizados
		* - Creación de la convocatoria al consejo directivo
          - Secretaría Ejecutiva
          - Convocatoria al consejo directivo
        * - Creacion de agenda con los casos a ser discutidos en el consejo directivo
          - Secretaria ejecutiva
		  - Agenda de creditos a discutir por el consejo directivo
        * - Impresion de la lista de asistentes al consejo directivo
          - Secretaria ejecutiva
		  - Lista de asistentes al consejo directivo
        * - Creacion del acta del consejo directivo
          - Secretaria ejecutiva
		  - Acta del consejo directivo
        * - Cracion de la minuta del consejo
          - Secretaria ejecutiva
		  - Minuta del consejo
        * - Creacion del documento de crédito para ser notariado por el beneficiario
          - Secretaria ejecutiva
		  - Registro de entrega del documento a al beneficiario


Modulo Administración
=====================

Descripción
-----------

Este módulo abarca los procesos de "Liquidación de créditos" y "Liberación de Créditos".
Incluye procedimientos relacionados con la consignación de los documentos notariados por parte de los beneficiarios hasta la entrega del cheque respectivo y con la liberación de los créditos. Procedimientos asociados con las actividades relativas a la liberación de los créditos.

Procedimientos de ingreso de datos
----------------------------------

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
		  - Registro de envio
		* - Generación de documento de liquidación del crédito
		  - Administración
		  - Documento de liquidación del crédito
		* - Cambio del estatus del expediente liberado
		  - Administración
		  - Estatus del expediente
		* - Registro de la entrega del documento de liberación del crédito
		  - Administración
		  - Registro de entrega
		* - Envío del expediente a archivo una vez liberado
		  - Administración
		  - Registro de envio
        * - Elaboracion de las cuentas por cobrar de los beneficiarios cuyos créditos fueron aprobados
		  - Asesor de Administrativo
  		  - Cuentas por cobrar
        * - Elaboracion de los cheques de los beneficiarios cuyos créditos fueron aprobados
		  - Gerente de administración
  		  - Cheque del credito
        * - Envio de los cheques a presidencia
		  - Gerente de administración
  		  - Registro de envio del cheque 
        * - Creacion la tabla de amortización de los beneficiarios cuyos cheques fueron procesados
		  - Gerente de administración
  		  - Tabla de amortizacion del credito
        * - Consulta de los pagos recibidos
		  - Gerente de administración
  		  - Pagos recibidos
        * - Anulacion de recibos por cheques devueltos y actualizacion del estado de cuenta revirtiendo el pago de las cuotas en el estado de cuenta y recalculando los intereses de las cuotas subsiguientes
		  - Gerente de administración
  		  - Estado de cuenta
        * - Posesion de permisos para modificar o corregir datos en el sistema.
          - Gerente de administracion
          - Datos en el sistema
		* - Registro de los pagos de los beneficiarios o beneficiarias para la cancelación de cuotas de los crédito
		  - Cajero
  		  - Estado de cuenta
        * - Generacion de reporte del ingreso diario de caja
		  - Cajero
  		  - Ingreso diario de caja
        * - Simulacion del recibo
		  - Cajero
  		  - Recibo de pago
        * - Registro de los datos de pago del recibo
		  - Cajero
  		  - Recibo de pago, estado de cuenta
        * - Impresion del recibo de pago
		  - Cajero
  		  - Recibo de pago, estado de cuenta
        * - Verificacion de cuotas vencidas
		  - Cajero
  		  - Cuotas vencidas
        * - Seleccion del expediente correspondiente al crédito al cual se desea pagar
		  - Cajero
  		  - Expediente
        * - Consulta del numero de cuotas vencidas, el total en bolivares en cada cuota y cuotas que estan proximas por vencerse
		  - Cajero
  		  - Cuotas vencidas
        * - Registro de pago a conveniencia del beneficiaro
		  - Cajero
  		  - Registro de pago
        * - Calculo de los intereses de mora correspondientes a la cuota a pagar
		  - Cajero
  		  - Intereses de mora
        * - Cierre de caja y desglose del ingreso total en billetes, monedas, cheques, punto de debito y depósitos
		  - Cajero
  		  - Ingreso total
        * - Creacion de un reporte con el total de personas atendidas diariamente
		  - Cajero
  		  - Reporte de beneficiarios

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Acompañamiento
=====================

Descripción
-----------

Este módulo abarca los procesos de "Inspección de Inversiones". Incluye procedimientos asociados a la verificación de la ejecución del plan de inversión por parte del beneficiario.


Procedimientos de ingreso de datos
----------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Ingreso de los datos asociados a la verificación de la inversión
         - Jefe de acompañamiento
         - Datos asociados a la verificación de la inversión
       * - Recomendación del beneficiario para liquidaciones sucesivas en caso de que pase la inspeccion
         - Jefe de acompañamiento
         - Recomendación del beneficiario para liquidaciones sucesivas.
       * - Ingreso del código del expediente a la lista de Archivo.
         - Jefe de acompañamiento
         - Lista de Archivo
       * - Envio del expediente a la unidad de Recuperaciones
         - Jefe de acompañamiento
         - Registro de envio
       * - Registro de la cantidad de empleos generados directos e indirectos por cada crédito
         - Jefe de acompañamiento
         - Registro de la cantidad de empleos
       * - Notificacion con la lista de créditos liquidados desde administración
         - Jefe de acompañamiento
       * - Consulta de la información del beneficiario
         - Jefe de acompañamiento
		 - Datos del beneficiario
       * - Consulta de la información del crédito
         - Jefe de acompañamiento
		 - Datos del crédito
       * - Consultar el apodo del beneficiario
         - Jefe de acompañamiento
		 - Apodo del beneficiario
       * - Llevar un registro de los beneficiarios y beneficiarias atendidos por fecha y hora
         - Jefe de acompañamiento
		 - Registro de beneficiarios atendidos.
       * - Generacion de informe de acompañamiento          
		 - Jefe de acompañamiento
		 - Datos del informe de acompañamiento.
       * - Generacion de reportes con formato para las minuta
		 - Jefe de acompañamiento
		 - plantilla de la minuta
       * - Guardado de fotografías de las inspecciones          
		 - Jefe de acompañamiento
		 - Fotografias de las inspecciones
       * - Generacion de notas de visitas de inspección, atención en oficina o llamadas telefónicas          
		 - Jefe de acompañamiento
		 - Plantilla de las notas
       * - Consulta de notas de visitas de inspección, atención en oficina o llamadas telefónicas
		 - Jefe de acompañamiento
		 - Plantilla de las notas
       * - Edicion de los datos del beneficiario.         
		 - Jefe de acompañamiento
		 - Datos del beneficiario
       * - Generacion de notificación de acompañamiento          
		 - Jefe de acompañamiento
		 - Plantilla de notificación de acompañamiento 
       * - Generacion de minuta de atención en oficina para las declaraciones de los beneficiarios          
		 - Jefe de acompañamiento
		 - Plantilla de la minuta de atencion
       * - Registro de los casos donde las visitas no son atendidas
		 - Jefe de acompañamiento
		 - Registro de los casos donde las visitas no son atendidas
       * - Generar formato de charla          
		 - Jefe de acompañamiento
		 - Plantilla de la charla
       * - Consulta de los depósitos de las cuotas
         - Jefe d  acompañamiento
         - Depositos de cuotas
       * - Envio del expediente a otras estaciones junto con nota explicativa
		 - Jefe de acompañamiento
		 - Registro de envio.

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida	

Módulo Caja
===========

Descripción
-----------

Este módulo abarca los procesos de "Pagos". Incluye procedimientos asociados con las actividades de recepción de pagos y actualización de estados de cuenta de beneficiarios o beneficiarias.

Procedimientos de ingreso de datos
----------------------------------

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

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Recuperaciones 
=====================

Descripción
-----------

Este módulo abarca los procesos de "Gestión de cobranzas". Incluye procedimientos asociados con las actividades de recepción de pagos, actualización de estados de cuenta de beneficiarios y trámites y gestión de recuperación de pagos caídos por parte de los beneficiarios.


Procedimientos
--------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Generacion de lista con los beneficiarios que se deben visitar por fecha, municipio y sectores en el caso que existan cuotas vencidas
         - Ejecutivo de cobranza
         - Cuotas vencidas, lista de beneficiarios
       * - Filtrado de estados de cuentas por cédula y expediente
         - Ejecutivo de cobranza
         - Estado de cuentas
       * - Acceso a los estados de cuenta desde la cartera de cobranza
         - Ejecutivo de cobranza
         - Estado de cuenta
       * - Consulta del estado de cuenta del beneficiario o beneficiaria
         - Ejecutivo de cobranza
         - Estado de cuenta
       * - Consulta de los depósitos realizados por el beneficiario o beneficiaria
         - Ejecutivo de cobranza
         - Depositos
       * - Generacion del reporte del ingreso diario de caja
         - Ejecutivo de cobranza
         - Reporte del ingreso diario de caja
       * - Registro de los beneficiarios atendidos diariamente
         - Ejecutivo de cobranza
         - Registro de los beneficiarios atendidos diariamente
       * - Cambio del estado del beneficiario según su morosidad
         - Gerente de recuperaciones
         - Estado de morosidad
       * - Creacion de carteras de cobranza
         - Ejecutivo de cobranza
         - Carteras de cobranza
       * - Establecimiento de metas diarias de recuperación
         - Ejecutivo de cobranza
         - Metas diarias de recuperación
       * - Creacion de notas con los acuerdos e información suministrada por el beneficiario
         - Ejecutivo de cobranza
         - Notas con acuerdos
       * - Consulta de notas con los acuerdos e información suministrada por el beneficiario
         - Ejecutivo de cobranza
         - Notas con acuerdos
       * - Creacion de recordatorios con las fechas de compromiso de pago del beneficiario
         - Ejecutivo de cobranza
         - Recordatorios con las fechas de compromiso de pago
       * - Ordenamiento de los expedientes por niveles de morosidad en las carteras
         - Ejecutivo de cobranza
         - Nivel de morosidad del expediente
       * - Verificacion de la validez de los depósitos bancarios para los pagos
         - Ejecutivo de cobranza
         - Validez de los depósitos bancarios
       * - Generación de solicitud de entrevista con un abogado de la unidad de Recuperaciones en caso de estado extrajudicial por mora.
         - Gerente de Recuperaciones.
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
       * - Posesion de permisos para modificar o corregir datos en el sistema.
         - Gerente de Recuperaciones
         - Datos en el sistema

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Consultoria Jurídica
===========================

Descripción
-----------

Este módulo abarca los procesos asistidos por los consultores jurídicos en: "Liquidación de créditos", "Liberación de créditos" y "Gestión de cobranza". Incluye procedimientos asociados a la redacción de documentos jurídicos y cambio de estatus del expediente.


Procedimientos de ingreso de datos
----------------------------------

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
       * - Generacion de documento de demanda
         - Consultoria Juridica
         - Documento de demanda
       * - Generacion de documento de liberacion
         - Consultoria Juridica
         - Documento de demanda
       * - Envio de los expedientes con procesos culminados a Archivo
         - Consultoria Juridica
         - Registro de envio

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Archivo
==============

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes", "Inspección de inversiones", "Liberación de créditos", "Gestión de cobranza". Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los distintos departamentos del FOMDES.


Procedimientos de ingreso de datos
----------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Ingreso de nuevos expedientes.
         - Archivólogo.
         - Codigo de expediente
       * - Registro de responsables por expediente solicitado.
         - Archivólogo.
         - Lista de responsables por expediente solicitado.
       * - Registro de historial con detalle de movimientos de los expedientes
         - Archivologo
         - Historial de movimiento del expediente
       * - Consulta por código de expediente.
         - Archivólogo.
         - Codigo de expediente
       * - Consulta lista de expedientes por departamento.
         - Archivólogo.
         - Lista de codigos de expediente
       * - Envio de los expedientes a diferentes dependencias
         - Archivologo
         - Registro de envio

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Estadística
==================

Descripción
-----------

Este módulo abarca los procesos que demandan análisis y cálculos estadísticos. Incluye procedimientos de generacion de estadísticas para el apoyo en la toma de decisiones por parte de las gerencias y directiva de FOMDES.


Procedimientos de ingreso de datos
----------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1


       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Generacion trimestral un reporte estadístico de todas las solicitudes ingresadas
         - Analista de credito
         - Solicitudes ingresadas
       * - Generacion de factura con los datos del beneficiario, monto aprobado, tasas de interés y cuotas
    	 - Jefe del departamento de estadística y auditoria de cobranza
		 - Factura de cobranza.
	   * - Generacion de reporte desglosado por niveles de morosidad
         - Jefe del departamento de estadística y auditoría de cobranza
    	 - Generacion de reporte
       * - Registro de exoneracion en el cobro del crédito
         - Jefe del departamento de estadística y auditoría de cobranza
		 - Registro de exoneracion en el cobro del crédito
       * - Agrupa en los reportes estadísticos de las solicitudes por sector dentro de cada unicipio, con el conteo y suma de los montos solicitados, y las totalizaciones.
         - Gerente de credito
         - Reportes estadísticos de las solicitudes

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Presidencia
==================

Descripción
-----------

Este módulo abarca los procesos en los que interviene la gestión directa del presidente del FOMDES. Incluye procedimientos de evaluación y coordinación con las gerencias para las tomas de decisiones.


Procedimientos de ingreso de datos
----------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Procedimiento
         - | Responsable
         - | Datos accedidos o modificados
       * - Monitoreo del ingreso diario de caja y cumplimiento de metas
         - Presidente
         - Ingreso diario de caja
       * - Revision y firma de los cheques
         - Presidente
         - Cheques
       * - Envio de los cheques firmados a secretaria ejecutiva
         - Presidente
         - Registro de envio
       * - Revision de montos, intereses y plazos de las solicitudes de crédito
         - Presidente
         - Solicitudes de potenciales beneficiarios
       * - Evaluacion y valoracion de indicadores clave de rendimiento y variables políticas
         - Presidente
         - Indicadores clave de rendimiento
        * - Consulta del ingreso diario de caja y metas diarias
		  - Presidente
		  - Ingreso diario de caja
        * - Consulta de montos, intereses y plazos de las solicitudes de crédito
		  - Presidente
          - Montos, intereses y plazos de las solicitudes de crédito
        * - Generacion y consulta de indicadores clave de rendimiento y variables políticas
          - Presidente
		  - Indicadores clave de rendimiento



Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Beneficiario
===================

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes" y "Recepción de propuestas",  Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los distintos departamentos del FOMDES.


Procedimientos de ingreso de datos
----------------------------------

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
         - Estatus de solicitud
       * - Consulta del estado de mis créditos
         - Beneficiario
         - Estatus de expediente
       * - Ejecucion de pagos en línea
         - Beneficiario
         - Estado de cuenta
       * - Registro en línea de pagos efectuados mediante transferencia o depósito
         - Beneficiario
         - Estado de cuenta

Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida

Módulo Atencion
===============

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes",  Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los distintos departamentos del FOMDES.


Procedimientos de ingreso de datos
----------------------------------

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
         - Lista de beneficiarios


Procedimiento de generacion de reportes
---------------------------------------

  .. list-table::
       :widths: 40 70 40
       :header-rows: 1

	   * - | Procedimiento
		 - | Responsable
		 - | Reporte de salida


