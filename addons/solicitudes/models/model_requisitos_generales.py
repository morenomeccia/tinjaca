# -*- coding: utf-8 -*-

from openerp import models, fields, api


class RequisitosGenerales(models.Model):
    _name = 'solicitudes.requisitos_generales'

    #_rec_name = 'codigo_requisito'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")

    observaciones = fields.Char(string='Observaciones')
    documento = fields.Binary(string='Documento')
    valido = fields.Boolean(string='Valido')
    tipo_requisito = fields.Selection(string='Tipo de requisito', selection=[('1','Cedula'),
                                                                             ('2','Propuesta de financiamiento'),
                                                                             ('3','RIF'),
                                                                             ('4','Documento de propiedad'),
                                                                             ('5','Documento de alquiler'),
                                                                             ('6','Documento de arrendamiento'),
                                                                             ('','Factura de arrendamiento'),
                                                                             ('7','Documento de comodato'),
                                                                             ('8','Documento otro de unidad de produccion'),
                                                                             ('9','Croquis de ubicacion'),
                                                                             ('10','Exposicion de motivos'),
                                                                             ('11','Perfil economico'),
                                                                             ('12','Proyecto economico'),
                                                                             ('13','Registro de comercio'),
                                                                             ('14','Permiso sanidad'),
                                                                             ('15','Permiso alcaldia'),
                                                                             ('16','Permiso bomberos'),
                                                                             ('17','Permiso otro')])

