# -*- coding: utf-8 -*-
{
    'name': "Tinjaca - Propuestas",

    'summary': """
        Recepción de propuestas de financiamiento del FOMDES y organizacion de talleres de induccion
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
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base','fomdes','politicas','contactos'],

    # always loaded
    'data': [
        # 'templates.xml',
        # 'security/ir.model.access.csv',
        'views/solicitantes_views.xml',
        'views/talleres_views.xml',
        'views/propuestas_views.xml',
        'views/propuestas_workflow.xml',
        'views/propuestas_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
