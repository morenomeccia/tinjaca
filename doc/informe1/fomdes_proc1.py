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

PROCESS_LABEL = "Recepción de Propuestas"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

u_cluster = {"u0": ("Propuesta de Financiamiento", "start"),
             "u1": ("Descargar Propuesta de Financiamiento", "human"),
             "u2": ("Introducir Propuesta de Financiamiento", "message"),
             "u3": ("Fin Propuesta de Financiamiento", "end")}

u_edges = {"u0": {"u1": {}},
           "u1": {"u2": {}},
           "u2": {"u3": {}},
           "u3": {}}

U = add_cluster(F, "u", "Usuario / Beneficiario", u_cluster, u_edges)

ic_cluster = {"ic0": ("Recibir Propuesta de Financiamiento", "start"),
              "ic1": ("Evaluar viabilidad de la Propuesta", "human"),
              "ic2": ("¿La propuesta es viable?", "exclusive"),
              "ic3": ("", "end")}

ic_edges = {"ic0": {"ic1": {}},
            "ic1": {"ic2": {}},
            "ic2": {"ic3": {"xlabel": "No"}}}

IC = add_cluster(F, "ic", "Información de Crédito", ic_cluster, ic_edges)

er_cluster = {"er0": ("Añadir al usuario a la lista del taller", "human"),
              "er1": ("Enviar Planilla de Requisitos", "message")}

er_edges = {"er0": {"er1": {}}}

ER = add_cluster(F, "er", "Estadística y Evaluación de Riesgos", er_cluster, er_edges)

F.add_node("Webadmin", image="static/database.png", shape="plaintext", label="", xlabel="Webadmin")

global_edges = {"u2":  {"ic0": {"style": "dashed"}},
                "ic2": {"er0": {"xlabel": "Si", "style": "dashed"}},
                "er1": {"ic3": {"style": "dashed"}, "Usuario": {"style": "dashed"}},
                "ic1": {"Webadmin": {"style": "dashed"}},
                "Webadmin": {"er0": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc1.png", prog='dot')
F.write("proc1.dot")
