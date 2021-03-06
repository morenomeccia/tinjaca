from openerp import models, fields, api

class CuentasBancarias(models.Model):
    _name = 'administracion.cuentas_bancarias'
    _rec_name = 'nro_cuenta'

    nro_cuenta = fields.Char(string= "Numero de cuenta")
    banco = fields.Selection(string="Banco", selection=[('banco_bancaribe','Bancaribe'),
                                                        ('banco_banesco','Banesco'),
                                                        ('banco_bicentenario','Bicentenario'),
                                                        ('banco_deltesoro','Del Tesoro'),
                                                        ('banco_exterior','Exterior'),
                                                        ('banco_fondocomun','Fondo Comun'),
                                                        ('banco_mercantil','Mercantil'),
                                                        ('banco_bod','Occidental de Descuento (BOD)'),
                                                        ('banco_provincial','Provincial'),
                                                        ('banco_venezuela','Venezuela')])
    tipo_cuenta = fields.Selection(string="Tipo de cuenta", selection=[('cuenta_corriente','Corriente'),
                                                                       ('cuenta_ahorro','Ahorro')])