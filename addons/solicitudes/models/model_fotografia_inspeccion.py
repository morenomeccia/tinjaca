# -*- coding: utf-8 -*-

from openerp import models, fields, api

class fotografiaInspecciones(models.Model):
    _name = 'solicitudes.fotografia_inspeccion'

    _rec_name = 'descripcion'

    inspecciones_id = fields.Many2one('solicitudes.inspecciones', string="Inspeccion")

    foto_inspeccion = fields.Binary(string='Fotografia de la inspeccion')
    descripcion = fields.Char(string='Descripcion de la fotografia')
    fecha = fields.Date(string='Fecha')

