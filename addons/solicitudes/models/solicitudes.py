# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Solicitudes(models.Model):
    _name = 'solicitudes.solicitudes'

    _rec_name = 'nro_expediente'

    nro_expediente = fields.Char(string='Numero de expediente', required=True)

    state = fields.Selection(string='Estacion', selection=[('estacion_1_consignacion_requisitos', 'Consignacion de Requisitos'),
                                                           ('estacion_2_control_previo', 'Control Previo'),
                                                           ('estacion_3_inspeccion_avaluo', 'Inspeccion / Avaluo'),
                                                           ('estacion_4_evaluacion_gerente', 'Evaluacion por Gerente'),
                                                           ('estacion_5_evaluacion_presidencia', 'Evaluacion por Presidencia'),
                                                           ('estacion_7_discusion_consejo', 'Discusion por Consejo'),
                                                           ('estacion_8_creacion_documentos', 'Creacion Documentos'),
                                                           ('estacion_9_liquidacion', 'Liquidacion')],
                                                           default='estacion_1_consignacion_requisitos')

    estatus_gerencia_credito = fields.Selection(string='Estatus Gerencia', selection=[('estatus_evaluar', 'Por evaluar'),
                                                                                      ('estatus_rechazado', 'Rechazado'),
                                                                                      ('estatus_aceptado', 'Aceptado'),
                                                                                      ('estatus_aceptado_cond', 'Aceptado Condicionado')],
                                                                                      default='estatus_evaluar')

    estatus_presidencia = fields.Selection(string='Estatus Presidencia', selection=[('estatus_decidir', 'Por decidir'),
                                                                                      ('estatus_recomendado', 'Recomendado'),
                                                                                      ('estatus_no_recomendado', 'No recomendado'),
                                                                                      ('estatus_recomendado_cond', 'Recomendado Condicionado')],
                                                                                      default='estatus_decidir')

    estatus_consejo_directivo = fields.Selection(string='Estatus Consejo', selection=[('estatus_discutir', 'Por discutir'),
                                                                                      ('estatus_negado', 'Negado'),
                                                                                      ('estatus_aprobado', 'Aprobado'),
                                                                                      ('estatus_aprobado_cond', 'Aprobado Condicionado'),
                                                                                      ('estatus_diferido', 'Diferido')],
                                                                                      default='estatus_discutir')

    propuestas_id = fields.Many2one('propuestasfomdes.propuestas', string="Propuesta")

    # Campos provinientes de propuestas:
    solicitantes_id_propuesta = fields.Many2one(string='Solicitante', related='propuestas_id.solicitantes_id', readonly=True)
    sector_id = fields.Many2one('politicas.sectores', string="Sector")
    garantia_id = fields.Many2one('politicas.garantias', string="Garantia")
    empresa_establecida = fields.Boolean(string='Empresa establecida?', default = False)

    # Campos para los montos y tasas sugeridas:
    monto_total = fields.Float(string='Monto total') 
    plazo_pago = fields.Integer(string='Periodo de pago')
    periodos_gracia = fields.Integer(string='Periodo de gracia')
    tasa_interes = fields.Float(string='Tasa de interes')
    tasa_mora = fields.Float(string='Tasa de mora')
    #monto_cuota = fields.Float(string='Monto de la cuota') #calculado
    comision_flat = fields.Float(string='Comision FLAT')
    aporte_social = fields.Float(string='Aporte social')

    # Campos para generar del documento de credito y de la empresa
    fecha_de_entrega = fields.Date("Fecha de Entrega")
    lapso_de_devolucion = fields.Integer(string='Lapso de devolucion del documento')

    # Campos de liquidacion de credito
    fecha_liquidacion = fields.Date(string='Fecha de liquidacion')
    fecha_ultima = fields.Date(string='Fecha ultima de pago') #calculado

    # Referencias a otros modelos:
    requisitos_generales_id = fields.One2many('solicitudes.requisitos_generales', 'solicitudes_id', string="Requisitos generales")
    requisitos_sector_id = fields.One2many('solicitudes.requisitos_sector', 'solicitudes_id', string="Requisitos sector")
    requisitos_garantia_id = fields.One2many('solicitudes.requisitos_garantia', 'solicitudes_id', string="Requisitos garantia")
    requisitos_empresa_id = fields.One2many('solicitudes.requisitos_empresa', 'solicitudes_id', string="Requisitos empresa")
    control_previo_id = fields.One2many('solicitudes.control_previo', 'solicitudes_id', string="Control Previo")
    avaluo_id = fields.One2many('solicitudes.avaluo', 'solicitudes_id', string="Avaluo")
    inspeccion_id = fields.One2many('solicitudes.inspecciones', 'solicitudes_id', string="Inspeccion")
    informe_tecnico_id = fields.One2many('solicitudes.informe_tecnico', 'solicitudes_id', string="Informe tecnico")
    consejos_directivos_ids = fields.Many2many('aprobacion.consejos', string="Consejo directivo")
    #cuentas_cobrar_ids = fields.One2many('administracion.cuentas_cobrar', string="Cuenta por cobrar") #Error!!!
    #cheques_ids = fields.One2many('administracion.cheques', 'solicitudes_id', string="Cuenta por cobrar") #Error!!!

    # Cambia a la estacion "Consignar Requisitos"
    @api.one
    def action_estacion_consignacion_requisitos(self):
        self.state = 'estacion_1_consignacion_requisitos'

    # Cambia a la estacion "Control Previo"
    @api.one
    def action_estacion_control_previo(self):
        self.state = 'estacion_2_control_previo'

    # Cambia a la estacion "Inspeccion - Avaluo"
    @api.one
    def action_estacion_inspeccion_avaluo(self):
        self.state = 'estacion_3_inspeccion_avaluo'

    # Cambia a la estacion "Aprobacion Gerente"
    @api.one
    def action_estacion_evaluacion_gerente(self):
        self.state = 'estacion_4_evaluacion_gerente'

    # Cambia a la estacion "Aprobacion Secretaria"
    @api.one
    def action_estacion_evaluacion_presidencia(self):
        self.state = 'estacion_5_evaluacion_presidencia'

    # Cambia a la estacion "Aprobacion Consejo"
    @api.one
    def action_estacion_discusion_consejo(self):
        self.state = 'estacion_7_discusion_consejo'

    # Cambia a la estacion "Creacion Documentos"
    @api.one
    def action_estacion_creacion_documentos(self):
        self.state = 'estacion_8_creacion_documentos'

    # Cambia a la estacion "Liquidacion"
    @api.one
    def action_estacion_liquidacion(self):
        self.state = 'estacion_9_liquidacion'

    # Cambia al estatus "Aceptado" (gerencia)
    @api.one
    def action_estatus_aceptado_gerencia(self):
        self.estatus_gerencia_credito = 'estatus_aceptado'

    # Cambia al estatus "Aceptado Condicionado" (gerencia)
    @api.one
    def action_estatus_aprobado_cond_gerencia(self):
        self.estatus_gerencia_credito = 'estatus_aceptado_cond'

    # Cambia al estatus "Rechazado" (gerencia)
    @api.one
    def action_estatus_rechazado_gerencia(self):
        self.estatus_gerencia_credito = 'estatus_rechazado'

    # Cambia al estatus "Recomendado" (presidencia)
    @api.one
    def action_estatus_recomendado_presidencia(self):
        self.estatus_presidencia = 'estatus_recomendado'

    # Cambia al estatus "Recomendado Condicionado" (presidencia)
    @api.one
    def action_estatus_recomendado_cond_presidencia(self):
        self.estatus_presidencia = 'estatus_recomendado_cond'

    # Cambia al estatus "No recomendado" (presidencia)
    @api.one
    def action_estatus_no_recomendado_presidencia(self):
        self.estatus_presidencia = 'estatus_no_recomendado'

    # Cambia al estatus "Aprobado" (consejo)
    @api.one
    def action_estatus_aprobado_consejo(self):
        self.estatus_consejo_directivo = 'estatus_aprobado'

    # Cambia al estatus "Aprobado Condicionado" (consejo)
    @api.one
    def action_estatus_aprobado_cond_consejo(self):
        self.estatus_consejo_directivo = 'estatus_aprobado_cond'

    # Cambia al estatus "Negado" (consejo)
    @api.one
    def action_estatus_negado_consejo(self):
        self.estatus_consejo_directivo = 'estatus_negado'

    # Cambia al estatus "Diferido" (consejo)
    @api.one
    def action_estatus_diferido_consejo(self):
        self.estatus_consejo_directivo = 'estatus_diferido'



    # display_name = fields.Char(
    #     string='Número de expediente', compute='_compute_display_name',
    # )
    #
    # @api.one
    # @api.depends('nro_expediente')
    # def _compute_display_name(self):
    #     self.display_name = self.nro_expediente

    #grupo_actual = fields.Char(string="Usuario Actual", comodel_name='res.users', default = lambda self: self.env.user.name)
    #grupo_actual = fields.Char(string="Usuario Actual", comodel_name='res.groups', default = lambda self: self.env.user.)
    #grupo_responsable = fields.Selection(string='Usuario responsable', selection=[('group_analista_credito', 'Analista de credito'),('group_analista_juridico', 'Analista juridico'),('group_analista_economico', 'Analista Economico'),('group_gerente_credito', 'Gerente de credito'),('group_secretaria_ejecutiva', 'Secretaria Ejecutiva')],default='fomdes.group_analista_credito')

    """
    grupo_actual = fields.Char(compute='_compute_grupo')

    # Returns group id of current user
    def _compute_grupo(self, cr, uid, *args):
        user_obj = self.pool.get('res.users')
        #grupo_actual = user_obj.browse(cr, uid, uid)['groups_id']
        grupo_actual = read(cr, uid, [uid], context)[0]['groups_id']
        return grupo_actual or False

    # Returns id of current user
    def _compute_grupo(self, cr, uid, *args):
        user_obj = self.pool.get('res.users')
        user_value = user_obj.browse(cr, uid, uid)
        return user_value.login or False
    """

    """
    @api.one
    def action_secretaria_rechazar(self, cr, uid, ids, context=None):
        if not len(ids):
            return False
        self.write(cr, uid, ids, {'state':'draft','shipped':0})
        wf_service = netsvc.LocalService("workflow")
        for p_id in ids:
            # Deleting the existing instance of workflow
            wf_service.trg_delete(uid, 'solicitudes', p_id, cr)
            wf_service.trg_create(uid, 'solicitudes', p_id, cr)
        self.state = 'estacion_4_gerencia_credito'
        self.estatus_consejo_directivo = 'estatus_rechazado'
        return True
    """
