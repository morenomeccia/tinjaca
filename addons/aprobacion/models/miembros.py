# -*- coding: utf-8 -*-

from openerp import models, fields, api

class miembros(models.Model):
    _name = 'aprobacion.miembros'

    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)	
    apellido = fields.Char(string='Apellido', required=True)	

    consejo_directivo_ids = fields.Many2many('aprobacion.consejo_directivo', string="Consejo directivo")



