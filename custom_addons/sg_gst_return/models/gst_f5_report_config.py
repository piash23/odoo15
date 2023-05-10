from odoo import models, fields


class GSTF5ReportConfig(models.Model):
    _name = 'gst.f5.report.config'

    name = fields.Char('Tax Category Name')


class AccountTax(models.Model):
    _inherit = 'account.tax'

    category_ids = fields.Many2many('gst.f5.report.config', 'category_config_rel', 'tax_id', 'category_id',
                                    'GST F5 report Category')
