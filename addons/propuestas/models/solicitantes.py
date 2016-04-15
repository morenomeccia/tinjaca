# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Solicitantes(models.Model):
    _name = 'propuestas.solicitantes'
    _inherit = 'contactos.personas'

    familiares_ids = fields.One2many('propuestas.familiares', 'solicitantes_id',string="Familiares")
    conyuges_ids = fields.One2many('propuestas.conyuges', 'solicitantes_id',string="Conyuges")
    unidades_productivas_ids = fields.One2many('propuestas.unidades_productivas', 'solicitantes_id', string="Unidad Productiva")
    propuestas_ids = fields.One2many('propuestas.propuestas', 'solicitantes_id', string="Propuesta")

