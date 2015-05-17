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

PROCESS_LABEL = "Inspección de Inversiones"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="7.5, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

a_cluster = {"a0": ("Recibir expediente", "start"),
             "a1": ("Verificar cumplimiento del plan de inversión", "human"),
             "a2": ("Elaborar informe del plan de inversión", "human"),
             "a3": ("¿Cumple?", "exclusive"),
             "a4": ("Enviar expediente a Recuperaciones", "message"),
             "a5": ("", "end")}

a_edges = {"a0": {"a1": {}},
           "a1": {"a2": {}},
           "a2": {"a3": {}},
           "a3": {"a4": {"xlabel": "Si"}},
           "a4": {"a5": {}}}

A = add_cluster(F, "a", "Acompañamiento", a_cluster, a_edges)

cj_cluster = {"cj0": ("Exigir reintegro del crédito", "human")}

cj_edges = {}

CJ = add_cluster(F, "cj", "Consultoría Jurídica", cj_cluster, cj_edges)

# F.add_node("SIGEFOMDES Administración", image="static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Administración")
# F.add_node("SISAC", image="static/database.png", shape="plaintext", label="", xlabel="SISAC")

global_edges = {"Secretaría Ejecutiva":  {"a0": {"style": "dashed"}},
                "a3": {"cj0": {"style": "dashed", "xlabel": "No"}},
                "a4": {"Recuperaciones": {"style": "dashed"}},
                "cj0":{"a5": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc5.png", prog='dot')
F.write("proc5.dot")
