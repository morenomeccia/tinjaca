# -*- coding: utf-8 -*-
{
    'name': "Tinjaca - Aprobacion",

    'summary': """ 
        Aprobacion de solicitudes de credito del FOMDES
     """,

    'description': """
		Tinjaca - Modulo Solicitudes (FOMDES)
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
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/aprobacion_views.xml',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
