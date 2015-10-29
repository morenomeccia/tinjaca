# -*- coding: utf-8 -*-

from openerp import models, fields, api

class consejoDirectivo(models.Model):
    _name = 'aprobacion.requisitos_sector'

	codigo = fields.Integer(string='Codigo del consejo')
	numero = fields.Integer(string='Numero del consejo')
	fecha = fields.datetime(string='Fecha y hora del consejo')

	estatus_decision = 		
	nro_expediente = one2many
	miembros = 
	plan_de_inversion = 

    #aprobacion_id = fields.Many2one('aprobacion.solicitudes', string="Número de expediente")
    #documentos_sector_id = fields.Many2one('politicas.documentos_sector', string="Tipo de Documento")

