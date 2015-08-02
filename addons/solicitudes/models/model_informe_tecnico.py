# -*- coding: utf-8 -*-

from openerp import models, fields, api


class InformeTecnico(models.Model):
    _name = 'solicitudes.informe_tecnico'

    _rec_name = 'codigo_informe'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")

    codigo_informe = fields.Char(string='Codigo Informe')
    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', required=True)
    tipo_empresa = fields.Char(string='Tipo de empresa')  # !!!
    Saldo_Balance_Personal = fields.Float(string='Balance personal')
    Organizacion_Juridica = fields.Char(string='Organizacion juridica')
    Recomendaciones = fields.Char(string='Recomendaciones')
    informe_fotografico_inspeccion = fields.Binary(string='Fotografia de la inspeccion', required=True)

    


