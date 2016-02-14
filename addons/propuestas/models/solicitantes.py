# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Solicitantes(models.Model):
    _name = 'propuestas.solicitantes'
    _description = 'Información de los solicitantes'
    _inherits = {'res.users': 'user_id'}

    _rec_name = 'cedula'

    user_id = fields.Many2one('res.users', string='Usuario', ondelete="cascade", select=True, required=True)
    cedula = fields.Char(string='Cédula de Identidad', required=True)
    nombres = fields.Char(string='Nombres', required=True) # de partner_firstname
    apellidos = fields.Char(string='Apellidos', required=True) # de partner_firstname
    rif = fields.Char(string='RIF')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', default=fields.Date.today())  # de partner_contact_birthdate
    edad = fields.Integer(string='Edad', readonly=True) #calculado!!!
    genero = fields.Selection(string='Sexo', selection=[('genero_masculino', 'Masculino'),
                                                        ('genero_femenino', 'Femenino')]) # de partner_gender
    direccion = fields.Text(string='Dirección de Habitación') # de res.partner>res.users
    pais_id = fields.Many2one(related='user_id.country_id', String='País', default=240)
    estado_id = fields.Many2one(related='user_id.state_id', String='Estado') #seleccion!!!
    municipio_id = fields.Many2one(related='user_id.municipality_id', String='Municipio') #seleccion!!!
    parroquia_id = fields.Many2one(related='user_id.parish_id', String='Parroquia') #seleccion!!!
    profesion_oficio = fields.Char(string='Profesión u Oficio')
    telefono_fijo = fields.Char(string='Teléfono Fijo') # de res.partner>res.users
    telefono_celular = fields.Char(string='Teléfono Celular') # de res.partner>res.users
    email = fields.Char(string='Correo Electrónico') # de res.partner>res.users

    unidades_productivas_ids = fields.One2many('propuestas.unidades_productivas', 'solicitantes_id', string="Unidad Productiva")
    propuestas_ids = fields.One2many('propuestas.propuestas', 'solicitantes_id', string="Propuesta")
    #    referencias_familiares_ids = fields.One2many('propuestas.referencias_familiares', 'solicitantes_id',string="Referencias Familiares")

    @api.onchange('state_id')
    def _onchange_state_id(self):
        """        """
        print self.state_id
        print self.state_id.country_id
        self.country_id = self.state_id.country_id

    # def write(self):
    #     return super(Solicitantes, self).write()

class res_partner(models.Model):
    '''Defining a address information '''
    _inherit = 'res.partner'
    _description = 'Address Information'

    solicitante_id = fields.Many2one('propuestas.solicitantes','Solicitante')