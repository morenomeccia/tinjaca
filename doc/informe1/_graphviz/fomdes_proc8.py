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

PROCESS_LABEL = "Liquidación de Créditos"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

ad_cluster = {"ad0": ("Recibir cancelación total", "start"),
              "ad1": ("Verificar estatus de cuenta", "human"),
              "ad2": ("Solicitar liberación de crédito", "human"),
              "ad3": ("Entregar documento al beneficiario", "message"),
              "ad4": ("", "end")}

ad_edges = {"ad0": {"ad1": {}},
            "ad1": {"ad2": {}},
            "ad2": {"ad3": {"style": "invis"}},
            "ad3": {"ad4": {}}}

AD = add_cluster(F, "ad", "Administración", ad_cluster, ad_edges)

cj_cluster = {"cj2": ("Redactar documento de liberación", "human")}

cj_edges = {}

CJ = add_cluster(F, "cj", "Consultoría Jurídica", cj_cluster, cj_edges)

p_cluster = {"p3": ("Firmar documento de liberación", "human"),}

p_edges = {}

P = add_cluster(F, "p", "Presidencia", p_cluster, p_edges)

#F.add_node("SIGEFOMDES Administración", image="_static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Administración")
F.add_node("SISAC", image="_static/database.png", shape="plaintext", label="", xlabel="SISAC")

global_edges = {"Caja": {"ad0": {"style": "dashed"}},
                "SISAC": {"ad1": {"style": "dashed"}},
                "ad2": {"cj2": {"style": "dashed"}},
                "cj2": {"p3": {"style": "dashed"}},
                "p3": {"ad3": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc8.png", prog='dot')
F.write("proc8.dot")
