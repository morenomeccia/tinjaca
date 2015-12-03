# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Solicitudes(models.Model):
    _name = 'solicitudes.solicitudes'

    _rec_name = 'nro_expediente'

    nro_expediente = fields.Char(string='Numero de expediente', required=True)

    state = fields.Selection(string='Estacion', selection=[('estacion_1_analisis_credito', 'Informacion de credito'),
                                                           ('estacion_2_analisis_juridico', 'Analisis juridico'),
                                                           ('estacion_3_analisis_economico', 'Analisis economico'),
                                                           ('estacion_4_gerencia_credito', 'Gerencia de credito'),
                                                           ('estacion_5_verificar_secretaria', 'Secretaria ejecutiva (por verificar)'),
                                                           ('estacion_6_aprobar_secretaria', 'Secretaria ejecutiva (por aprobar)'), 
                                                           ('estacion_7_crear_documentos_secretaria', 'Secretaria ejecutiva (crear documentos)'),
                                                           ('estacion_8_liquidacion', 'Liquidacion')], 
                                                           default='estacion_1_analisis_credito')

    estatus_consejo_directivo = fields.Selection(string='Estatus', selection=[('estatus_discutir', 'Por discutir'),
                                                                              ('estatus_rechazado', 'Rechazado'),
                                                                              ('estatus_aprobado', 'Aprobado'),
                                                                              ('estatus_diferido', 'Diferido')],
                                                                              default='estatus_discutir')

    grupo_responsable = fields.Selection(string='Usuario responsable', selection=[('fomdes.group_analista_credito', 'Analista de credito'),
                                                                                  ('fomdes.group_analista_juridico', 'Analista juridico'),
                                                                                  ('fomdes.group_analista_economico', 'Analista Economico'),
                                                                                  ('fomdes.group_gerente_credito', 'Gerente de credito'),
                                                                                  ('fomdes.group_secretaria_ejecutiva', 'Secretaria Ejecutiva')],
                                                                                  default='fomdes.group_analista_credito')

    # Campos provinientes de propuestas:
    sector_id = fields.Many2one('politicas.sectores', string="Sector")
    garantia_id = fields.Many2one('politicas.garantias', string="Garantia")
    empresa_promocional = fields.Boolean(string='Empresa promocional?')

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
    fecha_de_entrega = fields.Date()
    lapso_de_devolucion = fields.Integer(string='Lapso de devolucion del documento')

    # Referencias a otros modelos:
    requisitos_generales_id = fields.One2many('solicitudes.requisitos_generales', 'solicitudes_id', string="Requisitos generales")
    requisitos_sector_id = fields.One2many('solicitudes.requisitos_sector', 'solicitudes_id', string="Requisitos sector")
    requisitos_garantia_id = fields.One2many('solicitudes.requisitos_garantia', 'solicitudes_id', string="Requisitos garantia")
    requisitos_empresa_id = fields.One2many('solicitudes.requisitos_empresa', 'solicitudes_id', string="Requisitos empresa")
    control_previo_id = fields.One2many('solicitudes.control_previo', 'solicitudes_id', string="Control Previo")
    avaluo_id = fields.One2many('solicitudes.inspecciones', 'solicitudes_id', string="Avaluo")
    inspeccion_id = fields.One2many('solicitudes.inspecciones', 'solicitudes_id', string="Inspeccion")
    informe_tecnico_id = fields.One2many('solicitudes.informe_tecnico', 'solicitudes_id', string="Informe tecnico")

    grupo_actual = fields.Char(compute='_compute_grupo')

    def _compute_grupo(self, cr, uid, *args):
        user_obj = self.pool.get('res.users')
        grupo_actual = user_obj.browse(cr, uid, uid)['groups_id']
        return grupo_actual or False

    """
    def _compute_grupo(self, cr, uid, *args):
        user_obj = self.pool.get('res.users')
        user_value = user_obj.browse(cr, uid, uid)
        return user_value.login or False
    """


    # Envia a la estacion "Informacion de credito"
    @api.one
    def action_enviar_informacion_credito(self):
        self.state = 'estacion_1_analisis_credito'
        self.grupo_responsable = 'group_analista_credito'

    # Envia a la estacion "Analisis Juridico"
    @api.one
    def action_enviar_analisis_juridico(self):
        self.state = 'estacion_2_analisis_juridico'
        self.grupo_responsable = 'group_analista_juridico'

    # Envia a la estacion "Analisis Economico"
    @api.one
    def action_enviar_analisis_economico(self):
        self.state = 'estacion_3_analisis_economico'
        self.grupo_responsable = 'group_analista_economico'

    # Envia a la estacion "Gerencia de credito"
    @api.one
    def action_enviar_gerencia_credito(self):
        self.state = 'estacion_4_gerencia_credito'
        self.grupo_responsable = 'group_gerente_credito'

    # Envia a la estacion "Secretaria ejecutiva (por verificar)", boton "Enviar a secretaria ejecutiva"
    @api.one
    def action_enviar_secretaria_verificar(self):
        self.state = 'estacion_5_verificar_secretaria'
        self.grupo_responsable = 'group_secretaria_ejecutiva'

    # Envia a la estacion "Secretaria ejecutiva (por aprobar)", boton "verificado"
    @api.one
    def action_enviar_secretaria_aprobar(self):
        self.state = 'estacion_6_aprobar_secretaria'
        self.grupo_responsable = 'group_secretaria_ejecutiva'

    # Envia a la estacion "Secretaria ejecutiva (crear documentos)", boton "aprobar"
    @api.one
    def action_enviar_secretaria_documentar(self):
        self.state = 'estacion_7_crear_documentos_secretaria'
        self.estatus_consejo_directivo = 'estatus_aprobado'
        self.grupo_responsable = 'group_secretaria_ejecutiva'

    # Envia a la estacion "Gerencia de credito", boton "Rechazar"
    @api.one
    def action_secretaria_rechazar(self):
        self.state = 'estacion_4_gerencia_credito'
        self.estatus_consejo_directivo = 'estatus_rechazado'
        self.grupo_responsable = 'group_gerente_credito'

    # Envia a la estacion "Gerencia de credito", boton "Diferir"
    @api.one
    def action_secretaria_diferir(self):
        self.state = 'estacion_4_gerencia_credito'
        self.estatus_consejo_directivo = 'estatus_diferido'
        self.grupo_responsable = 'group_gerente_credito'

    # Envia a la estacion "Liquidacion", boton "Enviar a liquidacion"
    @api.one
    def action_enviar_liquidacion(self):
        self.state = 'estacion_8_liquidacion'

    # display_name = fields.Char(
    #     string='Número de expediente', compute='_compute_display_name',
    # )
    #
    # @api.one
    # @api.depends('nro_expediente')
    # def _compute_display_name(self):
    #     self.display_name = self.nro_expediente
