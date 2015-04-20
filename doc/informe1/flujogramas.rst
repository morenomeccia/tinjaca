**********************
Flujogramas y procesos
**********************

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

