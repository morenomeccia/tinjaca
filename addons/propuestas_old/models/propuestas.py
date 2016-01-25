# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Propuestas(models.Model):
     _name = 'propuestas.propuestas'

     solicitante_id = fields.Many2one(comodel_name='propuestas.solicitantes', string="Solicitante")
     unidad_prod_id = fields.Many2one(comodel_name='propuestas.unidades_productivas', string="Unidad Productiva")
     actividad_prod_id = fields.Many2one(comodel_name='propuestas.actividades_productivas', string="Actividad Productiva")
     avalista_id = fields.Many2one(comodel_name='propuestas.avalistas', string="Avalista")
     garantia_id = fields.Many2one(comodel_name='propuestas.garantias', string="Garantía")
     referencias_sol_id = fields.Many2one(comodel_name='propuestas.referencias_solicitantes', string="Referencias del Solicitante")
     # referencias_aval_id = fields.Many2one(comodel_name='propuestas.referencias_avalistas', string='Referencias del Avalista')
     plan_inversion_id = fields.Many2one(comodel_name='propuestas.planes_inversion', string='Plan de Inversión')
