# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Personas(models.Model):
    _name = 'contactos.personas'

    _inherits = {'res.partner': 'partner_id'}

    # overridden inherited fields to bypass access rights, in case you have
    # access to the user but not its corresponding partner
    #name = fields.Char(related='partner_id.name', inherited=True)
    #email = fields.Char(related='partner_id.email', inherited=True)