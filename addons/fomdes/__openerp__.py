# -*- coding: utf-8 -*-
{
    'name': "Tinjaca - Fomdes",

    'summary': """
        Definicion de la estructura, grupos y departamentos del FOMDES
    """,

    'description': """
        Tinjaca - Modulo Fomdes (FOMDES)
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tinjaca',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        #'security/ir.model.access.csv',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
