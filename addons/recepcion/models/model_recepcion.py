# -*- coding: utf-8 -*-

from openerp import models, fields, api

dependencias = [('presidencia', 'Presidencia'),
                ('credito', 'Gerencia de Crédito'),
                ('administracion', 'Gerencia de Administración'),
                ('recuperaciones', 'Gerencia de Recuperaciones'),
                ('rrhh', 'Recursos Humanos'),
                ('caja', 'Caja'),
                ('archivo', 'Archivo'),
                ('cjuridica', 'Consultoría Jurídica'),
                ('sejecutiva', 'Secretaría Ejecutiva')]

class Visitantes(models.Model):
    _name = 'recepcion.visitantes'

    _rec_name = 'cedula'
    nombres = fields.Char(string='Nombres', size=64)
    apellidos = fields.Char(string='Apellidos', size=64)
    cedula = fields.Char(string='Cédula de Identidad')
    visitas_id = fields.One2many(comodel_name='recepcion.visitas', inverse_name='visitante_id', string='Visitas')

    # @api.depends('nombres', 'apellidos')
    # def _nombre_apellido(self):
    #     for record in self:
    #         record.name = "{} {}".format(record.nombres, record.apellidos)

    _sql_constraints = [
        ('visitante_unico', 'unique(cedula)', 'El numero de cedula ya existe!')
    ]

class Visitas(models.Model):
    _name = 'recepcion.visitas'

    _rec_name = 'fecha'
    visitante_id = fields.Many2one(comodel_name='recepcion.visitantes', string='Visitante')
    fecha = fields.Datetime(string='Fecha')
    dependencia = fields.Selection(selection=dependencias, string='Dependencia')
