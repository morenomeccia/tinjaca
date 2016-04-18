from openerp import models, fields, api

class CuentasBancariasAvalista(models.Model):
    _name = 'propuestas.cuentas_bancarias_avalista'
    _rec_name = 'nro_cuenta'

    avalistas_id = fields.Many2one('propuestas.avalistas', string="Avalista")

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

    _sql_constraints = [
        ('numero_cuenta_unico', 'unique(nro_cuenta)', 'El numero de cuenta ya existe!')
    ]
