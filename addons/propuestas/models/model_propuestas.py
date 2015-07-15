# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Propuestas(models.Model):
     _name = 'propuestas.propuestas'

     name = fields.Char()
