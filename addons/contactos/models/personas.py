# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class Personas(models.Model):
    _name = 'contactos.personas'

    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', string='Contacto relacionado')

    cedula = fields.Char(string="Cedula", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    nombres = fields.Char(string="Nombres", required=True)
    rif = fields.Char(string="RIF")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", default=fields.Date.today())
    edad = fields.Integer(string="Edad", compute='_compute_edad')
    genero = fields.Selection(string='Genero', selection=[('genero_masculino', "Masculino"),
                                                          ('genero_femenino', "Femenino")])
    estado_civil = fields.Selection(string='Estado Civil', selection=[('estado_soltero', "Soltero"),
                                                                      ('estado_casado', "Casado"),
                                                                      ('estado_divorciado', "Divorciado"),
                                                                      ('estado_viudo', "Viudo")])
    hijos = fields.Integer(string="Hijos", default=0)
    profesion = fields.Char(string="Profesion u Oficio")
    telefono_oficina = fields.Char(string="Teléfono de Oficina")
    telefono_celular2 = fields.Char(string="Teléfono Celular 2")
    correo_electronico2 = fields.Char(string="Correo Electrónico 2")
    cuenta_twitter = fields.Char(string="Cuenta Twitter")
    nivel_estudios = fields.Selection(string='Nivel de Estudios', selection=[('estudio_ninguno', "Ninguno"),
                                                                             ('estudio_primaria', "Primaria"),
                                                                             ('estudio_secundaria', "Secundaria"),
                                                                             ('estudio_universitario', "Universitario")])
    trabaja = fields.Boolean(string="Trabaja?")
    ingresos_mensuales = fields.Float(string="Ingresos Mensuales")
    limite_tdc = fields.Float(string="Limite TDC")

    # Campos relacionados a res.partner:
    name = fields.Char(related='partner_id.name', string="Nombre", inherited=True)
    foto = fields.Binary(related='partner_id.image', string="Foto")
    pais_id = fields.Many2one(related='partner_id.country_id', string="País", default=240)  #Venezuela
    estado_id = fields.Many2one(related='partner_id.state_id', string="Estado")
    municipio_id = fields.Many2one(related='partner_id.municipality_id', string='Municipio')
    parroquia_id = fields.Many2one(related='partner_id.parish_id', string='Parroquia')
    ciudad = fields.Char(related='partner_id.city', string="Ciudad")
    direccion = fields.Char(related='partner_id.street', string="Dirección")
    direccion2 = fields.Char(related='partner_id.street2', string="Dirección 2")
    codigo_postal = fields.Char(related='partner_id.zip', string="Codigo Postal")
    telefono_habitacion = fields.Char(related='partner_id.phone', string="Teléfono de Habitacion")
    telefono_celular = fields.Char(related='partner_id.mobile', string="Teléfono Celular")
    telefono_fax = fields.Char(related='partner_id.fax', string="Fax")
    correo_electronico = fields.Char(related='partner_id.email', string="Correo Electrónico")

    @api.depends('cedula', 'apellidos', 'nombres')
    def _get_name(self):
        """Obtiene campo name a partir de los nombres y apellidos"""
        self.name = str(self.cedula) + " - " + str(self.nombres) + " " + str(self.apellidos)

    @api.onchange('cedula', 'apellidos', 'nombres')
    def _update_name(self):
        self._get_name()

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        """Obtiene campo edad a partir de la fecha de nacimiento"""
        f_nac = datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d").date()
        dif_t = relativedelta(date.today(), f_nac)
        self.edad = dif_t.years

    _sql_constraints = [
        ('persona_unica', 'unique(cedula)', 'Este numero de cedula ya existe!')
    ]



