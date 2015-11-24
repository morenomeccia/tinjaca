# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Talleres(models.Model):
    _name = 'solicitudes.talleres'

    fecha = fields.Date(string='Fecha', required=True)
