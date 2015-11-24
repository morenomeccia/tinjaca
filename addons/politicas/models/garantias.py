# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Garantias(models.Model):
    _name = 'politicas.garantias'

    _rec_name = 'codigo'

    codigo = fields.Char(string='Codigo',required=True)
    descripcion = fields.Char(string='Descripcion')
    habilitado = fields.Boolean(string='Habilitar')



