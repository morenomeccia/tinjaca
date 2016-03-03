# -*- coding: utf-8 -*-
{
    'name': "Tinjaca - Consejos",

    'summary': """ 
        Discusion de agendas y solicitudes de creditos del FOMDES.
     """,

    'description': """
		Tinjaca - Modulo Consejos (FOMDES)
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tinjaca',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','fomdes'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/consejos_views.xml',
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
