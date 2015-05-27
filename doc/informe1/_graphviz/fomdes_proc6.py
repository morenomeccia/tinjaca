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

PROCESS_LABEL = "Pagos"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

c_cluster = {"c0": ("Beneficiario desea cancelar cuota", "start"),
             "c1": ("Consultar el estado de cuenta", "human"),
             "c2": ("¿El estado de la cuenta es \"caja\"?", "exclusive"),
             "c3": ("Recibir el pago", "human"),
             "c4": ("Generar recibo", "message"),
             "c5": ("Referir al beneficiario a Recuperaciones", "message"),
             "c6": ("¿Es cancelación total?", "exclusive"),
             "c7": ("Solicitar Liberación a Consultoría Jurídica", "message"),
             "c8": ("", "end")}

c_edges = {"c0": {"c1": {}},
           "c1": {"c2": {}},
           "c2": {"c3": {"xlabel": "Si"}, "c5": {"xlabel": "No"}},
           "c3": {"c4": {}},
           "c4": {"c6": {}},
           "c6": {"c7": {"xlabel": "Si"}, "c8": {"xlabel": "No"}},
           "c7": {"c8": {}}}

C = add_cluster(F, "c", "Caja", c_cluster, c_edges)

cj_cluster = {"cj1": ("Liberar hipoteca o fianza", "human")}

cj_edges = {}

CJ = add_cluster(F, "cj", "Consultoría Jurídica", cj_cluster, cj_edges)

r_cluster = {"r0": ("Concertar entrevista con el abogado", "human")}

r_edges = {}

R = add_cluster(F, "r", "Recuperaciones", r_cluster, r_edges)

# F.add_node("SIGEFOMDES Administración", image=IMAGE_PATH + "database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Administración")
F.add_node("SISAC", image=IMAGE_PATH + "database.png", shape="plaintext", label="", xlabel="SISAC")

global_edges = {"Beneficiario":  {"c0": {"style": "dashed"}},
                "SISAC": {"c1": {"style": "dashed"}},
                "c3": {"SISAC": {"style": "dashed"}},
                "c5": {"r0": {"style": "dashed"}},
                "c7": {"cj1": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc6.png", prog='dot')
F.write("proc6.dot")
