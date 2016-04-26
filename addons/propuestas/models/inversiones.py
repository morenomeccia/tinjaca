#-*- coding: utf-8 -*-

from openerp import models, fields, api

class Inversiones(models.Model):
    _name = 'propuestas.inversiones'

    _rec_name = 'descripcion'

    propuestas_id = fields.Many2one('propuestas.propuestas', string="Propuesta")
    rubros_id = fields.Many2one('politicas.rubros', string="Rubro")

    descripcion = fields.Char(string="Descripcion")
    aporte_propio = fields.Float(string="Aporte Propio")
    aporte_fomdes = fields.Float(string="Aporte FOMDES")
