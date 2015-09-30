# -*- coding: utf-8 -*-

from openerp import models, fields, api


class RequisitosGenerales(models.Model):
    _name = 'solicitudes.requisitos_generales'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    tipo_documento = fields.Selection(string='Tipo de Documento', selection=[('1','Cedula'),
                                                                             ('2','Propuesta de financiamiento'),
                                                                             ('3','RIF'),
                                                                             ('4','Carta de residencia'),
                                                                             ('5','Documento de propiedad'),
                                                                             ('6','Documento de alquiler'),
                                                                             ('7','Documento de arrendamiento'),
                                                                             ('8','Factura de arrendamiento'),
                                                                             ('9','Documento de comodato'),
                                                                             ('10','Documento otro de unidad de produccion'),
                                                                             ('11','Croquis de ubicacion'),
                                                                             ('12','Exposicion de motivos'),
                                                                             ('13','Perfil economico'),
                                                                             ('14','Proyecto economico'),
                                                                             ('15','Registro de comercio'),
                                                                             ('16','Permiso sanidad'),
                                                                             ('17','Permiso alcaldia'),
                                                                             ('18','Permiso bomberos'),
                                                                             ('19','Permiso otro')])
    documento = fields.Binary(string='Documento')
    observaciones = fields.Char(string='Observaciones')
    valido = fields.Boolean(string='Valido')


