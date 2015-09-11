# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Garantia(models.Model):
    _name = 'propuestas.garantia'

    propuesta_id = fields.One2many('propuestas.propuestas', "garantia_id", "Propuesta")
    codigo_garantia = fields.Char(string='Código de la Garantía', required=True)
    numero_expediente = fields.Char(string='Número del Expediente', required=True)
    tipo_garantia = fields.Char(string='Garantia a ofrecer', required=True)
    descripcion = fields.Char(string='Descripción de la Garantía', required=True)
    avaluo = fields.Char(string='Avalúo de la Garantía', required=True)
    codigo_credito = fields.Char(string='Código del Crédito', required=True)

