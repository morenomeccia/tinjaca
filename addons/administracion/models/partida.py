from openerp import models, fields, api

class Partida(models.Model):
    _name = 'administracion.partida'
    _rec_name = 'descripcion'

    codigo = fields.Char(string= "Codigo de cuenta")
    descripcion = fields.Char(string="Descripcion")
    cuenta_cobrar_id = fields.One2many('administracion.cuenta_cobrar', 'partida_id' ,string='Cuenta por cobrar')
