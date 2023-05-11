from odoo import fields, models, api


class ShippingLine(models.Model):
    _name = 'shipping.line'
    _description = 'Shipping Line'

    shipping_line_code = fields.Char(
        string='Shipping Line Code',
        required=True)
    business_party_code = fields.Char(
        string='Business Party Code',
        required=False)
    name = fields.Char(
        string='Name',
        required=False)
    # address = fields.Char(
    #     string='Address',
    #     required=False)
    city = fields.Char(
        string='City', 
        required=False)
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        required=False)

    telephone = fields.Char(
        string='Telephone',
        required=False)
    fax = fields.Char(
        string='Fax',
        required=False)
    email = fields.Char(
        string='E-mail',
        required=False)
    web_site = fields.Char(
        string='Web_site',
        required=False)
    contact = fields.Char(
        string='Contact',
        required=False)
    cr_no = fields.Char(
        string='Cr No',
        required=False)
    analysis_code = fields.Char(
        string='Analysis Code',
        required=False)
