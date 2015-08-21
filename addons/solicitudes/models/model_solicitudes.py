# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Solicitudes(models.Model):
    _name = 'solicitudes.solicitudes'

    _rec_name = 'nro_expediente'

    nro_expediente = fields.Char(string='Numero de expediente', required=True)
    state = fields.Selection(string='Estacion', selection=[('1', 'Informacion de credito'),
                                                           ('2', 'Analisis juridico'),
                                                           ('3', 'Analisis economico'),
                                                           ('4', 'Gerencia de credito')], default='1')


    requisitos_generales_id = fields.One2many('solicitudes.requisitos_generales', 'solicitudes_id', string="Requisitos generales")
    informe_tecnico_id = fields.One2many('solicitudes.informe_tecnico', 'solicitudes_id', string="Informe tecnico")

    @api.one
    def action_informacion_credito(self):
        self.state = '1'

    @api.one
    def action_analisis_juridico(self):
        self.state = '2'

    @api.one
    def action_analisis_economico(self):
        self.state = '3'

    @api.one
    def action_gerencia_credito(self):
        self.state = '4'

    # display_name = fields.Char(
    #     string='Número de expediente', compute='_compute_display_name',
    # )
    #
    # @api.one
    # @api.depends('nro_expediente')
    # def _compute_display_name(self):
    #     self.display_name = self.nro_expediente
