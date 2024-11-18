{
    'name': 'SB Subscription',
    'summary': """Subscription reenable Subscription to Draft & Set the Period for the whole Invoice""",
    'version': '18.0.1.0.3',
    'category': 'Sales',
    'license': 'OPL-1',
    'author': 'stpehanbartl GmbH',
    'website': 'https://stephanbartl.at',
    'contributors': [
        'Georg Franke <georg.franke@sb.solutions>',
    ],
    'depends': [
        'sale_subscription',
        'sale_temporal',
        'sale_management',
        'muk_sb_account'
    ],
    'data': [
        'views/sale_temporal.xml',
    ],
    'application': False,
    'installable': True,
}
