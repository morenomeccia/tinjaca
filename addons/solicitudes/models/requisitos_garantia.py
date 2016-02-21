# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RequisitosGarantia(models.Model):
    _name = 'solicitudes.requisitos_garantia'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    documentos_garantia_id = fields.Many2one('politicas.documentos_garantia', string="Tipo de Documento")
    documento = fields.Binary(string='Documento')
    observaciones = fields.Char(string='Observaciones')
    valido = fields.Boolean(string='Valido')

    solicitudes_tipos_garantia_id = fields.Many2one(string='Garantia', related='solicitudes_id.propuestas_tipos_garantia_id', readonly=True)
