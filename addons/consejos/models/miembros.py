# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Miembros(models.Model):
    _name = 'consejos.miembros'
    _rec_name = 'cedula'

    cedula = fields.Char(string='Cédula de Identidad', required=True)
    nombres = fields.Char(string='Nombres', required=True) # de partner_firstname
    apellidos = fields.Char(string='Apellidos', required=True) # de partner_firstname
    rif = fields.Char(string='RIF')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', default=fields.Date.today())  # de partner_contact_birthdate
    edad = fields.Integer(string='Edad', readonly=True) #calculado!!!
    genero = fields.Selection(string='Sexo', selection=[('genero_masculino', 'Masculino'),
                                                        ('genero_femenino', 'Femenino')]) # de partner_gender
    direccion = fields.Text(string='Dirección de Habitación') # de res.partner>res.users
    municipio = fields.Char(String='Municipio') #seleccion!!!
    parroquia = fields.Char(String='Parroquia') #seleccion!!!
    profesion_oficio = fields.Char(string='Profesión u Oficio')
    telefono_fijo = fields.Char(string='Teléfono Fijo') # de res.partner>res.users
    telefono_celular = fields.Char(string='Teléfono Celular') # de res.partner>res.users
    email = fields.Char(string='Correo Electrónico') # de res.partner>res.users

    organizacion = fields.Char(String='Organizacion')
    fecha_ingreso = fields.Date(string='Fecha de Ingreso')
    fecha_retiro = fields.Date(string='Fecha de Retiro')

    consejos_ids = fields.Many2many('consejos.consejos', string="Consejos directivos", relation='consejos_consejos_miembros_rel')

    _sql_constraints = [
        ('miembro_consejo_unico', 'unique(cedula)', 'Este numero de cedula ya existe!')
    ]

