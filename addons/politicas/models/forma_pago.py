# -*- coding: utf-8 -*-

from openerp import models, fields, api

class FormaPago(models.Model):
    _name= 'politicas.forma_pago'

    _rec_name='descripcion'

    descripcion = fields.Char(string='Descripcion')
    nro_meses = fields.Integer(string='Cantidad en meses')
    habilitado = fields.Boolean(string='Habilitado')

