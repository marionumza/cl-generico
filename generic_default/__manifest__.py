# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (C) 2018  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'generico',
    'version': '9.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customizacion para Clientes Genericos',
    'author': 'jeo Software',
    'depends': [
        'sale_management',
        'account_invoicing',
        'purchase',
        'project',

        # para la localizacion argentina
        'l10n_ar_account',
        'l10n_ar_afipws_fe',        # Factura Electrónica Argentina
        'l10n_ar_aeroo_einvoice',   # impresion de factura electronica aeroo
        'l10n_ar_account_vat_ledger_citi',
        'account_debt_management',  #
        'l10n_ar_aeroo_payment_group',  #
    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '98069',
    'repos': [
        {'usr': 'marionumza', 'repo': 'cl-generico', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'odoo-argentina', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'account-financial-tools', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'account-payment', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'miscellaneous', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'argentina-reporting', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'reporting-engine', 'branch': '9.0'},
        {'usr': 'ingadhoc', 'repo': 'aeroo_reports', 'branch': '9.0'},
        {'usr': 'OCA', 'repo': 'partner-contact', 'branch': '9.0'},
        {'usr': 'rafi16jan', 'repo': 'backend-theme', 'branch': '9.0'},
        {'usr': 'it-projects-llc', 'repo': 'pos-addons', 'branch': '9.0'},
        {'usr': 'it-projects-llc', 'repo': 'misc-addons', 'branch': '9.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.6'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
        {'name': 'aeroo', 'usr': 'adhoc', 'img': 'aeroo-docs'},
    ]
}
