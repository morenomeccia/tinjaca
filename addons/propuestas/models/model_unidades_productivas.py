# -*- coding: utf-8 -*-

from openerp import models, fields, api


class UnidadProductiva(models.Model):
    _name = 'propuestas.unidad_productiva'
    _inherit = 'res.company'

    codigo_up = fields.Char(string='Código de la Solicitud', required=True)
    nombre_up = fields.Char(string='Nombres del Solicitante', required=True)
    direccion_up = fields.Char(string='Apellidos del Solicitante', required=True)
    telefono_fijo = fields.Integer(string='Telefono fijo', required=True)
    telefono_celular = fields.Integer(string='Telefono Celular', required=True)
    actividad = fields.Char(string='Actividad', required=True)
    experiencia = fields.Char(string='Experiencia', required=True)
    area_geografica = fields.Char(string='Area Geografica', required=True)
    tenencia = fields.Char(string='Tenencia', required=True)
    area_m2 = fields.Integer(string='Area en metros cuadrados', required=True)
    zona_geografica = fields.Char(string='Zona Geografica', required=True)
    servicios = fields.Char(string='Servicios', required=True)

    @api.model
    def create(self, values):
        return super(UnidadProductiva, self).create(values)
