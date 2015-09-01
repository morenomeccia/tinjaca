# -*- coding: utf-8 -*-

from openerp import models, fields, api

dependencias = [('presidencia', 'Presidencia'),
                ('credito','Gerencia de Crédito'),
                ('administracion', 'Gerencia de Administración'),
                ('recuperaciones','Gerencia de Recuperaciones'),
                ('rrhh', 'Recursos Humanos'),
                ('caja', 'Caja'),
                ('archivo', 'Archivo'),
                ('cjuridica', 'Consultoría Jurídica'),
                ('sejecutiva', 'Secretaría Ejecutiva')]

class visitantes(models.Model):
    _name = 'recepcion.visitantes'

    name = fields.Char(compute='_nombre_apellido')
    nombres = fields.Char(string='Nombres', size=40)
    apellidos = fields.Char(string='Apellidos', size=40)
    cedula = fields.Char(string='Cédula de Identidad')
    visita_id = fields.One2many('recepcion.visitantes', string='Visitas')

    @api.depends('nombres', 'apellidos')
    def _nombre_apellido(self):
        for record in self:
            record.name = "{} {}".format(record.nombres, record.apellidos)


class visitas(models.Model):
    _name = 'recepcion.visitantes'

    name = fields.Char()
    visitante_id = fields.Many2one('recepcion.visitantes', string='Visitante')
    fecha = fields.Datetime(string='Fecha')
    dependencia = fields.Selection(dependencias, string='Dependencia')