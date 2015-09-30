# -*- coding: utf-8 -*-

from openerp import models, fields, api

class controlPrevio(models.Model):
    _name = 'solicitudes.control_previo'

    _rec_name = 'fecha_elaboracion'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")

    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', required=True)
    descripcion_garantia = fields.Char(string='Descripcion de la garantia')
    estatus_analisis_juridico = fields.Selection(string='Estatus en analisis juridico', selection=[('1', 'Cumple'), ('2', 'No cumple'), ('3', 'Cumple condicionado')])
    observaciones = fields.Char(string='Observaciones')

