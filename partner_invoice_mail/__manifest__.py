# -*- coding: utf-8 -*-
{
    'name': "partner_invoice_mail",

    'summary': """
        This Module adds a checkbox to partner in order to notify the user to send the invoice via mail""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Jan Beckhoff",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '11.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/views.xml'
    ],
}
