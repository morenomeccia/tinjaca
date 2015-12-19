# -*- coding: utf-8 -*-

from openerp import models, fields, api

class FotografiasAcompanamiento(models.Model):
    _name = 'acompanamiento.fotografias_acompanamiento'

    _rec_name = 'descripcion'

    inspecciones_inversion_id = fields.Many2one('acompanamiento.inspecciones_inversion', string="Inspeccion")

    descripcion = fields.Char(string='Descripcion de la fotografia')
    fecha = fields.Date(string='Fecha')
    foto_acompanamiento = fields.Binary(string='Fotografia de la inspeccion')

