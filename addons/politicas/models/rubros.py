# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Rubros(models.Model):
    _name = 'politicas.rubros'

    _rec_name = 'descripcion'

    descripcion = fields.Char(string="Descripcion")
    habilitado = fields.Boolean(string='Habilitar')

    sector_ids = fields.Many2many('politicas.sectores', string="Sectores")

