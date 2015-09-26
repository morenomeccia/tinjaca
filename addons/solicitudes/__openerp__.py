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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/solicitudes.xml',
        'views/solicitudes_workflow.xml',
        'data/solicitudes.documentos_sector.csv',
        'data/solicitudes.documentos_garantia.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
