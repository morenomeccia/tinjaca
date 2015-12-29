# -*- coding: utf-8 -*-

from openerp import models, fields, api

class pagos(models.Model):
    _name = 'caja.pagos'

    monto = fields.Float(string='Monto del pago', required=True)
    fecha_pago = fields.Date(string='Fecha de pago', required=True)
    modo_pago = fields.Selection(string='Modo de pago', selection=[('pago_efectivo', 'Efectivo'),
                                                                   ('pago_debito', 'Debito'),
                                                                   ('pago_credito', 'Credito'),
                                                                   ('pago_cheque', 'Cheque'),
                                                                   ('pago_deposito', 'Deposito'),
                                                                   ('pago_transferencia', 'Transferencia')])
    exoneracion = fields.Boolean(string='Exoneracion?')

    cantidad = fields.Char() # Monto en frase !!! Calculado
    amortizacion_capital = fields.Float(string='Amortizacion de capital') # !!! Calculado
    interes_capital = fields.Float(string='Interes del capital') # !!! Calculado
    interes_mora = fields.Float(string='Interes por mora') # !!! Calculado
    concepto = fields.Char(string='Concepto de pago') # !!! Calculado

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Numero de expediente', required=True)
    #caja_id = fields.Many2one('caja.cajas', string='Numero de expediente', required=True) # !!! Obtenido del usuario?
    nro_expediente_solicitud = fields.Char(string='Número de expediente', related='solicitudes_id.nro_expediente', readonly=True)