# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class pagos(models.Model):
    _name = 'solicitudes.pagos'

    concepto = fields.Char(string='Concepto de pago', required=True) # !!!
    total = fields.Float(string='Total del pago', required=True)
    interes_capital = fields.Float(string='Interes del capital', required=True)
    interes_mora = fields.Float(string='Interes por mora', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)