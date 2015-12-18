-*- coding: utf-8 -*-

from openerp import models, fields, api

class Facturas(models.Model):
    _name = 'acompanamiento.facturas'

    rec_name = descripcion
    
    credito_id = fields.Many2one('administracion.creditos', string="Número de expediente")
    #rubro_id = fields.Many2one('politicas.rubros', string="Rubro")
    descripcion = fields.Char(string="Descripcion")
    monto = fields.Float(string="Monto")
    valido = fields.Boolean(string="Valida?")
    observaciones = fields.Char(string="Observaciones")