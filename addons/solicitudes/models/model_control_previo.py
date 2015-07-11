# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class controlPrevio(models.Model):
    _name = 'solicitudes.controlPrevio'

    codigo_analisis_juridico = fields.Char(string='Codigo de Analisis Juridico', required=True) # !!!
    nro_expediente = fields.Char(string='Numero de expediente', required=True) # !!!
    descripcion_garantia = fields.Char(string='Descripcion de la garantia', required=True)
    estatus_analisis_juridico = fields.Char(string='Estatus en analisis juridico', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)