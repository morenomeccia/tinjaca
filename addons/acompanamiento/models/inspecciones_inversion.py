# -*- coding: utf-8 -*-

from openerp import models, fields, api

class InspeccionesInversion(models.Model):
    _name = 'acompanamiento.inspecciones_inversion'

    _rec_name = 'fecha_inspeccion'

    creditos_id = fields.Many2one('administracion.creditos', string="Número de expediente", required=True)
    foto_inspeccion_id = fields.One2many('acompanamiento.fotografias_acompanamiento', 'informes_acompanamiento_id', string="Fotografias de la inspeccion")

    fecha_inspeccion = fields.Date(string='Fecha de inspeccion', required=True)
    numero_liquidacion = fields.Integer(string='Numero de Liquidacion')
    recomendacion = fields.Boolean(string='Recomendado para proximas liquidaciones?')
    resultados = fields.Text(string='Resultados')
    observaciones = fields.Char(string='Observaciones')
    
    cantidad_empleos = fields.Integer(string='Cantidad de empleos generados')
    
    
    
    




