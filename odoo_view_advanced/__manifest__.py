# -*- coding: utf-8 -*-
{
    'name': "odoo_view_advanced",

    'summary': """
        Conceptos avanzados de vistas""",

    'description': """
        Curso de conceptos avanzados de vistas
    """,

    'author': "Darío Rodríguez García",
    'website': "https://www.udemy.com/user/dario-rodriguez-garcia/",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
