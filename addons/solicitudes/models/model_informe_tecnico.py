# -*- coding: utf-8 -*-

from openerp import models, fields, api


class InformeTecnico(models.Model):
    _name = 'solicitudes.informe_tecnico'

    nro_expediente = fields.Char(string='Numero de expediente', required=True)  # !!!
    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', required=True)
    tipo_empresa = fields.Char(string='Tipo de empresa', required=True)  # !!!
    Saldo_Balance_Personal = fields.Float(string='Balance personal', required=True)
    Organizacion_Juridica = fields.Char(string='Organizacion juridica', required=True)
    Recomendaciones = fields.Char(string='Recomendaciones', required=True)
    firma = fields.Binary(string='Firma', required=True)
    informe_fotografico_inspeccion = fields.Binary(string='Fotografia de la inspeccion', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)
