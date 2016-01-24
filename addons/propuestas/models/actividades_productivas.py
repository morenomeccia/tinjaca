# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ActividadesProductivas(models.Model):
    _name = 'propuestasfomdes.actividades_productivas'

    _rec_name = 'descripcion'

    unidades_productivas_id = fields.Many2one('propuestasfomdes.unidades_productivas', string="Unidad Productiva", required=True)

    descripcion = fields.Char(string="Descripcion")
    producto_derivado = fields.Text(string='Productos Derivados de la Actividad')
    materia_prima = fields.Text(string='Materia Prima a Utilizar')
    obtiene_mp = fields.Text(string='¿Dónde y Cómo Obtiene la Materia Prima')
    precio_venta = fields.Float(string='Precio Estimado de Venta de los Productos')
    distribucion = fields.Text(string='Distribuión y Sistemas de Ventas')
    trabajadores = fields.Integer(string='Número de Trabajdores Existentes')
    puestos_generar = fields.Integer(string='Puestos de Trabajos que se van a Generar')
    explicacion_ap = fields.Char(string='Breve Explicación de la Propuesta Emprendedora')
    consigno_facturas = fields.Char(string='Consignación de Facturas')
    observaciones = fields.Char(string='Observaciones')
