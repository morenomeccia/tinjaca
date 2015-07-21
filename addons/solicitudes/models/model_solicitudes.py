# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Solicitudes(models.Model):
    _name = 'solicitudes.solicitudes'

    nro_expediente = fields.Char(string='Numero de expediente', required=True)
    informe_tecnico_id = fields.One2many('solicitudes.informe_tecnico', 'solicitudes_id', string="Informe tecnico") 
