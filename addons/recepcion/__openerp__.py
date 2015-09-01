# -*- coding: utf-8 -*-
{
    'name': "Recepción",

    'summary': """
        Módulo de Gestión de visitantes a la recepción""",

    'description': """
Módulo de Gestión de visitantes a la recepción
==============================================

Registra las visitas a FOMDES especificando la fecha y la dependencia destino.

Genera como reportes visitas por rangos de fechas y por dependencia.
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Visitas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'models/model_recepcion.py',
        'views/recepcion.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}