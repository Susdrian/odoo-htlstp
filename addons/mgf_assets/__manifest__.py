{
    'name': 'Asset Management',
    'summary': """General Asset Management""",
    'version': '16.0.1.0.3',
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
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/asset_asset.xml',
        'views/asset_menu.xml',
        'views/res_partner.xml',
    ],
    'application': True,
    'installable': True,
}
