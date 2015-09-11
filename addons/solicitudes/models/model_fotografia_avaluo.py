# -*- coding: utf-8 -*-

from openerp import models, fields, api

class fotografiaAvaluo(models.Model):
    _name = 'solicitudes.fotografia_avaluo'

    _rec_name = 'descripcion'

    avaluo_id = fields.Many2one('solicitudes.avaluo', string="avaluo")

    foto_avaluo = fields.Binary(string='Fotografia del avaluo')
    descripcion = fields.Char(string='Descripcion de la fotografia')
    fecha = fields.Date(string='Fecha')

