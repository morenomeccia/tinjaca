from openerp import models, fields, api

class CuentasBancarias(models.Model):
    _name = 'administracion.cuentas_bancarias'
    _rec_name = 'nro_cuenta'

    nro_cuenta = fields.Char(string= "Numero de cuenta")
    banco = fields.Selection(string="Banco", selection=[('banco_venezuela','Venezuela'),
                                                        ('banco_deltesoro','Del Tesoro'),
                                                        ('banco_mercantil','Mercantil'),
                                                        ('banco_provincial','Provincial')])
    tipo_cuenta = fields.Selection(string="Tipo de cuenta", selection=[('cuenta_corriente','Corriente'),
                                                                       ('cuenta_ahoroo','Ahorro')])