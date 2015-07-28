# -*- coding: utf-8 -*-

from openerp import models, fields, api


class InformeTecnico(models.Model):
    _name = 'solicitudes.informe_tecnico'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
 
    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', required=True)
    tipo_empresa = fields.Char(string='Tipo de empresa')  # !!!
    Saldo_Balance_Personal = fields.Float(string='Balance personal')
    Organizacion_Juridica = fields.Char(string='Organizacion juridica')
    Recomendaciones = fields.Char(string='Recomendaciones')
    firma = fields.Binary(string='Firma', required=True)
    informe_fotografico_inspeccion = fields.Binary(string='Fotografia de la inspeccion', required=True)

    


