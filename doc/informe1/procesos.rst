**********************
Procesos y Flujogramas
**********************

Los procesos fueron modelados usando la notación gráfica Business Process Modeling Notation (BPMN) para describir la
secuencia de los procesos y mensajes que fluyen entre las unidades que realizan las diferentes actividades del FOMDES.

Entre las características resaltantes del BPMN como metodología de representación gráfica de procesos, destaca la
posibilidad de identificar de modo claro y simplificado las líneas que agrupan varias unidades ejecutoras en el
cumplimiento de tareas y subprocesos. Pero además, el BPMN es muy útil en la identificación de líneas de comunicación y
flujos de entrada y salida entre cada uno de los procesos y subprocesos que se determinen para la institución.

A continuación se presentan los procesos identificados para la estructura funcional actual de la institución en lo
relativo a la asignación de créditos, acompañamiento en su ejecución y recuperación de la inversión.

.. index:: !Gerencia de Crédito, Potencial beneficiario o beneficiaria, Información de Crédito, Estadística y Evaluación de Riesgos

**Recepción de Propuestas**
===========================

    * **Descripción**: Abarca desde la solicitud de información por parte del potencial beneficiario o beneficiaria hasta la asistencia al taller

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Potencial beneficiario o beneficiaria, Información de Crédito, Estadística y Evaluación de Riesgos

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Necesidad de solicitar un crédito
         - Descargar e introducir planilla "Propuesta de Financiamiento"
         - Propuesta de financiamiento
       * - Propuesta de financiamiento
         - Revisar propuesta e ingresar los datos al sistema WebAdmin para generar código de la propuesta
         - Propuesta de financiamiento con código
       * - Propuesta de financiamiento
         - Evaluar la viabilidad de la propuesta y si cumple con las normativas del FOMDES
         - Propuesta viable/no viable
       * - Propuesta viable
         - Añadir potencial beneficiario o beneficiaria a la lista del "Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario" y
           enviar lista de requisitos
         - Potencial beneficiario o beneficiaria convocado para realizar taller

    * **Flujograma**: Ver Figura 3.1

    .. graphviz:: _graphviz/proc1.dot
       :caption: Recepción de Propuestas

.. index:: !Gerencia de Crédito, Potencial beneficiario o beneficiaria, Información de Crédito, Análisis Jurídico, Análisis Económico

**Recepción y Evaluación de Solicitudes**
=========================================

    * **Descripción**: Abarca desde la entrega de recaudos para solicitud de crédito hasta la generación del listado de
        expedientes sugeridos para aprobación de créditos

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Potencial beneficiario o beneficiaria, Información de Crédito, Análisis Jurídico, Análisis Económico

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Planilla de requisitos
         - Reunir y consignar los requisitos
         - Requisitos por sector
       * - Requisitos por sector
         - Ingresar datos al sistema SIGEFOMDES-Crédito y crear expediente.
         - Expediente con código por sector
       * - Expediente
         - Revisar validez legal de la garantía para conocer si cumple con las políticas de financiamiento de FOMDES
         - Expediente con control previo
       * - Expediente
         - Verificar la viabilidad económica de la unidad de producción
         - Expediente con informe de inspección
       * - Expediente
         - Verificar la garantía en el sitio
         - Expediente con informe de avalúo
       * - Expediente
         - Realizar el informe técnico
         - Expediente con informe técnico (memoria fotográfica)
       * - Expediente
         - Elaborar lista de expedientes para consideración de Presidencia
         - Lista de expedientes

    * **Flujograma**: Ver Figuras 3.2 y 3.3

    .. graphviz:: _graphviz/proc21.dot
       :caption: Recepción y Evaluación de Solicitudes 1

    .. graphviz:: _graphviz/proc22.dot
       :caption: Recepción y Evaluación de Solicitudes 2

.. index:: !Presidencia, Secretaría Ejecutiva, Presupuesto, Consejo Directivo

**Aprobación de Créditos**
==========================

    * **Descripción**: Abarca desde la recepción del lista de expedientes sugeridos para
      aprobación de créditos hasta la elaboración del Documento de Crédito y constitución de la
      empresa (de requerirse) para cada uno de los beneficiarios(as).

    * **Dependencia responsable**: Presidencia

    * **Unidad(es) Ejecutora(s)**: Presidencia, Secretaría Ejecutiva, Presupuesto, Consejo Directivo

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Lista de expedientes
         - Revisar montos, intereses y plazos del crédito y priorizar los expedientes que van a Consejo Directivo
         - Lista de expedientes
       * - Plan de inversión, decisiones previas del Consejo Directivo y Estados financieros
         - Elaborar certificación presupuestaria y financiera por sector
         - Certificación presupuestaria y financiera por sector
       * - Lista de expedientes para Consejo Directivo
         - Realizar agenda con expedientes priorizados y convocar al Consejo Directivo
         - Convocatoria del Consejo Directivo
       * - Certificación presupuestaria y financiera, lista de expedientes priorizada
         - Deliberar sobre aprobación de los créditos
         - Acta de decisión del Consejo Directivo
       * - Acta de créditos aprobados
         - Elaborar el documento de crédito y de ser necesario el documento de la empresa
         - Documento de crédito y documento de constitución de empresa

    * **Flujograma**: Ver Figura 3.4

    .. graphviz:: _graphviz/proc3.dot
       :caption: Aprobación de Créditos

.. index:: !Administración y Finanzas, Secretaría Ejecutiva, Presupuesto, Administración, Presidencia

**Liquidación de Créditos**
===========================

    * **Descripción**: Abarca desde la consignación de los documentos notariados por parte de los
      beneficiarios(as) hasta la entrega del cheque respectivo.

    * **Dependencia responsable**: Administración y Finanzas

    * **Unidad(es) Ejecutora(s)**: Secretaria Ejecutiva, Presupuesto, Administración, Presidencia

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Documento protocolizado del cŕedito
         - Revisar el documento protocolizado
         - Expediente con Documento de Crédito Protocolizado
       * - Expediente
         - Verificar documentación legal y elaborar certificación de disponibilidad para liquidación del crédito
         - Expediente en regla
       * - Expediente
         - Ingresar datos y crear cuentas en el sistema SIGEFOMDES-Administración y SISAC
         - Expediente con cuentas por cobrar y tabla de amortización
       * - Expediente
         - Imprimir y firmar orden de liquidación y cheque
         - Cheque
       * - Cheque firmado por Administración
         - Firmar cheque
         - Cheque firmado por Presidencia
       * - Cheque
         - Entregar cheque a beneficiario en acto público
         - Expediente con copia de orden de liquidación

    * **Flujograma**: Ver Figura 3.5

    .. graphviz:: _graphviz/proc4.dot
       :caption: Liquidación de Créditos

.. index:: !Gerencia de Crédito, !Gerencia de Recuperaciones, Acompañamiento y Asistencia Técnica, Consultoría Jurídica, Archivo

**Inspección de Inversiones**
=============================

    * **Descripción**: Comprende actividades relativas a la verificación de la ejecución del plan
      de inversión por parte del beneficiario.

    * **Dependencia responsable**: Gerencia de Crédito y Gerencia de Recuperaciones

    * **Unidad(es) Ejecutora(s)**: Acompañamiento y Asistencia Técnica, Consultoría Jurídica, Archivo

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Expediente
         - Visitar la unidad de producción para verificar si cumple con el plan de inversión
         - Informe de verificación de la inversión/Recomendación del beneficiario para liquidaciones sucesivas
       * - Expediente que no cumple con el plan de inversión
         - Solicitar reintegro del crédito
         - Devolución total del crédito
       * - Expediente
         - Ingresar código de expediente a la lista de Archivo
         - Expediente con informe de verificación del plan de inversión

    * **Flujograma**: Ver Figura 3.6

    .. graphviz:: _graphviz/proc5.dot
       :caption: Inspección de Inversiones

.. index:: !Administración y Finanzas, Caja, Consultoría Juridica

**Pagos**
=========

    * **Descripción**: Incluye actividades de recepción de pagos y actualización de estados de
      cuenta de beneficiarios(as)

    * **Dependencia responsable**: Administración y Finanzas

    * **Unidad(es) Ejecutora(s)**: Caja, Consultoría Juridica

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Beneficiario que desea pagar
         - Consultar estado de cuenta en SISAC
         - Estado de cuenta
       * - Cuenta en estado "caja"
         - Recibir pago de cuotas de crédito
         - Recibo original al beneficiario y copia al expediente en Archivo
       * - Último pago
         - Realizar la cancelación total del crédito
         - Solicitud de liberación a Consultoría Jurídica
       * - Cuenta en estado "extrajudicial"
         - Referir beneficiario a Recuperaciones
         - Solicitud de entrevista con Abogado de Recuperaciones
       * - Cuenta en estado "extrajudicial"
         - Referir beneficiario a Recuperaciones
         - Solicitud de entrevista con Abogado de Recuperaciones

    * **Flujograma**: Ver Figura 3.7

    .. graphviz:: _graphviz/proc6.dot
       :caption: Pagos

.. index:: !Gerencia de Recuperaciones, Ejecutivos de Cobranza, Consultoría Juridica

**Gestión de Cobranzas**
========================

    * **Descripción**: Comprende actividades relativas al trámite y gestión de recuperación de
      pagos caídos por parte de beneficiarios(as).

    * **Dependencia responsable**: Gerencia de Recuperaciones

    * **Unidad(es) Ejecutora(s)**: Recuperaciones, Ejecutivos de Cobranza, Presidencia, Consejo Directivo, Consultoría Jurídica

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Expediente que cumple con el plan de inversión
         - Revisar listas de carteras y sábanas
         - Lista de cuotas pagadas/vencidas
       * - Lista de cuotas pagadas/vencidas
         - Planificar seguimiento y rutas de cobranza
         - Informe de seguimiento al beneficiario
       * - Cuenta estado "A"
         - Realizar llamada o enviar mensaje SMS de advertencia
         - Llamada o mensaje SMS de advertencia
       * - Cuenta estado "B","C" o "D"
         - Solicitar entrevista y formular plan de pago
         - Acuerdo de plan de pago
       * - Solicitud de exoneración del crédito ante Presidencia
         - Revisar la exoneración del crédito
         - Solicitud de exoneración del crédito
       * - Solicitud de exoneración del crédito ante Consejo Directivo
         - Aprobar la exoneración del crédito
         - Solicitud de liberación del crédito
       * - Seguimiento de plan de pago
         - Cambiar estatus a caja si cumple el plan de pago
         - Cuenta en estatus caja
       * - Seguimiento de plan de pago
         - Cambiar estatus a demanda si no cumple el plan de pago
         - Ejecución de garantía


    * **Flujograma**: Ver Figuras 3.8 y 3.9

    .. graphviz:: _graphviz/proc7.dot
       :caption: Gestión de Cobranzas 1

    .. graphviz:: _graphviz/proc7b.dot
       :caption: Gestión de Cobranzas 2

.. index:: !Administración y Finanzas, Consultoría Juridica, Presidencia

**Liberación de Créditos**
==========================

    * **Descripción**: Contempla actividades relativas a la liberación de los créditos.

    * **Dependencia responsable**: Administración y Finanzas

    * **Unidad(es) Ejecutora(s)**: Administración y Finanzas, Consultoría Jurídica, Presidencia

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - | Entrada
         - | Actividades
         - | Salida
       * - Expediente con cancelación total
         - Verificar el estatus de la cuenta
         - Solicitud de liberación de crédito
       * - Expediente
         - Redactar documento de liberación del crédito
         - Documento de liberación del crédito
       * - Documento de liberación del crédito
         - Revisar y aprobar documento de liberación del crédito
         - Documento de liberación firmado por Presidencia
       * - Documento de liberación
         - Entregar documento al beneficiario
         - Expediente con documento de liberación

    * **Flujograma**: Ver Figura 3.10

    .. graphviz:: _graphviz/proc8.dot
       :caption: Liberación de Créditos