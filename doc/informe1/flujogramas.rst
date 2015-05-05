**********************
Procesos y Flujogramas
**********************

A continuación se presentan los procesos identificados para la estructura funcional actual del
FOMDES en lo relativo a la asignación, acompañamiento en la ejecución y recuperación de los
créditos.

+---------------------------------------------------+
|Nombre del Proceso: Solicitud de Crédito           |
|Descripción: Abarca desde la solicitud de          |
|          información por parte del beneficiario/-a|
|          hasta su entrega a Secretaría Ejecutiva  |
|Unidad ejecutora: Gerencia de Crédito              |
+===============+====================+==============+
|     Entrada   |      Actividades   |   Salida     |
+---------------+--------------------+--------------+
|               |                    |              |
|               |                    |              |
|               |                    |              |
+---------------+--------------------+--------------+
|               |                    |              |
|               |                    |              |
|               |                    |              |
+---------------+--------------------+--------------+

Flujograma

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

