# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DocumentosEmpresa(models.Model):
    _name = 'solicitudes.documentos_empresa'

    _rec_name = 'tipo_documento'

    tipo_documento = fields.Char(string='Tipo de Documento')
    empresa = fields.Char(string='Empresa')
