**********************
Procesos y Flujogramas
**********************

A continuación se presentan los procesos identificados para la estructura funcional actual del
FOMDES en lo relativo a la asignación, acompañamiento en la ejecución y recuperación de los
créditos.

**Recepción de Propuestas**
===========================

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario/-a hasta la asistencia al taller

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Analistas de Crédito, Estadística y Evaluación de Riesgos

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - El usuario descarga la planilla Propuesta de Financiamiento desde la web y la introduce en Información de Crédito
         - Revisa propuesta e ingresa los datos al sistema WebAdmin para generar código de la propuesta
         - Propuesta de financiamiento con código
       * - Propuesta de financiamiento con código
         - Evaluan la viabilidad de la propuesta y si cumple con las normativas del FOMDES
         - Propuesta viable/no viable
       * - Propuesta viable
         - Añade al usuario en la lista del Taller Integral de Asesoría y Acompañamiento al Potencial Beneficiario y se envia lista de requisitos
         - Usuario convocado para realizar taller

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

**Recepción y Evaluación de Solicitudes**
=========================================

    * **Descripción**: Abarca desde la entrega de recaudos para solicitud de crédito hasta la
      generación del listado de expedientes sugeridos para aprobación de créditos

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Análisis Jurídico, Análisis Económico

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Requisitos por sector
         - Ingreso de datos al sistema SIGEFOMDES-Crédito
         - Expediente con código por sector
       * - Expediente
         - Revisión de la garantia
         - Expediente con control previo
       * - Expediente
         - Realiza inspección y avalúo a la unidad de producción
         - Expediente con informe técnico de evaluación.

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

**Aprobación de Créditos**
==========================

    * **Descripción**: Abarca desde la recepción del listado de expedientes sugeridos para
      aprobación de créditos hasta la elaboración del Documento de Crédito y constitución de la
      empresa (de requerirse) para cada uno de los beneficiarios/-as.

    * **Dependencia responsable**: Presidencia

    * **Unidad(es) Ejecutora(s)**: Analistas de Crédito, Presupuesto, Secretaría Ejecutiva, Consejo Directivo, Presupuesto, Secretaría Ejecutiva

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Expediente
         - Revisión de la propuesta para aprobar/rechazar
         - Informe sobre perfil de la actividad, inversión y proyección económica
       * - Expediente
         - Revisión del expediente
         - Certificación presupuestaria por sector
       * - Propuesta sugerida para aprobar/rechazar
         - Convoca al consejo directivo
         - Lista de propuestas para aprobar/rechazar
       * - Propuesta para aprobar/rechazar
         - Revisión de expediente
         - Acta de propuesta aprobada
       * - Expediente
         - Realiza control previo de los requisitos
         - Certificación de disponibilidad de dinero para liquidación de crédito
       * - Expediente aprobado
         - Redacta documentos
         - Entrega documento de crédito y documento de constitución de empresa al beneficiario

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

**Liquidación de Créditos**
===========================

    * **Descripción**: Abarca desde la consignación de los documentos notariados por parte de los
      beneficiarios/-as hasta la entrega del cheque respectivo.

    * **Dependencia responsable**: Administración y Finanzas

    * **Unidad(es) Ejecutora(s)**: Secretaria Ejecutiva, Administración, Presidencia, Secretaría Ejecutiva

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Documento protocolizado del cŕedito
         - Revisión del documento protocolizado
         - Envia expediente a Administración
       * - Expediente
         - Ingreso de datos al sistema SIGEFOMDES-Administración-SISAC
         - Cuentas por cobrar/tabla de amortización/orden de liquidación/cheque firmado
       * - Cheque firmado por Administración
         - Firma del cheque
         - Cheque firmado
       * - Cheque firmado
         - Convoca acto público con el Gobernador
         - Entrega de cheque a beneficiario

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
      cuenta de beneficiarios/-as

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
      pagos caídos por parte de beneficiarios/-as.

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
