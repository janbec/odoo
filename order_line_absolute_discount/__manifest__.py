# -*- coding: utf-8 -*-
{
    'name': "order_line_absolute_discount",

    'summary': """
        Adds the possibility to choose an absolute discount in sale order lines and computes total discount across all order/invoice lines. Also enables relative discounts on Purchase Order lines.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jan Beckhoff",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'account', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/purchase_views.xml'
    ]
}
