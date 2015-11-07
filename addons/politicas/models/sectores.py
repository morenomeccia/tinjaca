# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Sectores(models.Model):
    _name = 'politicas.sectores'

    _rec_name = 'codigo'
    
    codigo = fields.Char(string='Codigo', required=True)
    descripcion = fields.Char(string='Descripcion')
    habilitado = fields.Boolean(string='Habilitar')

