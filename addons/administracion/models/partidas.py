from openerp import models, fields, api

class Partidas(models.Model):
    _name = 'administracion.partidas'
    _rec_name = 'descripcion'

    codigo = fields.Char(string= "Codigo de cuenta")
    descripcion = fields.Char(string="Descripcion")
    cuentas_cobrar_id = fields.One2many('administracion.cuentas_cobrar', 'partidas_id' ,string='Cuenta por cobrar')
