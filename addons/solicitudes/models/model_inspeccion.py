# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Inspecciones(models.Model):
    _name = 'solicitudes.inspecciones'

    _rec_name = 'fecha_inspeccion'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    foto_inspeccion_id = fields.One2many('solicitudes.fotografia_inspeccion', 'inspecciones_id', string="Fotografia de la inspeccion")

    fecha_inspeccion = fields.Date(string='Fecha de inspeccion', required=True)
    tiempo_funcionamiento = fields.Float(string='Tiempo de funcionamiento', required=True)
    cantidad_productos = fields.Integer(string='Cantidad de productos')
    costos_actividad = fields.Float(string='Costo de la actividad')
    sistema_produccion = fields.Char(string='Sistema de produccion')
    clientes = fields.Char(string='Clientes', required=True)
    distribucion_espacio_fisico = fields.Char(string='Distribucion del espacio fisico')
    condicion_fisica_sanitaria = fields.Selection(string='Condicion sanitaria', selection=[('1', 'Bueno'), ('2', 'Regular'), ('3', 'Malo')]) 
    maquinaria = fields.Char(string='Maquinaria') 
    materia_prima = fields.Char(string='Materia prima') 
    observaciones = fields.Char(string='Observaciones')
    resultados_inspeccion = fields.Char(string='Resultados del avaluo')
    viabilidad_unidad_de_produccion = fields.Boolean(string='La unidad de produccion es viable')
    




