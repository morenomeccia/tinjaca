# -*- coding: utf-8 -*-

from openerp import models, fields, api

class politicasFinanciamiento(models.Model):
    _name = 'fomdes.politicas_financiamiento'

    rec_name = "sector_id"    

    sector_id = fields.Many2one('fomdes.sectores', string="Sector")
    tasa_interes_promocional = fields.Float(string='Tasa de interes empresa promocional')
    tasa_interes_establecida = fields.Float(string='Tasa de interes empresa establecida')
    tasa_mora = fields.Float(string='Tasa de mora')
    comision_flat = fields.Float(string='Comision FLAT')
    aporte_social = fields.Float(string='Aporte social')
    plazo_maximo = fields.Integer(string='Plazo maximo de pago')
    monto_maximo = fields.Float(string='Monto maximo')
    monto_minimo = fields.Float(string='Monto minimo')
