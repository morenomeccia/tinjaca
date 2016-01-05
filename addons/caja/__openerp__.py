# -*- coding: utf-8 -*-
{
    'name': "Tinjaca - Caja",

    'summary': """
        Registro de los pagos recibidos por cancelacion de creditos aprobados por el FOMDES
    """,

    'description': """
        Tinjaca - Modulo Caja (FOMDES)
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tinjaca',
    'version': '0.1',


    # any module necessary for this one to work correctly
    'depends': ['base','fomdes','solicitudes'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
        'views/caja_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}