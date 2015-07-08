# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class estadosCuenta(models.Model):
    _name = 'solicitudes.EstadosCuenta'

    monto_total = fields.Float(string='Monto total', required=True) # !!!
    monto_cuota = fields.Float(string='Monto de la cuota', required=True)
    periodos_gracia = fields.Integer(string='Periodo de gracia', required=True)
    periodo_pago = fields.Integer(string='Periodo de pago', required=True)
    tasas_interes = fields.Float(string='Tasas de interes', required=True)
    interes_mora = fields.Float(string='Interes por mora', required=True)
    fecha_liquidacion = fields.Date(string='Fecha de liquidacion', required=True)
    fecha_ultima = fields.Date(string='Fecha ultima', required=True)