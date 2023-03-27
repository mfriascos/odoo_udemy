# -*- coding: utf-8 -*-
{
    'name': "custom_crm",

    'summary': """
    Módulo CRM parala gestión de visitas""",

    'description': """
    Módulo CRM parala gestión de visitas""",

    'author': "Mario Riascos",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': [
        'base',
        'sale_management',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/custom_sales_order_view.xml',
    ],

}