# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Solicitudes(models.Model):
    _name = 'solicitudes.solicitudes'

    name = fields.Char()
    nro_expediente = fields.Char(string='Numero de expediente', required=True) 


class Inspecciones(models.Model):
    _name = 'solicitudes.inspecciones'

    nro_expediente = fields.Char(string='Numero de expediente', required=True) # !!!
    tiempo_funcionamiento = fields.Float(string='Tiempo de funcionamiento', required=True)
    cantidad_productos = fields.Integer(string='Cantidad de productos')
    costos_actividad = fields.Float(string='Costo de la actividad')
    sistema_produccion = fields.Char(string='Sistema de produccion')
    clientes = fields.Char(string='Clientes', required=True)
    distribucion_espacio_fisico = fields.Char(string='Distribucion del espacio fisico')
    condicion_fisica_sanitaria = fields.Selection(string='Condicion sanitaria', selection=[('1', 'Bueno'), ('2', 'Regular'), ('3', 'Malo')]) # !!!
    maquinaria = fields.Char(string='Maquinaria') 
    materia_prima = fields.Char(string='Materia prima') 
    observaciones = fields.Char(string='Observaciones')
    firma = fields.Binary(string='Firma del beneficiario', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)

class InformeTecnico(models.Model):
    _name = 'solicitudes.informe_tecnico'

    nro_expediente = fields.Char(string='Numero de expediente', required=True)  # !!!
 
    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', required=True)
    tipo_empresa = fields.Char(string='Tipo de empresa')  # !!!
    Saldo_Balance_Personal = fields.Float(string='Balance personal')
    Organizacion_Juridica = fields.Char(string='Organizacion juridica')
    Recomendaciones = fields.Char(string='Recomendaciones')
    firma = fields.Binary(string='Firma', required=True)
    informe_fotografico_inspeccion = fields.Binary(string='Fotografia de la inspeccion', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)
    
    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Numero de expediente")

class controlPrevio(models.Model):
    _name = 'solicitudes.control_previo'

    codigo_analisis_juridico = fields.Char(string='Codigo de Analisis Juridico', required=True) # !!!
    nro_expediente = fields.Char(string='Numero de expediente', required=True) # !!!
    descripcion_garantia = fields.Char(string='Descripcion de la garantia', required=True)
    estatus_analisis_juridico = fields.Char(string='Estatus en analisis juridico', required=True)
    codigo_credito = fields.Integer(string='Codigo del credito', required=True)
