# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Personas(models.Model):
    _name = 'contactos.personas'

    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', string='Contacto relacionado')

    cedula = fields.Char(string="Cedula", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    nombres = fields.Char(string="Nombres", required=True)

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
    telefono_fijo = fields.Char(related='partner_id.phone', string="Teléfono Fijo")
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

