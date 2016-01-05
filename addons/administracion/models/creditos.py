# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Creditos(models.Model):
    _name = 'administracion.creditos'
    _rec_name = 'nro_expediente'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Número de expediente')
    nro_expediente = fields.Char(string='Numero de expediente',
                                            related='solicitudes_id.nro_expediente')
    cedula_solicitante = fields.Char(string='Cédula Solicitante',
                                     related='solicitudes_id.propuestas_id.cedula_solicitante')
    # caja_id = fields.Many2one('caja.cajas', string='Numero de expediente', required=True) # !!! Obtenido del usuario?
    solicitantes_id_propuesta = fields.Many2one(string='Solicitante',
                                            related='solicitudes_id.solicitantes_id_propuesta',
                                            readonly=True)
    # Campos para los montos y tasas sugeridas:
    monto_total = fields.Float(string='Monto total',
                                            related='solicitudes_id.monto_total')
    plazo_pago = fields.Integer(string='Periodo de pago',
                                            related='solicitudes_id.plazo_pago')
    periodos_gracia = fields.Integer(string='Periodo de gracia',
                                            related='solicitudes_id.periodos_gracia')
    tasa_interes = fields.Float(string='Tasa de interes',
                                            related='solicitudes_id.tasa_interes')
    tasa_mora = fields.Float(string='Tasa de mora',
                                            related='solicitudes_id.tasa_mora')
    # monto_cuota = fields.Float(string='Monto de la cuota') #calculado
    comision_flat = fields.Float(string='Comision FLAT',
                                            related='solicitudes_id.comision_flat')
    aporte_social = fields.Float(string='Aporte social',
                                            related='solicitudes_id.aporte_social')

    # Campos de liquidacion de credito
    fecha_liquidacion = fields.Date(string='Fecha de liquidacion',
                                            related='solicitudes_id.fecha_liquidacion')
