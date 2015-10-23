# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DocumentosGenerales(models.Model):
    _name = 'politicas.documentos_generales'

    _rec_name = 'tipo_documento'

    tipo_documento = fields.Char(string='Tipo de Documento')
