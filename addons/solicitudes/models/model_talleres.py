# -*- coding: utf-8 -*-

from openerp import models, fields, api

 class talleres(models.Model):
     _name = 'solicitudes.talleres'

     fecha = fields.Date(string='Fecha', required=True)
	 funcionario = fields.Selection(_select_funcionario, string='Funcionario', required=True)
	 
def _select_funcionario(self, cr, uid, context=None):
    obj = self.pool.get('fomdes.funcionarios')
    ids = obj.search(cr, uid, [])
    resultado = obj.read(cr, uid, ids, ['name', 'id'], context)
    resultado = [(r['id'], r['name']) for r in resultado]
    return resultado
	