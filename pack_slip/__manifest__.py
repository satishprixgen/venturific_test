{
    'name': 'Venturific Pack Print',
    'version': '13.0.0.6',
    'category': 'Inventory',
    'author': 'Prixgen Tech Solutions Pvt Ltd.',
    'company': 'Prixgen Tech Solutions Pvt Ltd.',
    'website': 'https://www.prixgen.com',
    'depends': ['base','stock','sale','account'],
    'data': [
        'reports/single_pack.xml',
        'data/sequence.xml',
        'wizards/print_doc.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/stock_quants_package.xml',
        'reports/pack_report_inherit.xml',
        'reports/sale_order_pack_print.xml',

        
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}