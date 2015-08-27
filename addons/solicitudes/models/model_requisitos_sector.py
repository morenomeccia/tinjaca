# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RequisitosSector(models.Model):
    _name = 'solicitudes.requisitos_sector'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    documentos_sector_id = fields.Many2one('solicitudes.documentos_sector', string="Tipo de Documento")
    documento = fields.Binary(string='Documento')
    observaciones = fields.Char(string='Observaciones')
    valido = fields.Boolean(string='Valido')
