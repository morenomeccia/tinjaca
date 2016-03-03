# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Consejos(models.Model):
    _inherit = 'consejos.consejos'

    solicitudes_ids = fields.Many2many('solicitudes.solicitudes', string="Solicitudes", relation='consejos_consejos_solicitudes_rel')
