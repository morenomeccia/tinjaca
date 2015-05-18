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

PROCESS_LABEL = "Gestión de Cobranzas"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

r_cluster = {"r0": ("Revisión periódica", "start"),
             "r1": ("Generar lista de cuentas pagadas y vencidas", "human"),
             "r2": ("Planificar seguimiento y rutas de cobranza", "human"),
             "r3": ("¿Estado de las cuentas?", "exclusive"),
             "r4": ("Realizar llamada o enviar SMS de advertencia", "message"),
             "r5": ("Concertar entrevista y formular plan de pago", "message"),
             "r6": ("¿Cumple plan de pago?", "exclusive"),
             "r7": ("Cambiar estatus a caja", "human"),
             "r8": ("cambiar estatus a demanda", "human"),
             "r9": ("", "end")}

r_edges = {"r0": {"r1": {}},
           "r1": {"r2": {}},
           "r2": {"r3": {}},
           "r3": {"r4": {"xlabel": "A"}, "r5": {"xlabel": "B, C o D"}},
           "r5": {"r6": {}},
           "r6": {"r7": {"xlabel": "Si"}, "r8": {"xlabel": "No"}},
           "r4": {"r9": {}},
           "r7": {"r9": {}},
           "r8": {"r9": {}}}

R = add_cluster(F, "r", "Recuperaciones", r_cluster, r_edges)

#F.add_node("SIGEFOMDES Administración", image="static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Administración")
F.add_node("SISAC", image="static/database.png", shape="plaintext", label="", xlabel="SISAC")

global_edges = {"Acompañamiento":  {"r0": {"xlabel": fill("Expedientes que cumplen plan de inversión", TEXT_WIDTH)}},
                "r7": {"SISAC": {"style": "dashed"}},
                "r8": {"Consultoría Jurídica": {"style": "dashed"}, "SISAC": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc7.png", prog='dot')
F.write("proc7.dot")
