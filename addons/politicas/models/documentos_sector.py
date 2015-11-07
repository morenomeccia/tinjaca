# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DocumentosSector(models.Model):
    _name = 'politicas.documentos_sector'

    _rec_name = 'tipo_documento'

    tipo_documento = fields.Char(string='Tipo de Documento')
    habilitado = fields.Boolean(string='Habilitar')

    sector_id = fields.Many2one('politicas.sectores', string="Sector")

