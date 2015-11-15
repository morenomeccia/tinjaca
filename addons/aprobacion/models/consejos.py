# -*- coding: utf-8 -*-

from openerp import models, fields, api

class consejos(models.Model):
    _name = 'aprobacion.consejos'
    _rec_name = 'numero'

    codigo = fields.Integer(string='Codigo del consejo')
    numero = fields.Integer(string='Numero del consejo')
    fecha = fields.Datetime(string='Fecha y hora del consejo')
    minuta = fields.Text(string='Fecha y hora del consejo')

    # Referencias a solicitudes
    solicitudes_ids = fields.Many2many('solicitudes.solicitudes', string="Numero de expediente")
    # Referencias a miembros o asistentes
    miembros_ids = fields.Many2many('aprobacion.miembros', string="Miembro")

