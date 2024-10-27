
{
    'name': 'Password Manager 1.0.5',
    'version': '17.0.1.0.5',
    'summary': 'Password Manager',
    'description': """Password Manager""",
    'author': 'Appeul Services',
    'company': 'Appeul',
    'maintainer': 'Appeul Services',
    'category': 'Sales',
    'website': 'https://www.appeul.com',
    'sequence':"5210",
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/pw_manager_view.xml',
        'views/menus.xml',

    ],
    'installable': True,
    'application': True,

    'license': 'LGPL-3',

}
