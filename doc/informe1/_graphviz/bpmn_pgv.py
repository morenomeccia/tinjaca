#!/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
BPMN PGV generates BPMN diagrams from graphviz using pygraphviz. This is an early alpha, usable but lacks many features
and configuration flexibility.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

__author__ = 'mapologo'

import pygraphviz as pgv
from textwrap import fill

IMAGE_PATH = "_static/"

LABEL_TEMPLATE = """<<TABLE border="0" cellborder="0">
                <TR><TD align="left"><IMG SRC="{}"/></TD></TR>
                <TR><TD>{}</TD></TR>
                </TABLE>>"""

TITLE_TEMPLATE = "<<B>{}</B>>"

GATE_TEMPLATE = """<<TABLE border="0" cellborder="0" cellpadding="0">
                <TR><TD><IMG SRC="{}"/></TD></TR>
                </TABLE>>"""

ACTIV_ICON = {"human": IMAGE_PATH + "person.png",
              "message": IMAGE_PATH + "envelope.png"}

EV_STYLE = {"start": "filled", "end": "filled, bold"}

TEXT_WIDTH = 25

def add_event(G, node, xlabel, ev_type):
    """
    Add an event node to G with label xlabel and event type ev_type.

    :param G: a pygraphviz AGraph.
    :param node: a string or string convertable.
    :param xlabel: a string used as identifier.
    :param ev_type: a string used as EV_STYLE key.
    :return: None
    """
    G.add_node(node, label="", xlabel=fill(xlabel, TEXT_WIDTH), shape="circle", width="0.6",
               style=EV_STYLE[ev_type], fillcolor="white:grey", fontsize="10")

def add_activity(G, node, label, act_type):
    """
    Add an activity node to G with label and activity type act_type.

    :param G: a pygraphviz AGraph.
    :param node: a string or string convertable.
    :param label: a string used as identifier.
    :param act_type: a string used as ACTIV_ICON key.
    :return: None
    """
    label = fill(label, TEXT_WIDTH)
    label = label.replace('\n', '<br/>')
    label = LABEL_TEMPLATE.format(ACTIV_ICON[act_type], label)
    G.add_node(node, label=label, shape="box", style="rounded,filled", fillcolor="white:grey")

GATE_ICON = {"exclusive": IMAGE_PATH + "cross.png",
             "complex": IMAGE_PATH + "asterisk.png"}

def add_gateway(G, node, xlabel, gate_type):
    """
    Add a gateway node to G with xlabel and gate type gate_type.

    :param G: a pygraphviz AGraph.
    :param node: a string or string convertable.
    :param xlabel: a string used as identifier.
    :param gate_type: a string used as GATE_ICON key.
    :return:
    """
    G.add_node(node, label=GATE_TEMPLATE.format(GATE_ICON[gate_type]), xlabel=xlabel, shape="diamond",
               style="filled", fillcolor="white:grey", fontsize="10", width="1", height="1", fixedsize="true")

ADD_ELEM = {"start": add_event,
            "end": add_event,
            "human": add_activity,
            "message": add_activity,
            "exclusive": add_gateway,
            "complex": add_gateway}

def add_edges(G, edge_list):
    """
    Add edges to G given by edge_list

    :param G:
    :param edge_list: A dict of dicts of dicts. A dict of origin nodes which has a dict of destination nodes which has
     a dict of attributes.
    :return: updated G
    """
    for orig, dests in edge_list.items():
        for dest, attrs in dests.items():
            G.add_edge(orig, dest)
            if attrs:
                E = G.get_edge(orig, dest)
                for (k, v) in attrs.items():
                    E.attr[k] = v
    return(G)

def add_cluster(G, name, label, cluster_nodes, cluster_edges):
    """
    Add a cluster subgraph to G with name "cluster_" + name and label. Comprehends a cluster_nodes bunch of nodes
    connected internally with cluster_edges.

    :param G: a pygraphviz AGraph.
    :param name: a string or string convertable.
    :param label: a string used as identifier, will be converted to "cluster_" + name.
    :param cluster_nodes: A list of str.
    :param cluster_edges: A dict of dicts of dicts. A dict of origin nodes which has a dict of destination nodes which
     has a dict of attributes.
    :return:
    """
    name = "cluster_" + name
    nodes = cluster_nodes.keys()
    G.add_subgraph(nodes, name)
    S = G.get_subgraph(name)
    S.graph_attr.update(label=TITLE_TEMPLATE.format(label), labeljust="l")
    for node, (label, node_type) in cluster_nodes.items():
        ADD_ELEM[node_type](S, node, label, node_type)
    add_edges(S, cluster_edges)
    return(S)



