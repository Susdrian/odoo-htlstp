{
    'name': 'Asset Management Devices',
    'summary': """Asset Management Device Extension""",
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
        'htlstp_assets',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/asset_device.xml',
        'views/asset_device_type_view.xml',
        'views/asset_device_menu.xml',
    ],
    'application': False,
    'installable': True,
}
