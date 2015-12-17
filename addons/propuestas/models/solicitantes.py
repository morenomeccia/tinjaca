# -*- coding: utf-8 -*-

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api


class Solicitantes(models.Model):
    _name = 'propuestas.solicitantes'
    _inherit = 'res.partner'

    # user_id = fields.Many2one('res.users')
    # propuesta_id = fields.One2many('propuestas.propuestas', "solicitante_id", string="Propuesta")
    # codigo_solicitud = fields.Char(string='Código de la Solicitud')
    # firstname = fields.Char(string='Nombres', required=True) # de partner_firstname
    # lastname = fields.Char(string='Apellidos', required=True) # de partner_firstname
    cedula = fields.Char(string='Cédula de Identidad', required=True)
    rif = fields.Char(string='RIF')
    birthdate_date = fields.Date(string='Fecha de Nacimiento',
                                 default=fields.Date.today())  # de partner_contact_birthdate
    edad = fields.Integer(string='Edad', compute="_compute_edad", readonly=True)
    # gender = fields.Char(string='Sexo') # de partner_gender
    # street = fields.Char(string='Dirección de Habitación') # de res.partner>res.users
    # municipality_id = fields.Many2one('res.country.state.municipality', 'Municipality')
    # parish_id = fields.Many2one('res.country.state.municipality.parish', 'Parish')
    profesion_oficio = fields.Char(string='Profesión u Oficio')

    # phone = fields.Char(string='Teléfono Fijo') # de res.partner>res.users
    # mobile = fields.Char(string='Teléfono Celular') # de res.partner>res.users
    # email = fields.Char(string='Correo Electrónico') # de res.partner>res.users

    @api.model
    def create(self, values):
        res_id = super(Solicitantes, self).create(values)
        return res_id

    @api.onchange('birthdate_date')
    def _onchange_birthdate_date(self):
        """Almacenar la fecha en el campo birthdate original."""
        self.birthdate = self.birthdate_date
        dnac = datetime.strptime(self.birthdate_date, "%Y-%m-%d").date()
        dt = relativedelta(date.today(), dnac)
        self.edad = dt.years

    @api.depends('birthdate_date')
    def _compute_edad(self):
        """Calcular la edad actual a partir de la fecha de nacimiento"""
        dnac = datetime.strptime(self.birthdate_date, "%Y-%m-%d").date()
        dt = relativedelta(date.today(), dnac)
        self.edad = dt.years

        # @api.onchange('birthdate')
        # def set_age(self):
        #     for rec in self:
        #    if rec.dob:
        #    dt = rec.dob
        #    d1 = datetime.strptime(dt, "%Y-%m-%d").date()
        #         d2 = date.today()
        #    rd = relativedelta(d2, d1)
        #         rec.age = str(rd.years) + ' years'

        # @api.depends('nombres', 'apellidos')
        # def _nombre_apellido(self):
        #     for record in self:
        #         record.name = "{} {}".format(record.nombres, record.apellidos)
