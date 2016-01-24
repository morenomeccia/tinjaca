#-*- coding: utf-8 -*-

from openerp import models, fields, api

class Inversiones(models.Model):
    _name = 'propuestasfomdes.inversiones'

    _rec_name = 'descripcion'

    propuestas_id = fields.Many2one('propuestasfomdes.propuestas', string="Propuesta")
    rubro_id = fields.Many2one('politicas.rubros', string="Rubro")

    descripcion = fields.Char(string="Descripcion")
    monto_solicitado = fields.Float(string="Monto Solicitado")
    monto_recomendado = fields.Float(string="Monto recomendado")
    monto_ajustado = fields.Float(string="Monto Ajustado")
    aporte_propio = fields.Float(string="Aporte Propio")
