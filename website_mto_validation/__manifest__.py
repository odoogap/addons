{
    'name': "Website MTO Validation",
    'version': '15.0.1.0',
    'author': "ERPGAP",
    'summary': 'Show warning if MTO and there is no BOM and seller and prevent publishing',
    'description': 'Show warning if MTO and there is no BOM and seller and prevent publishing',
    'website': "https://www.erpgap.com",
    'depends': [
        'sale',
        'website_sale',
        'stock',
        'mrp',
        'purchase'
    ],
    'data': [
        'views/product_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}