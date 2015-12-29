# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Talleres(models.Model):
    _name = 'propuestasfomdes.talleres'

    codigo = fields.Char(string="Codigo del taller")
    fecha = fields.Date(string='Fecha', required=True)
    responsable = fields.Char(string="Responsable")
