# -*- coding: utf-8 -*-

from openerp import models, fields, api

class observaciones_estaciones(models.Model):
    _name = 'solicitudes.observaciones_estaciones'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    estacion = fields.Selection(string='Estacion', related='solicitudes_id.state')
    observacion = fields.Text(string='Observacion')
	
