# -*- coding: utf-8 -*-

from openerp import models, fields, api


class InformeTecnico(models.Model):
    _name = 'solicitudes.informe_tecnico'

#    def _select_solicitud(self, cr, uid, context=None):
#        obj = self.pool.get('solicitudes.solicitudes')
#        ids = obj.search(cr, uid, [])
#        resultado = obj.read(cr, uid, ids, ['nro_expediente', 'id'], context)
#        resultado = [(r['id'], r['nro_expediente']) for r in resultado]
#        return resultado

#    nro_expediente = fields.Selection(_select_solicitud, string='Solicitud', required=True)

#    nro_expediente = fields.related('solicitudes_id', 'nro_expediente', type="char", string='Name', store=True)
    solicitudes_id = fields.Many2one('solicitudes.solicitudes', string="Numero de expediente")
 
    fecha_elaboracion = fields.Date(string='Fecha de elaboracion', required=True)
    tipo_empresa = fields.Char(string='Tipo de empresa')  # !!!
    Saldo_Balance_Personal = fields.Float(string='Balance personal')
    Organizacion_Juridica = fields.Char(string='Organizacion juridica')
    Recomendaciones = fields.Char(string='Recomendaciones')
    firma = fields.Binary(string='Firma', required=True)
    informe_fotografico_inspeccion = fields.Binary(string='Fotografia de la inspeccion', required=True)
    


