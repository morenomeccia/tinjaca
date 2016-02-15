# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TiposGarantia(models.Model):
    _name = 'politicas.tipos_garantia'

    _rec_name = 'codigo'

    codigo = fields.Char(string='Codigo',required=True)
    descripcion = fields.Char(string='Descripcion')
    habilitado = fields.Boolean(string='Habilitar')



