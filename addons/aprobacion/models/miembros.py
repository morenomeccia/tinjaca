# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Miembros(models.Model):
    _name = 'aprobacion.miembros'
    _rec_name = 'cedula'

    cedula = fields.Char(string='Cedula', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)	

    # referencias al modelo de consejo directivo
    consejos_ids = fields.Many2many('aprobacion.consejos', string="Consejos directivos", relation='consejos_miembros')



