# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ReferenciasSolicitantes(models.Model):
    _name = 'propuestas.referencias_solicitantes'

    propuesta_id = fields.One2many('propuestas.propuestas', string="Propuesta")
    codigo_referencias = fields.Char(string='Código de las Referencias', required=True)
    nombres = fields.Char(string='Nombres del Avalista', required=True)
    apellidos = fields.Char(string='Apellidos del Avalista', required=True)
    ci = fields.Integer(string='CI del Avalista', required=True)
    direccion_habitacion = fields.Char(string='Direccion de Habitacion', required=True)
    telefono_fijo = fields.Integer(string='Telefono Fijo', required=True)
    telefono_celular = fields.Integer(string='Telefono Celular', required=True)
    codigo_solicitante = fields.Char(string='Código del Solicitante', required=True)