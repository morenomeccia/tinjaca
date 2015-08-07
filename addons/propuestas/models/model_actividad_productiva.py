#-*- coding: utf-8 -*-

from openerp import models, fields, api

class ActividadProductiva(models.Model):
    _name = 'propuestas.actividad_productiva'

    codigo_ap = fields.Char(string='Código de la Actividad Productiva', required=True)
    producto_derivado = fields.Char(string='Productos Derivados de la Actividad', required=True)
    materia_prima = fields.Char(string='Materia Prima a Utilizar', required=True)
    obtiene_mp = fields.Char(string='¿Dónde y Cómo Obtiene la Materia Prima', required=True)
    precio_venta = fields.Char(string='Precio Estimado de Venta de los Productos', required=True)
    distribucion = fields.Char(string='Distribuión y Sistemas de Ventas', required=True)
    trabajadores = fields.Integer(string='Número de Trabajdores Existentes', required=True)
    puestos_generar = fields.Integer(string='Puestos de Trabajos que se van a Generar', required=True)
    explicacion_ap = fields.Char(string='Breve Explicación de la Propuesta Emprendedora', required=True)
    codigo_up = fields.Char(string='Código de la Unidad Productiva', required=True)
    codigo_credito = fields.Char(string='Código del Crédito', required=True)
    consigno_facturas = fields.Char(string='Consignación de Facturas', required=True)
    observaciones = fields.Char(string='Observaciones', required=True)
