# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Propuestas(models.Model):
     _name = 'propuestas.propuestas'

     solicitante_id = fields.Many2one('propuestas.solicitantes', string="Solicitante")
     unidad_prod_id = fields.Many2one('propuestas.unidades_productivas', string="Unidad Productiva")
     actividad_prod_id = fields.Many2one('propuestas.actividades_productivas', string="Actividad Productiva")
