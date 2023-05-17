from odoo import fields, models, api


class ShippingLine(models.Model):
    _name = "shipping.line"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Shipping Line"

    shipping_line_code = fields.Char(string="Shipping Line Code", required=True)
    business_party_code = fields.Char(string="Business Party Code", required=False)
    name = fields.Char(string="Name", required=False)
    street = fields.Char(string="Street", required=False)
    street2 = fields.Char(string="Street2", required=False)

    city = fields.Char(string="City", required=False)
    state_id = fields.Many2one(
        comodel_name="res.country.state", string="State_id", required=False
    )
    zip = fields.Char(string="Zip", required=False)
    country_id = fields.Many2one(
        comodel_name="res.country", string="Country", required=False
    )

    telephone = fields.Char(string="Telephone", required=False)
    fax = fields.Char(string="Fax", required=False)
    email = fields.Char(string="E-mail", required=False)
    web_site = fields.Char(string="Web_site", required=False)
    contact = fields.Char(string="Contact", required=False)
    cr_no = fields.Char(string="Cr No", required=False)
    analysis_code = fields.Char(string="Analysis Code", required=False)
    country_code = fields.Char(
        related="country_id.code", readonly=True, string="Country Code"
    )
