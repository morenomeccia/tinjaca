**********************
Procesos y Flujogramas
**********************

A continuación se presentan los procesos identificados para la estructura funcional actual del
FOMDES en lo relativo a la asignación, acompañamiento en la ejecución y recuperación de los
créditos.

**Recepción de Propuestas**
===========================

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario(a) hasta la asistencia al taller

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Usuario/Beneficiario, Información de Crédito, Estadística y Evaluación de Riesgos

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Necesidad de solicitar un crédito
         - Descargar e introducir planilla de "Propuesta de Financiamiento"
         - Propuesta de financiamiento
       * - Propuesta de financiamiento
         - Revisar propuesta e ingresar los datos al sistema WebAdmin para generar código de la propuesta
         - Propuesta de financiamiento con código
       * - Propuesta de financiamiento
         - Evaluar la viabilidad de la propuesta y si cumple con las normativas del FOMDES
         - Propuesta viable/no viable
       * - Propuesta viable
         - Añadir al usuario en la lista del "Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario" y
           enviar lista de requisitos
         - Usuario convocado para realizar taller

    * **Flujograma**: Ver Figura 3.1

    .. graphviz:: proc1.dot


**Recepción y Evaluación de Solicitudes**
=========================================

    * **Descripción**: Abarca desde la entrega de recaudos para solicitud de crédito hasta la generación del listado de
        expedientes sugeridos para aprobación de créditos

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Usuario/Beneficiario, Información de Crédito, Análisis Jurídico, Análisis Económico

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Planilla de requisitos
         - Reunir y consignar los requisitos
         - Requisitos por sector
       * - Requisitos por sector
         - Ingresar datos al sistema SIGEFOMDES-Crédito, y crear expediente.
         - Expediente con código por sector
       * - Expediente
         - Revisar validez legal de la garantía
         - Expediente con control previo
       * - Expediente
         - Verificar la viabilidad económica de la unidad de producción
         - Expediente con informe de inspección
       * - Expediente
         - Verificar la garantía en el sitio
         - Expediente con informe de avalúo
       * - Expediente
         - Realizar el informe técnico
         - Expediente con informe técnico (con memoria fotográfica)
       * - Expediente
         - Elaborar lista de expedientes para consideración del Consejo Directivo
         - Lista de expedientes

    * **Flujograma**: Ver Figuras 3.2 y 3.3

    .. graphviz:: proc21.dot

    .. graphviz:: proc22.dot


**Aprobación de Créditos**
==========================

    * **Descripción**: Abarca desde la recepción del lista de expedientes sugeridos para
      aprobación de créditos hasta la elaboración del Documento de Crédito y constitución de la
      empresa (de requerirse) para cada uno de los beneficiarios(as).

    * **Dependencia responsable**: Presidencia

    * **Unidad(es) Ejecutora(s)**: Secretaría Ejecutiva, Presupuesto, Consejo Directivo

    * **Tabla de Actividades**:

    .. tabularcolumns:: |p{4cm}|p{7cm}|p{4cm}|

    .. list-table::
       :widths: 40 70 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Lista de expedientes
         - Revisar lista de expedientes junto con presidencia
         - Lista de expedientes priorizada
       * - Expediente
         - Elaborar certificación presupuestaria por sector
         - Certificación presupuestaria por sector
       * - Lista de expediente para consejo directivo
         - Convocar al consejo directivo
         - Acta de créditos aprobados
       * - Acta de créditos aprobados
         - Elaborar el documento de crédito y de ser necesario el documento de la empresa
         - Documento de crédito y documento de constitución de empresa

    * **Flujograma**:

    .. graphviz:: proc3.dot

**Liquidación de Créditos**
===========================

    * **Descripción**: Abarca desde la consignación de los documentos notariados por parte de los
      beneficiarios(as) hasta la entrega del cheque respectivo.

    * **Dependencia responsable**: Administración y Finanzas

    * **Unidad(es) Ejecutora(s)**: Secretaria Ejecutiva,Presupuesto, Administración, Presidencia, Secretaría Ejecutiva

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Documento protocolizado del cŕedito
         - Revisar el documento protocolizado
         - Expediente con Documento de Crédito Protocolizado
       * - Expediente
         - Verificar documentación legal y elaborar certificación de disponibilidad para liquidación del crédito
         - Expediente en regla
       * - Expediente
         - Ingreso de datos y creación de cuentas en el sistema SIGEFOMDES-Administración y SISAC
         - Expediente con cuentas por cobrar y tabla de amortización
       * - Expediente
         - Imprimir y firmar orden de liquidación y cheque
         - Cheque
       * - Cheque firmado por Administración
         - Firma del cheque
         - Cheque firmado por Presidencia
       * - Cheque
         - Entregar cheque a beneficiario
         - Expediente con copia de orden de liquidación

    * **Flujograma**:

    .. graphviz::

**Inspección de Inversiones**
=============================

    * **Descripción**: Comprende actividades relativas a la verificación de la ejecución del plan
      de inversión por parte del beneficiario.

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Acompañamiento y Asistencia Técnica, Consultoria Juridica, Archivo

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Expediente
         - Visita la unidad de producción para verificar si cumple/no cumple con el plan de inversión
         - Informe de verificación de la inversión/Recomendación del beneficiario para futuros créditos
       * - Expediente que no cumple con el plan de inversión
         - Solicitud de reintegro del crédito
         - Crédito otorgado
       * - Expediente
         - Introduce documentos al expediente
         - Expediente

    * **Flujograma**:

    .. graphviz::

       digraph G05 { rankdir=LR; node [shape=box, style=rounded];

        subgraph clusterA { labeljust=l; label="any-section@company.com";
         AS [label="", shape=circle, width="0.3"];
         AE [label="", shape=circle, width="0.3", style=bold];
         A1 [label="A1: Daily\nReport"];
         A2 [label="A2: Memo"];

         AS -> A1;
         A2 -> AE;
         A1 -> A2 [style=invis];
        }

        subgraph clusterB { labeljust=l; label="section-leader@company.com";
         B1 [label="B1: Review"];
        }

       A1 -> B1 [tailport=sw,headport=nw]; // *Specify positions of tail port and head port*
       B1 -> A1 [arrowtail=odiamond, label="NG"];
       B1 -> A2 [arrowtail=rcrowlvee];
       }

**Pagos**
=========

    * **Descripción**: Incluye actividades de recepción de pagos y actualización de estados de
      cuenta de beneficiarios(as)

    * **Dependencia responsable**: Administración

    * **Unidad(es) Ejecutora(s)**: Caja

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Cuentas por cobrar
         - Recibe pago de cuotas de crédito
         - Recibo de pago realizado. Original al beneficiario y copia al expediente

    * **Flujograma**:

    .. graphviz::

       digraph G05 { rankdir=LR; node [shape=box, style=rounded];

        subgraph clusterA { labeljust=l; label="any-section@company.com";
         AS [label="", shape=circle, width="0.3"];
         AE [label="", shape=circle, width="0.3", style=bold];
         A1 [label="A1: Daily\nReport"];
         A2 [label="A2: Memo"];

         AS -> A1;
         A2 -> AE;
         A1 -> A2 [style=invis];
        }

        subgraph clusterB { labeljust=l; label="section-leader@company.com";
         B1 [label="B1: Review"];
        }

       A1 -> B1 [tailport=sw,headport=nw]; // *Specify positions of tail port and head port*
       B1 -> A1 [arrowtail=odiamond, label="NG"];
       B1 -> A2 [arrowtail=rcrowlvee];
       }

**Gestión de Cobranzas**
========================

    * **Descripción**: Comprende actividades relativas al trámite y gestión de recuperación de
      pagos caídos por parte de beneficiarios(as).

    * **Dependencia responsable**: Gerencia de Recuperaciones

    * **Unidad(es) Ejecutora(s)**: Recuperaciones, Ejecutivos de Cobranza, Consultoría Jurídica

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Expediente que cumple con el plan de inversión
         - Revisión de carteras y sabanas
         - Lista de cuotas pagadas/vencidas
       * - Lista de cuotas pagadas/vencidas
         - Planifica seguimiento y rutas de cobranza
         - Informe de seguimiento al beneficiario
       * - Lista de morosos
         - Demanda por ejecución de garantia
         - Garantia del crédito

    * **Flujograma**:

    .. graphviz::

       digraph G05 { rankdir=LR; node [shape=box, style=rounded];

        subgraph clusterA { labeljust=l; label="any-section@company.com";
         AS [label="", shape=circle, width="0.3"];
         AE [label="", shape=circle, width="0.3", style=bold];
         A1 [label="A1: Daily\nReport"];
         A2 [label="A2: Memo"];

         AS -> A1;
         A2 -> AE;
         A1 -> A2 [style=invis];
        }

        subgraph clusterB { labeljust=l; label="section-leader@company.com";
         B1 [label="B1: Review"];
        }

       A1 -> B1 [tailport=sw,headport=nw]; // *Specify positions of tail port and head port*
       B1 -> A1 [arrowtail=odiamond, label="NG"];
       B1 -> A2 [arrowtail=rcrowlvee];
       }


**Liberación de Créditos**
==========================

    * **Descripción**: Contempla actividades relativas a la liberación de los créditos.

    * **Dependencia responsable**: Administración

    * **Unidad(es) Ejecutora(s)**: Administración, Consultoría Jurídica, Presidencia

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Expediente
         - Revisión de sabana
         - Informe para liberación de crédito
       * - Expediente
         - Redacta documento de liberación del crédito
         - Documento de liberación del crédito
       * - Documento de liberación del crédito
         - Firma documento de liberación del crédito
         - Entrega de documento al beneficiario

    * **Flujograma**:

    .. graphviz::

       digraph G05 { rankdir=LR; node [shape=box, style=rounded];

        subgraph clusterA { labeljust=l; label="any-section@company.com";
         AS [label="", shape=circle, width="0.3"];
         AE [label="", shape=circle, width="0.3", style=bold];
         A1 [label="A1: Daily\nReport"];
         A2 [label="A2: Memo"];

         AS -> A1;
         A2 -> AE;
         A1 -> A2 [style=invis];
        }

        subgraph clusterB { labeljust=l; label="section-leader@company.com";
         B1 [label="B1: Review"];
        }

       A1 -> B1 [tailport=sw,headport=nw]; // *Specify positions of tail port and head port*
       B1 -> A1 [arrowtail=odiamond, label="NG"];
       B1 -> A2 [arrowtail=rcrowlvee];
       }
