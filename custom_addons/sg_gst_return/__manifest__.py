{
    "name": "Singapore - GST Return",
    "version": "1.1.1",
    "author": "Md. Hasibul Hasan Shovo",
    'category': 'Accounting & Finance/Account Reports',
    "website": "http://www.linkedin.com/in/hasibulhshovo",
    "description": """
        Singapore Accounting: QWeb reports of Account.
        ==============================================
        * Generation of GST form 5 and GST form 7 reports as per official l10n_sg COA.
    """,
    'depends': ['l10n_sg', 'sale', 'purchase', 'stock', 'web'],
    'data': [
        'data/gst_f5_report_config_data.xml',
        'security/ir.model.access.csv',
        'views/gst_f5_report_config_views.xml',
        'wizards/gst_f5_return_wizard_views.xml',
        'reports/gst_f5_return_report_tmpl.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
