from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PaymentTerm(models.Model):
    _name = "payment.term"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Payment Term"
    _order = "id desc"

    code = fields.Char("Code", help='Code for the payment term')
    description = fields.Char("Description", help='Description for the payment term')
    net_days = fields.Float("Net Days")
    discount_days = fields.Float("Discount Days")
    discount_percent = fields.Float("Discount Percentage")
    service_charge_min_amt = fields.Float("Service Charge Minimum Amount")
    service_charge_percent = fields.Float("Service Charge Percentage")
    active = fields.Boolean("Active", default=True)

    @api.constrains("code")
    def _check_unique_code(self):
        for rec in self:
            if rec.code:
                msg = "'%s' already exists!" % rec.code
                envobj = self.env['payment.term'].search([('id', '!=', rec.id), ('name', '=', rec.code), '|', ('active', '=', True), ('active', '=', False)], limit=1)
                if envobj:
                    raise ValidationError(msg)