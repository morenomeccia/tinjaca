from openerp import models, fields, api

class CuentaCobrar(models.Model):
    _name = 'administracion.cuenta_cobrar'
    _rec_name = 'descripcion'

    codigo = fields.Char(string= "Codigo de cuenta")
    descripcion = fields.Char(string="Descripcion")
    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string='Numero de expediente', required=True)
    partida_id = fields.Many2one('administracion.partida', string = 'Partida presupuestaria')
