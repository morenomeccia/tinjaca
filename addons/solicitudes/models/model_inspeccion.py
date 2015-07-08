# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class inspecciones(models.Model):
    _name = 'solicitudes.inspecciones'

    nro_expediente = fields.Char(string='Numero de expediente', required=True) # !!!
    tiempo_funcionamiento = fields.Date(string='Tiempo de funcionamiento', required=True)
    cantidad_productos = fields.Integer(string='Cantidad de productos', required=True)
    costos_actividad = fields.Float(string='Costo de la actividad', required=True)
    sistema_produccion = fields.Char(string='Sistema de produccion', required=True)
    clientes = fields.Char(string='Clientes', required=True)
    distribucion_espacio_fisico = fields.Char(string='Distribucion del espacio fisico', required=True)
    condicion_fisica_sanitaria = fields.Char(string='Condicion sanitaria', required=True) # !!!
    maquinaria = fields.Char(string='Maquinaria', required=False) 
    materia_prima = fields.Char(string='Materia prima', required=True) 
    observaciones = fields.Char(string='Observaciones', required=True)
    firma = fields.binary(string='Firma del beneficiario', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)
