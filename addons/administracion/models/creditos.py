from openerp import models, fields, api

class Creditos(models.Model):
    _name = 'administracion.creditos'
    _rec_name = 'descripcion'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Número de expediente', required=True)
    #caja_id = fields.Many2one('caja.cajas', string='Numero de expediente', required=True) # !!! Obtenido del usuario?
    solicitante_propuesta = fields.Many2one(string='Solicitante',
                                            related='solicitudes_id.solicitante_propuesta',
                                            readonly=True)
    # Campos para los montos y tasas sugeridas:
    monto_total = fields.Float(string='Monto total',
                                            related='solicitudes_id.monto_total',
                                            readonly=True)
    plazo_pago = fields.Integer(string='Periodo de pago',
                                            related='solicitudes_id.plazo_pago',
                                            readonly=True)
    periodos_gracia = fields.Integer(string='Periodo de gracia',
                                            related='solicitudes_id.periodos_gracia',
                                            readonly=True)
    tasa_interes = fields.Float(string='Tasa de interes',
                                            related='solicitudes_id.tasa_interes',
                                            readonly=True)
    tasa_mora = fields.Float(string='Tasa de mora',
                                            related='solicitudes_id.tasa_mora',
                                            readonly=True)
    #monto_cuota = fields.Float(string='Monto de la cuota') #calculado
    comision_flat = fields.Float(string='Comision FLAT',
                                            related='solicitudes_id.comision_flat',
                                            readonly=True)
    aporte_social = fields.Float(string='Aporte social',
                                            related='solicitudes_id.aporte_social',
                                            readonly=True)

    # Campos de liquidacion de credito
    fecha_liquidacion = fields.Date(string='Fecha de liquidacion',
                                            related='solicitudes_id.fecha_liquidacion',
                                            readonly=True)
    fecha_ultima = fields.Date(string='Fecha ultima de pago',
                                            related='solicitudes_id.fecha_ultima',
                                            readonly=True)