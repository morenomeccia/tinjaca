# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Propuestas(models.Model):
     _name = 'propuestas.propuestas'

     solicitante_id = fields.Many2one(comodel_name='propuestas.solicitantes', string="Solicitante")
     unidad_prod_id = fields.Many2one(comodel_name='propuestas.unidades_productivas', string="Unidad Productiva")
     actividad_prod_id = fields.Many2one(comodel_name='propuestas.actividades_productivas', string="Actividad Productiva")
     # avalista_id = fields.Many2one('propuestas.avalistas', 'propuesta_id', string="Avalista")
     # garantia_id = fields.Many2one('propuestas.garantias', 'propuesta_id', string="Garantia")
     referencias_solicitante_id = fields.Many2one(comodel_name='propuestas.referencias_solicitantes', string="Referencias del Solicitante")
     # referencias_avalista_id = fields.Many2one('propuestas.referencias_avalistas', 'propuesta_id', string='Referencias del Avalista')
     plan_inversion_id = fields.Many2one(comodel_name='propuestas.planes_inversion', string='Plan de Inversión')