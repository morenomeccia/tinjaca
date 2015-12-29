# -*- coding: utf-8 -*-

from openerp import models, fields, api


class UnidadesProductivas(models.Model):
    _name = 'propuestasfomdes.unidades_productivas'

    _rec_name = 'nombre'

    solicitantes_id = fields.Many2one('propuestasfomdes.solicitantes', string="Solicitante")

    nombre = fields.Char(string="Nombre de la Unidad Productiva")
    direccion = fields.Text(string='Dirección') # de res.partner>res.company
    telefono_fijo = fields.Integer(string='Teléfono fijo')
    telefono_celular = fields.Integer(string='Teléfono Celular')
    actividad = fields.Text(string='Actividades')
    experiencia = fields.Text(string='Experiencia')
    area_geografica = fields.Text(string='Area Geografica')
    tenencia = fields.Text(string='Tenencia')
    area_m2 = fields.Float(string='Area en metros cuadrados')
    zona_geografica = fields.Char(string='Zona Geografica')
    servicios = fields.Text(string='Servicios')

    actividades_productivas_ids = fields.One2many('propuestasfomdes.actividades_productivas', 'unidades_productivas_id', string="Actividades Productivas")