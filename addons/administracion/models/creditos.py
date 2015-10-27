# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Creditos(models.Model):
    _name = 'solicitudes.creditos'

    fecha_liquidacion = fields.Date(string='Fecha de liquidacion', required=True)
    fecha_ultima = fields.Date(string='Fecha ultima', required=True) #calculado
