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
       :header-rows: 3

       * - Entrada
         - Actividades
         - Salida
       * - Propuesta de financiamiento.
         - Ingreso de datos al sistema WebAdmin.
         - Propuesta con código.
       * - Propuesta con código.
         - Revisión de la viabilidad de la propuesta.
         - Propuesta viable/no viable.
       * - Propuesta viable.
         - Incluye en lista del taller y envia requisitos.
         - Propuesta seleccionada para taller.

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
       :header-rows: 3

       * - Entrada
         - Actividades
         - Salida
       * - Requisitos por sector
         - Ingreso de datos al sistema SIGEFOMDES-Crédito
         - Expediente con codigo por sector
       * - Expediente
         - Revisión de la garantia
         - Propuesta que cumplen/no cumplen
       * - Propuesta que cumplen/no cumplen
         - Realiza inspeccion y avaluo a la unidad de producción
         - Informe tecnico

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

    * **Unidad(es) Ejecutora(s)**: Secretaría Ejecutiva, Consejo Directivo

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - Recepción de Propuesta de Financiamiento.
         - Ingreso de datos al sistema (Web Admin).
         - Planilla de la propuesta de financiamiento.

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

    * **Dependencia responsable**: Administración

    * **Unidad(es) Ejecutora(s)**: Presupuesto, Finanzas, Secretaría Ejecutiva, Presidencia

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO

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

    * **Unidad(es) Ejecutora(s)**: Departamento de Seguimiento, Verificación y Asistencia Técnica

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO

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
       * - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO

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

    * **Unidad(es) Ejecutora(s)**: Gerencia de Recuperaciones y Consultoría Jurídica

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO

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

    * **Unidad(es) Ejecutora(s)**: Administración, Presidencia, Consultoría Jurídica

    * **Tabla de Actividades**:

    .. list-table::
       :widths: 40 40 40
       :header-rows: 1

       * - Entrada
         - Actividades
         - Salida
       * - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO
         - TEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTOTEXTO TEXTO

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
