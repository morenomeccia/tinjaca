# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Consejos(models.Model):
    _name = 'aprobacion.consejos'
    _rec_name = 'numero'

    numero = fields.Integer(string='Numero del consejo')
    fecha = fields.Datetime(string='Fecha y hora del consejo')
    minuta = fields.Text(string='Minuta')

    # Referencias a solicitudes
    #solicitudes_ids = fields.Many2many('solicitudes.solicitudes', string="Numero de expediente")
    # Referencias a miembros o asistentes
    miembros_ids = fields.Many2many('aprobacion.miembros', string="Miembros", relation='consejos_miembros')

