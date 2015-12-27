# -*- coding: utf-8 -*-

from openerp import models, fields, api

class pagos(models.Model):
    _name = 'solicitudes.pagos'

    monto = fields.Float(string='Monto del pago', required=True)
    fecha_pago = fields.Date(string='Fecha de pago', required=True)

    cantidad = fields.Char() # Monto en frase !!! Calculado
    capital = fields.Float(string='Abono de capital') # !!! Calculado
    interes_capital = fields.Float(string='Interes del capital') # !!! Calculado
    interes_mora = fields.Float(string='Interes por mora') # !!! Calculado
    concepto = fields.Char(string='Concepto de pago') # !!! Calculado

    creditos_id = fields.Many2one('administracion.creditos', string='Numero de expediente', required=True)
    #caja_id = fields.Many2one('caja.cajas', string='Numero de expediente', required=True) # !!! Obtenido del usuario?