# -*- coding: utf-8 -*-

from openerp import models, fields, api

class politicasFinanciamiento(models.Model):
    _name = 'fomdes.politicas_financiamiento'
    
    sector_id = fields.Many2one('fomdes.sectores', string="Sector")
    porcentaje_promocional = fields.Float(string='Porcentaje promocional')
    porcentaje_establecido = fields.Float(string='Porcentaje establecido')
    tasa_mora = fields.Float(string='Tasa de mora')
    comision_flat = fields.Float(string='Comision FLAT')
    aporte_social = fields.Float(string='Aporte social')
    

