from openerp import models, fields, api

class CuentasCobrar(models.Model):
    _name = 'administracion.cuentas_cobrar'
    _rec_name = 'descripcion'

    codigo = fields.Char(string= "Codigo de cuenta")
    descripcion = fields.Char(string="Descripcion")
    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Numero de expediente', required=True)
    partidas_id = fields.Many2one('administracion.partidas', string ='Partida presupuestaria')
