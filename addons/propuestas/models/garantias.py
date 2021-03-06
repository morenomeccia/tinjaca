# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Garantias(models.Model):
    _name = 'propuestas.garantias'

    _rec_name = 'descripcion'

    propuestas_id = fields.Many2one('propuestas.propuestas', "Propuesta")

    tipos_garantia_id = fields.Many2one('politicas.tipos_garantia', string="Tipo de Garantía", required=True)

    descripcion = fields.Char(string='Descripción de la Garantía')
    avaluo = fields.Char(string='Avalúo de la Garantía')


