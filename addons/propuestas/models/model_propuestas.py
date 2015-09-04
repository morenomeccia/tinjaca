# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Propuestas(models.Model):
     _name = 'propuestas.propuestas'

     solicitante_id = fields.Many2one('propuestas.solicitantes', 'propuesta_id', string="Solicitante")
     unidad_prod_id = fields.Many2one('propuestas.unidades_productivas', 'propuesta_id', string="Unidad Productiva")
     actividad_prod_id = fields.Many2one('propuestas.actividades_productivas', 'propuesta_id', string="Actividad Productiva")
     # avalista_id = fields.Many2one('propuestas.avalistas', 'propuesta_id', string="Avalista")
     # garantia_id = fields.Many2one('propuestas.garantias', 'propuesta_id', string="Garantia")
     referencias_solicitante_id = fields.Many2one('propuestas.referencias_solicitantes', 'propuesta_id', string="Referencias del Solicitante")
     # referencias_avalista_id = fields.Many2one('propuestas.referencias_avalistas', 'propuesta_id', string='Referencias del Avalista')
     plan_inversion_id = fields.Many2one('propuestas.planes_inversion', 'propuesta_id', string='Plan de Inversión')