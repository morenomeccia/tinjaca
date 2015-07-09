*****************
Diseño de Módulos
*****************

El sistema Tinjacá esta diseñado por módulos que agrupan funcionalidades asociadas a los distintos procesos descritos en
el Informe de Requerimientos y Nudos Críticos de los Sistemas Actuales. En esta sección se presenta una descripción de
cada uno de los módulos planteados, los procedimientos que se ejecutan, los datos accedidos o modificados, y los
reportes generados.

Asimismo, el sistema contempla diferentes perfiles de usuario que se relacionan directamente con el rol que desempeña la
persona dentro del FOMDES. Los perfiles de usuario definen tanto los permisos como las restricciones para cada módulo.

Cada cuenta de usuario tendrá asociado un perfil de usuario, de modo que tanto el acceso a los datos del sistema como
los menús e interfaz, dependa de cada perfil de usuario según la sesión iniciada por los funcionarios de FOMDES como
usuarios del sistema Tinjacá. De esta manera las funciones permitidas estarán condicionadas y limitadas por el mismo
sistema de forma predeterminada.

Por otro lado, también existen perfiles especiales con tipos de usuario avanzados dentro del sistema, llamados
super-usuarios, que tienen capacidades superiores en la administración del sistema, dentro de un ámbito específico.


.. index:: !Módulo Propuestas, Propuestas, Solicitantes, Talleres

Módulo Propuestas
=================

Descripción
-----------

Este módulo abarca los procesos de "Recepción de propuestas". Incluye procedimientos asociados con la recepción y validación de la propuesta de financiamiento y la inclusión de los solicitantes a las listas de los talleres de inducción.

Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Campos accedidos o modificados
        * - Ingreso de datos del solicitante
          - Analista de crédito
          - Datos del solicitante
        * - Ingreso de datos de la propuesta de financiamiento a partir de la planilla consignada
          - Analista de crédito
          - Datos de la unidad de producción, actividad productiva, plan de inversión, avalistas, garantías
        * - Generación del código de propuesta
          - Analista de crédito
          - Código de la propuesta de financiamiento
        * - Registro de la viabilidad de la propuesta según las normativas del FOMDES
          - Analista de crédito
          - Viabilidad de propuesta
        * - Registro del envío de requisitos
          - Analista de crédito
          - Chequeo del envío de requisitos
        * - Incluir al solicitante en la lista del taller de inducción
          - Analista de crédito
          - Código de asignación de taller

.. index:: !Reportes Propuestas

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Consultar el listado de propuestas de financiamiento que son viables
          - Analista de crédito
          - Lista de propuestas de financiamiento
        * - Generación de la planilla de requisitos
          - Analista de crédito
          - Planilla de requisitos
        * - Generación de la invitación para la asistencia al taller
          - Analista de crédito
          - Invitación de asistencia al taller
        * - Generación de la lista de convocados al taller de inducción
          - Analista de crédito
          - Lista de potenciales beneficiarios asignados al taller
        * - Generación de la lista de espera de los potenciales beneficiarios que no asistan al taller
          - Analista de crédito
          - Lista de espera de potenciales beneficiarios

.. index:: !Módulo Solicitudes, Requisitos, Control Previo, Avalúo, Inspección, Créditos

Módulo Solicitudes
==================

Descripción
-----------

Este módulo abarca los procesos de "Recepción y Evaluación de Solicitudes". Incluye procedimientos asociados con la recepción y validación de recaudos para solicitud de crédito y generación del listado de expedientes sugeridos para aprobación de créditos.

Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Campos accedidos o modificados
        * - Registro de la validez de los requisitos
          - Analista de crédito
          - Validez de los requisitos
        * - Creación de expediente con código por sector
          - Analista de crédito
          - Código de expediente
        * - Envío del expediente a la estación de Análisis Jurídico
          - Analista de crédito
          - Estación del expediente
        * - Registro de la validez legal de la garantía
          - Analista Jurídico
          - Validez legal de garantía
        * - Asignación del estatus de “CUMPLE”, “NO CUMPLE” o “CUMPLE CONDICIONADO” para las garantías
          - Analista Jurídico
          - Estatus de la garantía
        * - Envío del expediente a la estación de Análisis Económico
          - Análisis Jurídico
          - Estación actual del expediente


.. index:: !Módulo Solicitudes, Inspecciones, Consejo Directivo, Presupuestos

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Campos accedidos o modificados
        * - Registro de la viabilidad económica de la unidad de producción
          - Analista Económico
          - Viabilidad económica de la unidad de producción
        * - Ingreso de fotografías de inspecciones en cada expediente
          - Analista Económico
          - Código de las fotografías
        * - Ingreso de los resultados de la inspección
          - Analista Económico
          - Datos de la inspección
        * - Ingreso de los resultados del avalúo
          - Analista Económico
          - Datos del avalúo
        * - Especificación de los lapsos de pago del crédito por el beneficiario
          - Analista Económico
          - Lapsos de pago del crédito
        * - Enviar el expediente al Gerente de Crédito
          - Analista Económico
          - Estación del expediente
        * - Inclusión del expediente en la lista para consideración del Consejo Directivo
          - Gerente de crédito
          - Código de lista para aprobación
        * - Asignación de las tasas de interés por sector, rubro o garantía
          - Gerente de crédito
          - Tasas de interés
        * - Asignación de los montos por sector, rubro o garantía
          - Gerente de crédito
          - Monto
        * - Asignación de los meses de gracia por sector, rubro o garantía
          - Gerente de crédito
          - Meses de gracia
        * - Envío de expediente a Secretaría ejecutiva
          - Gerente de crédito
          - Estación del expediente
        * - Consulta de expedientes rechazados
          - Gerente de crédito
          - lista de expedientes rechazados
        * - Edición de datos personales del beneficiario
          - Analista económico, analista de crédito
          - Datos personales del beneficiario

.. index:: !Reportes Solicitudes

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Consultar propuestas de financiamiento viables
          - Analista de crédito
          - Información de propuesta de financiamiento
        * - Generar informes POA
          - Analista de crédito
          - Informe POA
        * - Generación del informe de control previo
          - Analista Jurídico
          - Informe control previo
        * - Generación de rutas para visitar la unidad de producción
          - Analista Económico
          - Lista de rutas
        * - Generación del informe de inspección con registro fotográfico
          - Analista Económico
          - Informe de inspección    
        * - Ingreso del informe técnico de la garantía
          - Analista Económico
          - Informe técnico de la garantía
        * - Generación del informe técnico
          - Analista Económico
          - Informe técnico
        * - Generación de la lista para consideración del Consejo Directivo
          - Gerente de crédito
          - Lista para consideración del Consejo Directivo
        * - Generación de una lista de rezagados en caso de que se termine el presupuesto pautado
          - Gerente de crédito
          - Lista de potenciales beneficiarios
        * - Realizar reportes por municipio, por rubro, por estatus y por rango de fechas
          - Gerente de crédito
          - Reporte de expedientes
        * - Distribución de los analistas económicos por municipios y parroquias para realizar las inspecciones
          - Gerente de crédito
          - Lista de distribución de los analistas económicos.

.. index:: !Módulo Aprobación, Secretaría Ejecutiva, Presupuestos, Liquidaciones, Acompañamiento, Recuperaciones

Módulo Aprobación
=================

Descripción
-----------

Este módulo abarca los procesos de "Aprobación de Créditos". Incluye los procedimientos asociados con la recepción de la
lista de expedientes sugeridos para aprobación de crédito, la elaboración del Documento de Crédito y constitución de la
empresa (de requerirse) para cada uno de los beneficiarios(as).

Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
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
        * - Asignación de la prioridad de los expedientes
          - Secretaría Ejecutiva
          - Prioridad
        * - Certificación de disponibilidad presupuestaria y financiera del crédito
          - Jefe de presupuesto
          - Certificación de disponibilidad presupuestaria y financiera del crédito
        * - Registro de aprobación del documento del crédito
          - Secretaria ejecutiva
          - Aprobación del consejo directivo
        * - Asignación del estatus de la solicitud de crédito en base a lo discutido en el consejo directivo
          - Secretaria ejecutiva
          - Estatus de la solicitud de crédito
        * - Rechazo del crédito en los casos en que los cheques no se retiren o los créditos se rechacen por los beneficiarios
          - Secretaria ejecutiva
          - Estatus del crédito
        * - Envío al gerente de crédito de los expedientes rechazados
          - Secretaria ejecutiva
          - Estación del expediente
        * - Envío de los documentos notariados a la gerencia de administración
          - Secretaria ejecutiva
          - Estación del expediente
        * - Envío de expedientes liquidados a Acompañamiento y Recuperaciones
          - Secretaria ejecutiva
          - Estación del expediente

.. index:: !Reportes Aprobación

Procedimientos de generación de reportes
----------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Generación del documento de crédito
          - Secretaría Ejecutiva
          - Documento de crédito            
        * - Generación del documento de la empresa
          - Secretaría Ejecutiva
          - Documento de la empresa
        * - Creación de la convocatoria al consejo directivo
          - Secretaría Ejecutiva
          - Convocatoria al consejo directivo
        * - Creación de agenda con los casos a ser discutidos en el consejo directivo
          - Secretaria ejecutiva
          - Agenda de créditos a discutir por el consejo directivo
        * - Impresión de la lista de asistentes al consejo directivo
          - Secretaria ejecutiva
          - Lista de asistentes al consejo directivo
        * - Creación del acta del consejo directivo
          - Secretaria ejecutiva
          - Acta del consejo directivo
        * - Creación de la minuta del consejo
          - Secretaria ejecutiva
          - Minuta del consejo
        * - Creación del documento de crédito para ser notariado por el beneficiario
          - Secretaria ejecutiva
          - Registro de entrega del documento a al beneficiario

.. index:: !Módulo Administración, Liquidaciones, Pagos, Recuperaciones

Modulo Administración
=====================

Descripción
-----------

Este módulo abarca los procesos de "Liquidación de créditos" y "Liberación de Créditos". Incluye procedimientos
relacionados con la consignación de los documentos notariados por parte de los beneficiarios hasta la entrega del cheque
respectivo y con la liberación de los créditos.

Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Certificación de la disponibilidad para liquidación del crédito
          - Analista Financiera
          - Disponibilidad para liquidación del crédito
        * - Consulta de tabla de cuentas por cobrar
          - Analista Financiera
          - Tabla de cuentas por cobrar
        * - Enviar expediente a la unidad de Acompañamiento y Asistencia Técnica
          - Analista Financiera
          - Estación del expediente
        * - Enviar documento a consultaría jurídica para liberación del documento
          - Analista Financiera
          - Estatus del expediente
        * - Registro de la entrega del documento de liberación del crédito
          - Secretaria ejecutiva
          - Registro de entrega
        * - Envío del expediente a archivo una vez liberado
          - Analista Financiera
          - Estación del expediente
        * - Envío de los cheques a presidencia
          - Gerente de administración
          - Registro de envío del cheque 
        * - Anulación de recibos por cheques devueltos y recalculando los intereses de las cuotas subsiguientes
          - Analista Financiera
          - Estado de cuenta

.. index:: !Reportes Administración

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Creación de tabla de amortización del crédito
          - Analista Financiera
          - Tabla de amortización del crédito
        * - Creación del estado de cuenta del crédito
          - Asesor Administrativo
          - Estado de cuenta del crédito
        * - Generación de la orden de liquidación
          - Asesor Administrativo
          - Orden de liquidación
        * - Generación de la orden del cheque
          - Asesor Administrativo
          - Orden del cheque
        * - Generación del documento de liquidación del crédito
          - Jefe de presupuesto
          - Documento de liquidación del crédito
        * - Elaboración de los cheques de los beneficiarios cuyos créditos fueron aprobados
          - Gerente de administración
          - Cheque del crédito
        * - Consulta de los pagos recibidos
          - Analista Financiera
          - Pagos recibidos

.. index:: !Módulo Acompañamiento, Visitas Acompañamiento, Rutas Acompañamiento

Módulo Acompañamiento
=====================

Descripción
-----------

Este módulo abarca los procesos de "Inspección de Inversiones". Incluye procedimientos asociados a la verificación de la
ejecución del plan de inversión por parte del beneficiario.


Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Ingreso de los datos asociados a la verificación de la inversión
          - Jefe de acompañamiento
          - Datos asociados a la verificación de la inversión
        * - Registro de la recomendación del beneficiario para liquidaciones sucesivas en caso de que pase la inspección
          - Jefe de acompañamiento
          - Recomendación del beneficiario para liquidaciones sucesivas.
        * - Envío del expediente a Archivo.
          - Jefe de acompañamiento
          - Estación del expediente
        * - Envío del expediente a la unidad de Recuperaciones
          - Jefe de acompañamiento
          - Estación del expediente
        * - Envío del expediente a consultaría 
          - Jefe de acompañamiento
          - Estación del expediente
        * - Ingreso de nota explicativa para la siguiente estación
          - Jefe de acompañamiento
          - Nota explicativa
        * - Registrar los beneficiarios atendidos con fecha y hora
          - Jefe de acompañamiento
          - Registro de beneficiarios atendidos.
        * - Ingreso de fotografías de las inspecciones          
          - Jefe de acompañamiento
          - Código de fotografías de las inspecciones
        * - Generación de notas de visitas de inspección, atención en oficina o llamadas telefónicas          
          - Jefe de acompañamiento
          - Datos de las notas
        * - Edición de los datos del beneficiario.         
          - Jefe de acompañamiento
          - Datos del beneficiario
        * - Registro de los casos donde las visitas no son atendidas
          - Jefe de acompañamiento
          - Datos de los casos donde las visitas no son atendidas
        * - Edición de datos personales del beneficiario
          - Jefe de acompañamiento
          - Datos personales del beneficiario

.. index:: !Reportes Acompañamiento

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida  
        * - Registro de la cantidad de empleos generados directos e indirectos por cada crédito
          - Jefe de acompañamiento
          - Cantidad de empleos
        * - Consulta de la lista de créditos liquidados por administración
          - Jefe de acompañamiento
          - Lista de créditos liquidados
        * - Consulta de la información del beneficiario
          - Jefe de acompañamiento
          - Datos del beneficiario
        * - Consulta de la información del crédito
          - Jefe de acompañamiento
          - Datos del crédito
        * - Consulta de los beneficiarios atendidos por fecha y hora
          - Jefe de acompañamiento
          - Registro de beneficiarios atendidos.
        * - Generación de informe de acompañamiento          
          - Jefe de acompañamiento
          - Informe de acompañamiento.
        * - Generación de reportes con formato para las minutas
          - Jefe de acompañamiento
          - plantilla de la minuta
        * - Consulta de notas de visitas de inspección, atención en oficina o llamadas telefónicas
          - Jefe de acompañamiento
          - Plantilla de las notas
        * - Generación de notificación de acompañamiento          
          - Jefe de acompañamiento
          - Plantilla de notificación de acompañamiento 
        * - Generación de minuta de atención en oficina para las declaraciones de los beneficiarios          
          - Jefe de acompañamiento
          - Plantilla de la minuta de atención
        * - Generar formato de charla          
          - Jefe de acompañamiento
          - Plantilla de la charla
        * - Consulta de los depósitos de las cuotas
          - Jefe de acompañamiento
          - Depósitos de cuotas

.. index:: !Módulo Caja, Pagos

Módulo Caja
===========

Descripción
-----------

Este módulo abarca los procesos de "Pagos". Incluye procedimientos asociados con las actividades de recepción de pagos y
actualización de estados de cuenta de beneficiarios o beneficiarias.

Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Registro de los pagos de los beneficiarios para la cancelación de cuotas de los créditos
          - Cajero, ejecutivo de cobranza (caja)
          - Estado de cuenta
        * - Selección del expediente correspondiente al crédito al cual se desea pagar
          - Cajero
          - Expediente
        * - Calculo de los intereses de mora correspondientes a la cuota a pagar
          - Cajero
          - Intereses de mora
        * - Cierre de caja y desglose del ingreso total en billetes, monedas, cheques, punto de debito y depósitos
          - Cajero
          - Ingreso total
        * - Generación de solicitud de liberación a la unidad de Consultoría Jurídica en caso de último pago (cancelación total del crédito). 
          - Cajero, ejecutivo de cobranza (caja).
          - Registro de solicitud de liberación.
        * - Actualizar cuentas por cobrar y partidas presupuestarias con cada pago
          - Cajero
          - Cuentas por cobrar y partidas presupuestarias

.. index:: !Reportes Caja

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Generación de reporte del ingreso diario de caja
          - Cajero
          - Ingreso diario de caja
        * - Simulación del recibo
          - Cajero
          - Recibo de pago simulado
        * - Impresión del recibo de pago
          - Cajero
          - Recibo de pago
        * - Consulta del numero de cuotas vencidas, el total en Bolívares en cada cuota con sus intereses y cuotas que están próximas por vencerse
          - Cajero
          - Cuotas vencidas
        * - Creación de un reporte con el total de personas atendidas diariamente
          - Cajero
          - Reporte de beneficiarios atendidos

.. index:: !Módulo Recuperaciones, Visitas Cobranza, Rutas Cobranza

Módulo Recuperaciones 
=====================

Descripción
-----------

Este módulo abarca los procesos de "Gestión de cobranzas". Incluye procedimientos asociados con las actividades de
recepción de pagos, actualización de estados de cuenta de beneficiarios y trámites y gestión de recuperación de pagos
caídos por parte de los beneficiarios.


Procedimientos
--------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Registro de los beneficiarios atendidos diariamente
          - Ejecutivo de cobranza
          - Registro de los beneficiarios atendidos diariamente
        * - Cambio del estado del beneficiario según su morosidad
          - Gerente de recuperaciones
          - Estado de morosidad
        * - Creación de carteras de cobranza
          - Ejecutivo de cobranza
          - Carteras de cobranza
        * - Establecimiento de metas diarias de recuperación
          - Gerente de recuperaciones
          - Metas diarias de recuperación
        * - Ingreso de notas con los acuerdos e información suministrada por el beneficiario
          - Ejecutivo de cobranza
          - Notas con acuerdos
        * - Creación de recordatorios con las fechas de compromiso de pago del beneficiario
          - Ejecutivo de cobranza
          - Recordatorios con las fechas de compromiso de pago
        * - Generación de solicitud de entrevista con un abogado en caso de estado extrajudicial por mora
          - Gerente de Recuperaciones
          - Registro de solicitud de entrevista
        * - Cambiar estatus del crédito a demanda en el caso que lo amerite.
          - Gerente de Recuperaciones
          - Estatus del crédito
        * - Registro de exoneración en el cobro del crédito
          - Gerente de recuperaciones
          - Exoneración en el cobro del crédito
        * - Edición de datos personales del beneficiario
          - Ejecutivo de cobranza
          - Datos personales del beneficiario

.. index:: !Reportes Recuperaciones

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Generación de lista con los beneficiarios que se deben visitar por fecha, municipio y sectores en el caso que existan cuotas vencidas
          - Ejecutivo de cobranza
          - Lista de beneficiarios
        * - Consulta de estados de cuentas por cédula y expediente
          - Ejecutivo de cobranza
          - Estado de cuentas
        * - Acceso a los estados de cuenta desde la cartera de cobranza
          - Ejecutivo de cobranza
          - Estado de cuenta
        * - Consulta de los depósitos realizados por el beneficiario
          - Ejecutivo de cobranza
          - Depósitos
        * - Generación del reporte del ingreso diario de caja
          - Ejecutivo de cobranza
          - Reporte del ingreso diario de caja
        * - Consulta de notas con los acuerdos e información suministrada por el beneficiario
          - Ejecutivo de cobranza
          - Notas con acuerdos
        * - Ordenamiento de los expedientes por niveles de morosidad en las carteras
          - Ejecutivo de cobranza
          - Lista ordenada por morosidad
        * - Verificación de la validez de los depósitos bancarios para los pagos
          - Ejecutivo de cobranza
          - Validez de los depósitos bancarios
        * - Generar informe de seguimiento al beneficiario.
          - Ejecutivo de cobranza.
          - Informe de seguimiento.

.. index:: !Módulo Consultoría Jurídica, Créditos, Liberaciones

Módulo Consultaría Jurídica
===========================

Descripción
-----------

Este módulo abarca los procesos asistidos por los consultores jurídicos en: "Liquidación de créditos", "Liberación de
créditos" y "Gestión de cobranza". Incluye procedimientos asociados a la redacción de documentos jurídicos y cambio de
estatus del expediente.


Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Ingreso de datos del documento de liberación del crédito.
          - Consultoría Jurídica.
          - Datos de liberación del crédito.
        * - Generación de solicitud de reintegro del crédito en caso de que el beneficiario no cumpla con el plan de inversión.
          - Consultoría Jurídica.
          - Registro de solicitud de reintegro del crédito.
        * - Cambio del estatus del expediente a liberado.
          - Consultoría Jurídica
          - Estatus del expediente
        * - Envío de los expedientes con procesos culminados a Archivo
          - Consultaría Jurídica
          - Estación del expediente

.. index:: !Reportes Consultoría Jurídica

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Generación del documento de liberación del crédito
          - Consultoría Jurídica
          - Documento de liberación del crédito
        * - Generación del documento de solicitud de reintegro del crédito
          - Consultoría Jurídica
          - Documento de reintegro del crédito
        * - Generación de documento de liberación de hipotecas o fianzas para expedientes cancelados en su totalidad.
          - Consultoría Jurídica
          - Documento de liberación de hipotecas.
        * - Consulta de los expedientes con estatus “demanda” o "liberado"
          - Consultoría Jurídica
          - Lista de expedientes por estatus
        * - Generación de documento de demanda
          - Consultaría Jurídica
          - Documento de demanda

.. index:: !Módulo Archivo, Créditos

Módulo Archivo
==============

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes", "Inspección de inversiones", "Liberación de créditos",
"Gestión de cobranza". Incluye procedimientos asociados al control de la ubicación de los expedientes dentro de los
distintos departamentos del FOMDES.


Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Ingreso de nuevos expedientes.
          - Archivólogo.
          - Código de expediente
        * - Registro de responsables por expediente solicitado.
          - Archivólogo.
          - Responsable del expediente
        * - Envió de los expedientes a diferentes dependencias
          - Archivólogo
          - Estación del expediente

.. index:: !Reportes Archivo

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Registro de historial con detalle de movimientos de los expedientes
          - Archivólogo
          - Historial de movimiento del expediente
        * - Consulta lista de expedientes por departamento.
          - Archivólogo.
          - Lista de códigos de expediente

.. index:: !Módulo Estadística, Créditos, Presidencia

Módulo Estadística
==================

Descripción
-----------

Este módulo abarca los procesos que demandan análisis y cálculos estadísticos. Incluye procedimientos de generación de
estadísticas para el apoyo en la toma de decisiones por parte de las gerencias y directiva de FOMDES.

.. index:: !Reportes Estadística

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Generación de un reporte estadístico de todas las solicitudes ingresadas
          - Analista de crédito
          - Solicitudes ingresadas

.. index:: !Módulo Presidencia, Secretaría Ejecutiva

Módulo Presidencia
==================

Descripción
-----------

Este módulo abarca los procesos en los que interviene la gestión directa del presidente del FOMDES. Incluye
procedimientos de evaluación y coordinación con las gerencias para las tomas de decisiones.

Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Generación de la lista de expedientes priorizados
          - Secretaría Ejecutiva
          - Lista de expedientes priorizados

.. index:: !Reportes Presidencia

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Consulta del ingreso diario de caja y cumplimiento de metas
          - Presidente
          - Ingreso diario de caja
        * - Revisión de montos, intereses y plazos de las solicitudes de crédito
          - Presidente
          - Información de las solicitudes
        * - Evaluación y valoración de indicadores clave de rendimiento y variables políticas
          - Presidente
          - Indicadores clave de rendimiento

.. index:: !Módulo Atención

Módulo Atención
===============

Descripción
-----------

Este módulo abarca "Recepción y Evaluación de solicitudes",  Incluye procedimientos asociados al control de la ubicación
de los expedientes dentro de los distintos departamentos del FOMDES.


Procedimientos de ingreso de datos
----------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Datos accedidos o modificados
        * - Registro de los datos del solicitante junto con la fecha, hora y destino
          - Recepcionista
          - Datos del beneficiario
        * - Generación de colas por orden de atención y por dependencia
          - Recepcionista
          - Cola de cada dependencia

.. index:: !Reportes Atención

Procedimiento de generación de reportes
---------------------------------------

    .. list-table::
        :widths: 40 40 40
        :header-rows: 1

        * - | Procedimiento
          - | Responsable
          - | Reporte de salida
        * - Consulta de la información del estatus de las solicitudes activas
          - Recepcionista
          - Estatus de las solicitudes activas
        * - Consulta de la información del estado de cuenta del beneficiario
          - Recepcionista
          - Estado de cuenta del beneficiario
        * - Generación de reportes de los visitantes por rango de fecha y cedula
          - Recepcionista
          - Visitantes por rango de fecha y cedula

