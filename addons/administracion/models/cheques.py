from openerp import models, fields, api

class Cheques(models.Model):
    _name = 'administracion.cheques'
    _rec_name = 'nro_cheque'

    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Numero de expediente', required=True)
    cuentas_bancarias_id = fields.Many2one('administracion.cuentas_bancarias', string= "Cuenta Bancaria", required=True)

    nro_cheque = fields.Char(string="Nro de Cheque", required=True)
    nombre_cobrador = fields.Char(string="Nombre del cobrador", required=True)
    monto = fields.Float(string="Monto", required=True)
    motivo = fields.Char(string="Motivo")

