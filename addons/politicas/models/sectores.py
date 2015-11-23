# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Sectores(models.Model):
    _name = 'politicas.sectores'

    _rec_name = 'codigo'
    
    codigo = fields.Char(string='Codigo', required=True)
    descripcion = fields.Char(string='Descripcion')
    habilitado = fields.Boolean(string='Habilitar')

    tasa_interes_promocionales = fields.Float(string='Tasa de interes (empresas promocionales)')
    tasa_interes_establecidas = fields.Float(string='Tasa de interes (empresas establecidas)')
    tasa_mora = fields.Float(string='Tasa de mora')
    comision_flat = fields.Float(string='Comision FLAT')
    aporte_social = fields.Float(string='Aporte social')
    plazo_maximo = fields.Integer(string='Plazo maximo de pago')
    monto_maximo = fields.Float(string='Monto maximo')
    monto_minimo = fields.Float(string='Monto minimo')

