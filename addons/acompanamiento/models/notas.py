# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Notas(models.Model):
    _name = 'acompanamiento.notas'

    _rec_name = 'fecha_nota'

    creditos_id = fields.Many2one('administracion.creditos', string="Número de expediente", required=True)
    
    fecha_nota = fields.Date(string='Fecha de la nota', required=True)
    tipo_nota = fields.Selection(string='Tipo de nota', selection=[('1', 'Atencion en oficina'), ('2', 'Llamada telefonica'), ('3', 'Visita a la unidad')]) 
    declaraciones = fields.Text(string='Declaraciones')
    
    




