# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DocumentosGarantia(models.Model):
    _name = 'politicas.documentos_garantia'

    _rec_name = 'tipo_documento'

    tipo_documento = fields.Char(string='Tipo de Documento')
    garantia = fields.Char(string='Garantia')
