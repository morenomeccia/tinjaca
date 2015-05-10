**********************
Procesos y Flujogramas
**********************

A continuación se presentan los procesos identificados para la estructura funcional actual del
FOMDES en lo relativo a la asignación, acompañamiento en la ejecución y recuperación de los
créditos.


#. **Recepción de Propuestas**

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario/-a
    hasta la asistencia al taller

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Estadística y evaluación de riesgos

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

#. **Recepción y Evaluación de solicitudes**

    * **Descripción**: Abarca desde la entrega de recaudos para solicitud de crédito hasta la
    generación del listado de expedientes sugeridos para aprobación de créditos

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Análisis Jurídico, Análisis Económico

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

#. **Aprobación de Créditos**

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

#. **Liquidación de créditos**

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

#. **Inspección de inversiones**

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario/-a hasta la entrega de Recaudos a dependencia

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Estadística

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

#. **Gestión de cobranzas**

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario/-a hasta la entrega de Recaudos a dependencia

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Estadística

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

#. **Pagos**

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario/-a hasta la entrega de Recaudos a dependencia

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Estadística

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

#. **Liberación de créditos**

    * **Descripción**: Abarca desde la solicitud de información por parte del beneficiario/-a hasta la entrega de Recaudos a dependencia

    * **Dependencia responsable**: Gerencia de Crédito

    * **Unidad(es) Ejecutora(s)**: Información de Crédito, Estadística

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

