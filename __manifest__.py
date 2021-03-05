# -*- coding: utf-8 -*-
{
    'name': 'Fleet extension',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
    'sequence': 110,
    'summary': 'Fleet, Insurance, Equipment',
    'company': 'Daniel Demedziuk',
    'description': """
Fleet module extension
==================================
This addition to the Fleet module extends the basic module with additional data such as:
- date of registration inspection
- car equipment
- tyre type
and more.

If you need help, contact the author of the module.

email: daniel.demedziuk@gmail.com
""",
    'website': 'website',
    'category': 'Tool',
    'depends': ['base', 'mail', 'fleet'],
    'data': [
        'views/fleet_extension_view.xml',
        'views/vehicle_odometer_log_view.xml',
        ],
    'auto_install': False,
    'application': True,
    'installable': True,
}
