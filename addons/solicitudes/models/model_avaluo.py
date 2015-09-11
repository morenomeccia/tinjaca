# -*- coding: utf-8 -*-

from openerp import models, fields, api

class avaluo(models.Model):
    _name = 'solicitudes.avaluo'

    _rec_name = 'fecha_avaluo'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Número de expediente")
    foto_avaluo_id = fields.One2many('solicitudes.fotografia_avaluo', 'avaluo_id', string="Fotografia de la avaluo")

    fecha_avaluo = fields.Date(string='Fecha de avaluo', required=True)
    descripcion_inmueble = fields.Char(string='Descripcion del inmueble')
    valor_del_inmueble = fields.Char(string='Valor del inmueble')
    ubicacion_del_inmueble = fields.Char(string='Ubicacion del inmueble')
    linderos_del_inmueble = fields.Char(string='Linderos del inmueble')
    caracteristicas_sector = fields.Char(string='Caracteristicas del sector')
    observaciones = fields.Char(string='Observaciones')



    



