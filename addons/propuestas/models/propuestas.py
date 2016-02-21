# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Propuestas(models.Model):
    _name = 'propuestas.propuestas'

    _rec_name = 'codigo_planilla'

    solicitantes_id = fields.Many2one('propuestas.solicitantes', string="Solicitante", required=True)
    unidades_productivas_id = fields.Many2one('propuestas.unidades_productivas', string="Unidad Productiva")

    codigo_planilla = fields.Char(string="Codigo Planilla", required=True)
    fecha_recibida = fields.Date(string='Fecha de recepcion', default=fields.Date.today(), required=True)

    producto_derivado = fields.Text(string='Productos derivados de la actividad')
    materia_prima = fields.Text(string='Materia prima a utilizar')
    obtencion_materia = fields.Text(string='¿Dónde y cómo obtiene la materia prima?')
    precio_venta = fields.Float(string='Precio estimado de venta de los productos')
    distribucion = fields.Text(string='Distribuión y sistemas de ventas')
    trabajadores = fields.Integer(string='Número de trabajadores existentes')
    puestos_trabajo = fields.Integer(string='Puestos de trabajos que se van a generar')
    explicacion = fields.Text(string='Breve explicación de la propuesta emprendedora')

    tipos_garantia_id = fields.Many2one('politicas.tipos_garantia', string="Tipo de Garantia")
    codigo_garantia = fields.Char(related='tipos_garantia_id.codigo')

    referencias_solicitante_ids = fields.One2many('propuestas.referencias_solicitante', 'propuestas_id', string="Referencias del Solicitante")
    garantias_ids = fields.One2many('propuestas.garantias', 'propuestas_id', string="Garantías")
    avalistas_ids = fields.One2many('propuestas.avalistas', 'propuestas_id', string="Avalista")
    #referencias_avalista_ids = fields.One2many('propuestas.referencias_avalista', 'propuestas_id', string='Referencias del Avalista')
    inversiones_ids = fields.One2many('propuestas.inversiones', 'propuestas_id', string='Plan de Inversiones')

    inversion_total_propia = fields.Float(string='Inversión total propia') #TODO calculado!!!
    inversion_total_fomdes = fields.Float(string='Inversión total fomdes') #TODO calculado!!!
    observaciones = fields.Text(string='Observaciones')

    talleres_ids = fields.Many2many('propuestas.talleres', string="Taller", relation='talleres_propuestas')

    state = fields.Selection(string='Estacion', selection=[('estacion_1_propuesta_recibida', 'Propuesta recibida'),
                                                           ('estacion_2_taller', 'Taller'),
                                                           ('estacion_3_creacion_expediente', 'Creacion de expediente')],
                                                           default='estacion_1_propuesta_recibida')


    # Cambia a la estacion "Propuesta recibida"
    @api.one
    def action_estacion_propuesta_recibida(self):
        self.state = 'estacion_1_propuesta_recibida'

    # Cambia a la estacion "Taller"
    @api.one
    def action_estacion_taller(self):
        self.state = 'estacion_2_taller'

    # Cambia a la estacion "Creacion de expediente"
    @api.one
    def action_estacion_creacion_expediente(self):
        self.state = 'estacion_3_creacion_expediente'


