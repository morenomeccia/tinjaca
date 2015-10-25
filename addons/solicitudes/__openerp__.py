# -*- coding: utf-8 -*-
{
    'name': "Tinjaca-Solicitudes",

    'summary': """
        Modulo para la gestion de solicitudes de credito del FOMDES
    """,

    'description': """
        Tinjaca - Modulo Solicitudes (FOMDES)
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['politicas'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        #'security/security.xml',
        'templates.xml',
        'views/solicitudes_views.xml',
        'views/solicitudes_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
