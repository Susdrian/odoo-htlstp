{
    'name': 'Asset Management Application',
    'summary': """Asset Management Application Extension""",
    'version': '18.0.1.0.3',
    'category': 'Asset/Management',
    'license': 'OPL-1',
    'author': 'mgfranke.io',
    'website': 'https://mgfranke.io',
    'contributors': [
        'Georg Franke <georg@mgfranke.com>',
    ],
    'depends': [
        'base',
        'web',
        'mgf_assets',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/asset_applications_version_view.xml',
        'views/asset_applications_view.xml',
        'views/asset_applications_menu.xml',
    ],
    'application': False,
    'installable': True,
}
