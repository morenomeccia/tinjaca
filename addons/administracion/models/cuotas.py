# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Cuotas(models.Model):
    _name = 'administracion.cuotas'
    _rec_name = 'nro_expediente'


    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Número de expediente')
    creditos_id = fields.Many2one('administracion.creditos', string='Datos del crédito')
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento')
    int_capital = fields.Float(string='Interés de Capital')
    amort_capital = fields.Float(string='Amortización de Capital')
    mensualidad = fields.Float(string='Mensualidad')
    saldo_pendiente = fields.Float(string='Saldo Pendiente')


