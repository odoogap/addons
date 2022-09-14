{
    'name': "BOM_Seller_warning",
    'version': '1.0',
    'author': "Odoo Gap",
    'summary': 'Show warning if there is no BOM and seller and prevent publishing',
    'description': 'free and available items',
    'website': "https://www.odoogap.com",
    'depends': [
        'sale',
        'website_sale',
        'stock',
        'mrp',

    ],
    'data':['views/view.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}