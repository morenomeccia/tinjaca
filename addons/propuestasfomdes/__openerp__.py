# -*- coding: utf-8 -*-
{
    'name': "Tinjaca - Propuestas X",

    'summary': """
        Recepción de propuestas de financiamiento y gestion de talleres de induccion
    """,

    'description': """
        Tinjaca - Modulo Propuestas (FOMDES)
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tinjaca',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','politicas'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
        'views/propuestas_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}