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

PROCESS_LABEL = "Gestión de Cobranzas 2"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

b_cluster = {"b0": ("Requiere solicitar exoneración", "start"),
             "b1": ("Solicitar exoneración", "message"),
             "b2": ("", "end")}

b_edges = {"b0": {"b1": {}},
           "b1": {"b2": {}}}

B = add_cluster(F, "b", "Beneficiario", b_cluster, b_edges)

cd_cluster = {"cd2": ("Recibir solicitud de exoneración", "start"),
              "cd3": ("¿Revisar exoneración?", "human"),
              "cd4": ("¿Aprobar exoneración?", "exclusive"),
              "cd5": ("Ordenar ejecución de la exoneración", "message"),
              "cd6": ("", "end")}

cd_edges = {"cd2": {"cd3": {}},
            "cd3": {"cd4": {}},
            "cd4": {"cd5": {"xlabel": "Si"}, "cd6":{"xlabel": "No"}},
            "cd5": {"cd6": {}}}

CD = add_cluster(F, "cd", "Consejo Directivo", cd_cluster, cd_edges)

r_cluster = {"r10": ("Recibir orden de exoneración", "start"),
             "r11": ("Ejecutar exoneración de crédito", "human"),
             "r12": ("", "end")}

r_edges = {"r10": {"r11": {}},
           "r11": {"r12": {}}}

R = add_cluster(F, "r", "Recuperaciones", r_cluster, r_edges)

#F.add_node("SIGEFOMDES Administración", image="static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Administración")
F.add_node("SISAC", image="static/database.png", shape="plaintext", label="", xlabel="SISAC")

global_edges = {"b1": {"cd2": {"style": "dashed"}},
                "cd5": {"r10": {"style": "dashed"}},
                "r11": {"SISAC":{}}}

add_edges(F, global_edges)

F.draw("proc7b.png", prog='dot')
F.write("proc7b.dot")
