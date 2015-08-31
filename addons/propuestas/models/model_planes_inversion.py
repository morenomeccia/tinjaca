#-*- coding: utf-8 -*-

from openerp import models, fields, api


class Planes_Inversion(models.Model):
    _name = 'propuestas.planes_inversion'

    codigo_pi = fields.Char(string='Código del Plan de Inversión', required=True)
    capital_trabajo = fields.Integer(string='Capital de Trabajo', required=True)
    materia_prima = fields.Integer(string='Materia Prima', required=True)
    mano_obra = fields.Integer(string='Mano de Obra', required=True)
    gastos_constitucion = fields.Integer(string='Gastos de Constitución', required=True)
    inversiones_fijas = fields.Integer(string='Inversiones Fijas', required=True)
    ampliacion_remodelacion = fields.Integer(string='Ampliación o Remodelación', required=True)
    maquinaria = fields.Integer(string='Maquinaria', required=True)
    equipo = fields.Integer(string='Equipos', required=True)
    herramientas_menores = fields.Integer(string='Utensilios y Herramientas Menores', required=True)
    otros = fields.Integer(string='Otros', required=True)
    inversion_total = fields.Integer(string='Inversión Total', required=True)
    codigo_ap = fields.Char(string='Código de la Unidad Productiva', required=True)
    codigo_credito = fields.Char(string='Código del Crédito', required=True)
    consigno_facturas = fields.Char(string='Consignación de Facturas', required=True)
    observaciones = fields.Char(string='Observaciones', required=True)