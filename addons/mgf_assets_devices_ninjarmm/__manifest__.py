{
    'name': 'Asset Management Devices NinjaRMM',
    'summary': """Asset Management Device Ninja RMMExtension """,
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
        'mgf_assets_applications',
        'mgf_assets_devices'
    ],
    'data': [
        'views/res_partner.xml'
    ],
    'application': False,
    'installable': True,
}
