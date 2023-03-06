# -*- coding: utf-8 -*-
{
    'name': "Instrumentos Musicais",

    'summary': """Organiza as túas vendas de instrumentos/reparacións etc ...""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jesús Taboada Iglesias",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/instrumentos_tenda_views.xml',
        'views/instrumentos_instrumento_views.xml',
        'views/instrumentos_reparacion_views.xml',
        'views/instrumentos_empleado_views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
