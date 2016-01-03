from openerp import models, fields, api

class Partidas(models.Model):
    _name = 'administracion.partidas'
    _rec_name = 'codigo'

    codigo = fields.Char(string= "Codigo de partida", required=True)
    descripcion = fields.Char(string="Descripcion")

    cuentas_cobrar_ids = fields.One2many('administracion.cuentas_cobrar', 'partidas_id' ,string='Cuenta por cobrar')
