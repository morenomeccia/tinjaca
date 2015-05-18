#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
BPMN diagram for FOMDES process 1
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from bpmn_pgv import *
import pygraphviz as pgv

__author__ = 'mapologo'

PROCESS_LABEL = "Recepción y Evaluación de Solicitudes 1"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

u_cluster = {"u4": ("Recibir Requisitos", "start"),
             "u5": ("Reunir Requisitos", "human"),
             "u6": ("Consignar los Requisitos", "message"),
             "u7": ("Fin Requisitos", "end")}

u_edges = {"u4": {"u5": {}},
           "u5": {"u6": {}},
           "u6": {"u7": {}},
           "u7": {}}

U = add_cluster(F, "u", "Usuario", u_cluster, u_edges)

ic_cluster = {"ic4": ("Recibir Requisitos", "start"),
              "ic5": ("Crear Expediente", "human"),
              "ic6": ("Entrevista con el usuario", "human"),
              "ic7": ("", "end")}

ic_edges = {"ic4": {"ic5": {}},
            "ic5": {"ic6": {}},
            "ic6": {"ic7": {"style": "invis"}}}

IC = add_cluster(F, "ic", "Información de Crédito", ic_cluster, ic_edges)

aj_cluster = {"aj0": ("Verificar validez legal de los requisitos", "human"),
              "aj1": ("Elaborar Informe de Control Previo", "human"),
              "aj2": ("¿La garantía cumple?", "exclusive"),
              "aj3": ("Enviar Expediente a Análisis Económico", "message")}

aj_edges = {"aj0": {"aj1": {}},
            "aj1": {"aj2": {}},
            "aj2": {"aj3": {"xlabel": "Si"}}}

AJ = add_cluster(F, "aj", "Análisis Jurídico", aj_cluster, aj_edges)

F.add_node("SIGEFOMDES Crédito", image="static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Crédito")

global_edges = {"u6":  {"ic4": {"style": "dashed"}},
                "ic6": {"aj0": {"style": "dashed"}},
                "ic5": {"SIGEFOMDES Crédito": {"style": "dashed"}},
                "aj1": {"SIGEFOMDES Crédito": {"style": "dashed"}},
                "aj3": {"ic7": {"style": "dashed"}, "Análisis Económico": {"style": "dashed"}},
                fill("Estadística y Evaluación de Riesgos", TEXT_WIDTH): {"u4": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc21.png", prog='dot')
F.write("proc21.dot")
