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

PROCESS_LABEL = "Aprobación de Créditos"
# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="", rankdir="TB", splines="ortho", labelloc="b",
                    size="8, 7.5", forcelabels="true", ranksep="0.25", fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

se_cluster = {"se0": ("Recibir Lista de Expedientes", "start"),
              "se1": ("Verificar Lista de Expedientes", "human"),
              "se2": ("Solicitar Certificación Presupuestaria y Financiera", "message"),
              "se3": ("Convocar el Consejo Directivo", "message"),
              "se4": ("Elaborar el Acta de Créditos Aprobados", "human"),
              "se5": ("Elaborar el Documento de Credito (Documento de Empresa)", "human"),
              "se6": ("", "end")}

se_edges = {"se0": {"se1": {}},
            "se1": {"se2": {}},
            "se2": {"se3": {"style": "invis"}},
            "se3": {"se4": {"style": "invis"}},
            "se4": {"se5": {}},
            "se5": {"se6": {}}}

SE = add_cluster(F, "se", "Secretaría Ejecutiva", se_cluster, se_edges)

p_cluster = {"p0": ("Verificar Lista de Expedientes", "human")}

p_edges = {}

P = add_cluster(F, "p", "Presidencia", p_cluster, p_edges)

pr_cluster = {"pr0": ("Elaborar Certificación Presupuestaria y Financiera", "human"),
              "pr1": ("Enviar Certificación a Secretaría Ejecutiva", "message")}

pr_edges = {"pr0": {"pr1": {}}}

PR = add_cluster(F, "pr", "Presupuesto/Administración", pr_cluster, pr_edges)

cd_cluster = {"cd0": ("Revisar los expedientes", "human"),
              "cd1": ("¿Se aprueba el crédito?", "complex")}

cd_edges = {"cd0": {"cd1": {}}}

CD = add_cluster(F, "cd", "Consejo Directivo", cd_cluster, cd_edges)

# F.add_node("SIGEFOMDES Crédito", image="_static/database.png", shape="plaintext", label="", xlabel="SIGEFOMDES Crédito")

global_edges = {"Gerencia de Crédito":  {"se0": {"style": "dashed"}},
                "p0": {"se1": {"style": "dashed"}},
                "se2": {"pr0": {"style": "dashed"}},
                "pr1": {"se3": {"style": "dashed"}},
                "se3": {"cd0": {"style": "dashed"}},
                "cd1": {"se4": {"style": "dashed"}},
                "se5": {"Usuario": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("proc3.png", prog='dot')
F.write("proc3.dot")
