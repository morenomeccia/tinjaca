# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Facturas(models.Model):
    _name = 'acompanamiento.facturas'

    _rec_name = 'descripcion'
    
    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente", required=True)
    rubro_id = fields.Many2one('politicas.rubros', string="Rubro")
    descripcion = fields.Char(string="Descripcion")
    monto = fields.Float(string="Monto")
    valido = fields.Boolean(string="Valida?")
    observaciones = fields.Char(string="Observaciones")