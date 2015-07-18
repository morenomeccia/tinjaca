# -*- coding: utf-8 -*-

from openerp import models, fields, api

class credito(models.Model):
    _name = 'solicitudes.credito'

    nro_expediente = fields.Char(string='Numero de expedientes', required=True) # !!!
    codigo_solcitante = fields.Integer(string='Codigo del solicitante', required=True)
    codigo_unidad_productiva = fields.Integer(string='Codigo de la unidad productiva', required=True)
    codigo_taller = fields.Integer(string='Codigo del taller', required=True)
    codigo_consejo = fields.Integer(string='Codigo del consejo', required=True)
    codigo_estados_cuenta = fields.Integer(string='Codigo de los estados de cuenta', required=True)