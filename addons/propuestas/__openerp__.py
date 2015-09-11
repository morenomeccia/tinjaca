# -*- coding: utf-8 -*-
{
    'name': "propuestas",

    'summary': """
        Este módulo abarca los procesos de Recepción de propuestas""",

    'description': """
Módulo de Gestión de Propuestas
=================================

        Este módulo abarca los procesos de 'Recepción de propuestas'. Incluye procedimientos asociados con la recepción y
validación de la propuesta de financiamiento y la inclusión de los solicitantes a las listas de los talleres de inducción.
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/propuestas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}