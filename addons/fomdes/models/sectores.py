# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Sectores(models.Model):
    _name = 'fomdes.sectores'

    _rec_name = 'sector'
    
    sector = fields.Selection(string='Sector', selection=[('agricola', 'A - Agricola'),
                                                           ('turismo', 'T - Turismo'),
                                                           ('artesanal', 'AR - Artesanal'),
                                                           ('cyt', 'CyT - Ciencia y Tecnologia'),
                                                           ('pyme', 'PyME - Pequena y Mediana Empresa'),
                                                           ('pymi', 'PyMI - Pequena y Mediana Industria'),
                                                           ('microempresa', 'MEMP - Microempresa')])