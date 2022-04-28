# -*- coding: utf-8 -*-
{
    'name': "gestionAlternant",

    'summary': """
        """,

    'description': """
        Module permettant la gestion d'un alternant ainsi que sa classe et son entreprise
    """,

    'author': "Clémence Amélineau",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/gestionAlternant.xml',
        'views/templates.xml',
        'views/gestionAlternant.xml',
        'menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
