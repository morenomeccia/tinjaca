-*- coding: utf-8 -*-

from openerp import models, fields, api

class Avalistas(models.Model):
    _name = 'propuestas.avalistas'

    propuesta_id = fields.One2many('propuestas.propuestas', string="Propuesta")
    codigo_avalista = fields.Char(string='Código del Avalista', required=True)
    nombres = fields.Char(string='Nombres del Avalista', required=True)
    apellidos = fields.Char(string='Apellidos del Avalista', required=True)
    ci = fields.Integer(string='CI del Avalista', required=True)
    direccion_habitacion = fields.Char(string='Direccion de Habitacion', required=True)
    telefono_fijo = fields.Integer(string='Telefono Fijo', required=True)
    telefono_celular = fields.Integer(string='Telefono Celular', required=True)
    correo_electronico = fields.Char(string='Correo Electronico', required=True)
    nombre_direccion_trabajo = fields.Char(string='Nombre y Dirección de Trabajo', required=True)
    cargo = fields.Char(string='Cargo', required=True)
    ingreso_mensual = fields.Integer(string='Ingreso Mensual', required=True)
    otros_ingresos = fields.Integer(string='Otros Ingresos', required=True)
    total_ingresos = fields.Integer(string='Total de Ingresos', required=True)
    referencias_avalista = fields.Integer(string='Referencias Personales del Avalista', required=True)
    codigo_solicitante = fields.Char(string='Código del Solicitante', required=True)