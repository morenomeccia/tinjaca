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

PROCESS_LABEL = "Recepción y Evaluación de Solicitudes 2"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

ae_cluster = {"ae0": ("Recibir Expediente", "start"),
              "ae1": ("Planificar las rutas", "human"),
              "ae2": ("Realizar la Inspección", "human"),
              "ae3": ("¿Requiere Garantía?", "exclusive"),
              "ae4": ("Realizar avalúo de la garantía", "human"),
              "ae5": ("", "exclusive"),
              "ae6": ("Realizar Informe Técnico", "human"),
              "ae7": ("Enviar Expediente al Gerente de Crédito", "message"),
              "ae8": ("", "end")}

ae_edges = {"ae0": {"ae1": {}},
            "ae1": {"ae2": {}},
            "ae2": {"ae3": {}},
            "ae3": {"ae4": {"xlabel": "Si"}, "ae5": {"xlabel": "No"}},
            "ae4": {"ae5": {}},
            "ae5": {"ae6": {}},
            "ae6": {"ae7": {}},
            "ae7": {"ae8": {}}}

AE = add_cluster(F, "ae", "Análisis Económico", ae_cluster, ae_edges)

gc_cluster = {"gc0": ("Recibir Expediente", "start"),
              "gc1": ("Revisión del Expediente", "human"),
              "gc2": ("Dictamen del Informe Técnico", "complex"),
              "gc3": ("Enviar Expediente a Secretaría Ejecutiva", "message"),
              "gc4": ("", "end")}

gc_edges = {"gc0": {"gc1": {}},
            "gc1": {"gc2": {}},
            "gc2": {"gc3": {"xlabel": "Aprobado"}},
            "gc3": {"gc4": {}}}

GC = add_cluster(F, "gc", "Gerencia de Crédito", gc_cluster, gc_edges)

F.add_node("SIGEFOMDES Crédito", image="static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Crédito")

global_edges = {"Ánálisis Jurídico": {"ae0": {"style": "dashed"}},
                "ae7": {"gc0": {"style": "dashed"}},
                "ae0": {"gc0": {"style": "invis"}},
                "ae2": {"SIGEFOMDES Crédito": {"style": "dashed"}},
                "ae4": {"SIGEFOMDES Crédito": {"style": "dashed"}},
                "ae6": {"SIGEFOMDES Crédito": {"style": "dashed"}},
                "SIGEFOMDES Crédito": {"gc1": {"style": "dashed"}},}

add_edges(F, global_edges)

F.draw("proc22.png", prog='dot')
F.write("proc22.dot")
