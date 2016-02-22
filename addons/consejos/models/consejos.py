# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Consejos(models.Model):
    _name = 'consejos.consejos'
    _rec_name = 'numero'

    numero = fields.Integer(string='Numero del consejo', required=True)
    fecha = fields.Datetime(string='Fecha y hora del consejo', required=True)
    agenda = fields.Text(string='Agenda')
    minuta = fields.Text(string='Minuta')

    miembros_ids = fields.Many2many('consejos.miembros', string="Miembros", relation='consejos_miembros_rel')

