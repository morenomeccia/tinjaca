# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Sectores(models.Model):
    _name = 'politicas.sectores'

    _rec_name = 'sector'
    
    sector = fields.Char(string='Sector', required=True)
    habilitado = fields.Boolean(string='Habilitado')

