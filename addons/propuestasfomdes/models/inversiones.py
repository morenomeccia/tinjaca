#-*- coding: utf-8 -*-

from openerp import models, fields, api

class Inversiones(models.Model):
    _name = 'propuestasfomdes.inversiones'

    _rec_name = 'descripcion'

    propuestas_id = fields.Many2one('propuestasfomdes.propuestas', string="Propuesta")
    rubro_id = fields.Many2one('politicas.rubros', string="Rubro")

    descripcion = fields.Char(string="Descripcion")
    aporte_propio = fields.Float(string="Aporte Propio")
    aporte_fomdes = fields.Float(string="Aporte FOMDES")
