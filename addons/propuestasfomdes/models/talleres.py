# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Taller(models.Model):
    _name = 'propuestasfomdes.taller'

    _rec_name = 'fecha'

    fecha = fields.Date(string='Fecha', required=True)

    propuestas_ids = fields.Many2many('propuestasfomdes.propuestas', string="Propuestas")
