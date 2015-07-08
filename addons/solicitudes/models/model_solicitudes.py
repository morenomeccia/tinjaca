# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Solicitudes(models.Model):
     _name = 'solicitudes.solicitudes'

     name = fields.Char()
