# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DocumentosSector(models.Model):
    _name = 'solicitudes.documentos_sector'

    _rec_name = 'tipo_documento'

    tipo_documento = fields.Char(string='Tipo de Documento')
    sector = fields.Char(string='Sector')