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
       * - Propuesta de financiamiento
         - Ingreso de datos al sistema WebAdmin
         - Propuesta de financiamiento
       * - Propuesta de financiamiento
         - Revisión de la viabilidad de la propuesta
         - Propuesta viable/no viable
       * - Propuesta viable
         - Incluye propuesta en lista del taller y envia requisitos
         - Propuesta seleccionada para taller

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

**Recepción y Evaluación de solicitudes**
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
         - Propuesta que cumple/no cumple con las políticas de financiamiento
       * - Propuesta que cumple/no cumple con las políticas de financiamiento
         - Realiza inspección y avalúo a la unidad de producción
         - Informe técnico de evaluación para aprobar/rechazar crédito

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
       * - Propuesta sugerida para aprobar/rechazar
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
       * - Propuesta aprobada
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

**Liquidación de créditos**
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

**Inspección de inversiones**
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

**Gestión de cobranzas**
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


**Liberación de créditos**
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
