# -*- coding: utf-8 -*-

from openerp import models, fields, api


class UnidadesProductivas(models.Model):
    _name = 'propuestas.unidades_productivas'

    _rec_name = 'nombre'

    solicitantes_id = fields.Many2one('propuestas.solicitantes', string="Solicitante")

    nombre = fields.Char(string="Nombre de la Unidad Productiva")
    direccion = fields.Text(string='Dirección') # de res.partner>res.company
    telefono_fijo = fields.Integer(string='Teléfono fijo')
    telefono_celular = fields.Integer(string='Teléfono Celular')
    actividad = fields.Char(string='Actividad que realiza')
    experiencia = fields.Text(string='Experiencia en el area')
    # Area de funcionamiento:
    area_geografica = fields.Text(string='Area geografica a cubrir')
    espacio_funcionamiento = fields.Selection(string='Espacio', selection=[('1', 'Local'), ('2', 'Galpon'), ('3', 'Finca'), ('4', 'Terreno'), ('5', 'Casa de habitacion'),('6', 'Posada'), ('7', 'Hotel'), ('8', 'Otro')])
    situacion_propiedad = fields.Selection(string='Situacion', selection=[('1', 'Propio'), ('2', 'Alquilado'), ('3', 'Comodato'), ('4', 'Familiar'), ('5', 'Otro')])
    area_m2 = fields.Float(string='Area en metros cuadrados')
    zona_geografica = fields.Char(string='Zona Geografica', selection=[('1', 'Rural'), ('2', 'Urbana')])
    servicio_electricidad = fields.Boolean(string='Electricidad')
    servicio_agua = fields.Boolean(string='Agua')
    servicio_telefono = fields.Boolean(string='Telefono')
    servicio_internet = fields.Boolean(string='Internet')
    servicio_cabletv = fields.Boolean(string='TV por cable')
    servicio_transporte = fields.Boolean(string='Transporte')
    servicio_aseo = fields.Boolean(string='Aseo domiciliario')
    servicio_vialidad = fields.Boolean(string='Vialidad')
