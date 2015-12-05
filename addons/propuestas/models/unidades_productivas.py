# -*- coding: utf-8 -*-

from openerp import models, fields, api


class UnidadProductiva(models.Model):
    _name = 'propuestas.unidad_productiva'
    _inherit = 'res.company'

    solicitante_id = fields.Many2one(comodel_name='propuestas.solicitantes', string="Solicitante")
    propuesta_id = fields.One2many('propuestas.propuestas', "unidad_prod_id", string="Propuesta")
    street = fields.Char(string='Dirección') # de res.partner>res.company
    street2 = fields.Char(string='Dirección cont.') # de res.partner>res.company
    telefono_fijo = fields.Integer(string='Teléfono fijo')
    telefono_celular = fields.Integer(string='Teléfono Celular')
    actividad = fields.Char(string='Actividad')
    experiencia = fields.Char(string='Experiencia')
    area_geografica = fields.Char(string='Area Geografica')
    tenencia = fields.Char(string='Tenencia')
    area_m2 = fields.Integer(string='Area en metros cuadrados')
    zona_geografica = fields.Char(string='Zona Geografica')
    servicios = fields.Char(string='Servicios')

    @api.model
    def create(self, values):
        return super(UnidadProductiva, self).create(values)
