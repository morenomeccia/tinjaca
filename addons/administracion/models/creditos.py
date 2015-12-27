# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Creditos(models.Model):
    _name = 'administracion.creditos'
    _rec_name = 'nro_expediente_solicitudes'

    fecha_liquidacion = fields.Date(string='Fecha de liquidacion', required=True)
    fecha_ultima = fields.Date(string='Fecha ultima de pago', required=True) #calculado

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string = "Numero de Expediente")

    nro_expediente_solicitudes = fields.Char(string='Numero de Expediente', related='solicitudes_id.nro_expediente', readonly=True)
