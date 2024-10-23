{
    'name': 'Asset Management Services',
    'summary': """Asset Management Service Extension""",
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
        'mgf_assets',
        'mgf_assets_applications',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/asset_service.xml',
        'views/asset_service_type_view.xml',
        'views/asset_service_menu.xml',
    ],
    'application': False,
    'installable': True,
}