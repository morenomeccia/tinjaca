#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

__author__ = 'mapologo'

import pygraphviz as pgv
from textwrap import fill

LABEL_TEMPLATE = """<<TABLE border="0" cellborder="0">
<TR><TD align="left"><IMG SRC="{}"/></TD></TR>
<TR><TD>{}</TD></TR>
</TABLE>>"""

TITLE_TEMPLATE = "<<B>{}</B>>"

GATE_TEMPLATE = '<<IMG SRC="{}"/>>'

ACTIV_ICON = {"human": "person.png", "message": "envelope.png"}

EV_STYLE = {"start": "filled", "end": "filled, bold"}

def add_event(G, node, xlabel, ev_type):
    G.add_node(node, label="", xlabel=fill(xlabel, 20), shape="circle", width="0.6",
               style=EV_STYLE[ev_type], fillcolor="white:grey", fontsize="10")

def add_activity(G, node, label, act_type):
    label = fill(label, 20)
    label = label.replace('\n', '<br/>')
    label = LABEL_TEMPLATE.format(ACTIV_ICON[act_type], label)
    G.add_node(node, label=label, shape="box", style="rounded,filled", fillcolor="white:grey")

GATE_ICON = {"exclusive": "cross.png",
             "complex": "asterisk.png"}

def add_gateway(G, node, xlabel, gate_type):
    G.add_node(node, label="", image=GATE_ICON[gate_type], xlabel=xlabel, shape="diamond",
               style="filled", fillcolor="white:grey", fontsize="10")

ADD_ELEM = {"start": add_event,
            "end": add_event,
            "human": add_activity,
            "message": add_activity,
            "exclusive": add_gateway,
            "complex": add_gateway}

def add_edges(G, edge_list):
    for orig, dests in edge_list.items():
        for dest, attrs in dests.items():
            G.add_edge(orig, dest)
            if attrs:
                E = G.get_edge(orig, dest)
                for (k, v) in attrs.items():
                    E.attr[k] = v
    return(G)

def add_cluster(G, name, label, cluster_nodes, cluster_edges):
    name = "cluster_" + name
    nodes = cluster_nodes.keys()
    G.add_subgraph(nodes, name)
    S = G.get_subgraph(name)
    S.graph_attr.update(label=TITLE_TEMPLATE.format(label), labeljust="l")
    for node, (label, node_type) in cluster_nodes.items():
        ADD_ELEM[node_type](S, node, label, node_type)
    add_edges(S, cluster_edges)
    return(S)

# A graph for FOMDES processes
F = pgv.AGraph(strict=False, directed=True)

F.graph_attr.update(label="Diagrama de Procesos FOMDES", rankdir="LR", splines="ortho",
                    fontname="Liberation Sans Narrow Condensed")
F.node_attr.update(fontname="Liberation Sans Narrow Condensed")
F.edge_attr.update(fontname="Liberation Sans Narrow Condensed", fontsize="10")

u_cluster = {"u0": ("Propuesta de Financiamiento", "start"),
             "u1": ("Descargar Propuesta de Financiamiento", "human"),
             "u2": ("Introducir Propuesta de Financiamiento", "message"),
             "u3": ("Fin Propuesta de Financiamiento", "end"),
             "u4": ("Recibir Requisitos", "start"),
             "u5": ("Reunir Requisitos", "human"),
             "u6": ("Consignar los Requisitos", "message"),
             "u7": ("Fin Requisitos", "end")}

u_edges = {"u0": {"u1": {}},
           "u1": {"u2": {}},
           "u2": {"u3": {}},
           "u3": {},
           "u4": {"u5": {}},
           "u5": {"u6": {}},
           "u6": {"u7": {}},
           "u7": {}}

U = add_cluster(F, "u", "Usuario / Beneficiario", u_cluster, u_edges)

ic_cluster = {"ic0": ("Recibir Propuesta de Financiamiento", "start"),
              "ic1": ("Evaluar viabilidad de la Propuesta", "human"),
              "ic2": ("¿La propuesta es viable?", "exclusive"),
              "ic3": ("", "end"),
              "ic4": ("Recibir Requisitos", "start"),
              "ic5": ("Crear Expediente", "human"),
              "ic6": ("Entrevista con el usuario", "human"),
              "ic7": ("", "end")}

ic_edges = {"ic0": {"ic1": {}},
            "ic1": {"ic2": {}},
            "ic2": {"ic3": {"xlabel": "No"}},
            "ic4": {"ic5": {}},
            "ic5": {"ic6": {}},
            "ic6": {"ic7": {"style":"invis"}}}

IC = add_cluster(F, "ic", "Información de Crédito", ic_cluster, ic_edges)

er_cluster = {"er0": ("Añadir al usuario a la lista del taller", "human"),
              "er1": ("Enviar Planilla de Requisitos", "message")}

er_edges = {"er0": {"er1": {}}}

ER = add_cluster(F, "er", "Estadística y Evaluación de Riesgos", er_cluster, er_edges)

aj_cluster = {"aj0": ("Verificar validez legal de los requisitos", "human"),
              "aj1": ("Elaborar Informe de Control Previo", "human"),
              "aj2": ("¿La garantía cumple?", "exclusive"),
              "aj3": ("Enviar Expediente a Análisis Económico", "message")}

aj_edges = {"aj0": {"aj1": {}},
            "aj1": {"aj2": {}},
            "aj2": {"aj3": {"xlabel": "Si"}}}

AJ = add_cluster(F, "aj", "Análisis Jurídico", aj_cluster, aj_edges)

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

global_edges = {"u2":  {"ic0": {"style": "dashed"}},
                "ic2": {"er0": {"xlabel": "Si", "style": "dashed"}},
                "er1": {"ic3": {"style": "dashed"}, "u4": {"style": "dashed"}},
                "u6":  {"ic4": {"style": "dashed"}},
                "ic6": {"aj0": {"style": "dashed"}},
                "aj3": {"ic7": {"style": "dashed"}, "ae0": {"style": "dashed"}},
                "ae7": {"gc0": {"style": "dashed"}}}

add_edges(F, global_edges)

F.draw("bpmn_fomdes_pgv.png", prog='dot')
F.write("bpmn_fomdes_pgv.dot")


