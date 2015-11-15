# -*- coding: utf-8 -*-

from openerp import models, fields, api

class miembros(models.Model):
    _name = 'aprobacion.miembros'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)	
    apellido = fields.Char(string='Apellido', required=True)	

    # referencias al modelo de consejo directivo
    #consejos_ids = fields.Many2many('aprobacion.consejo', string="Consejo directivo")



