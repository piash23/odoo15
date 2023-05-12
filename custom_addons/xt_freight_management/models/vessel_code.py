from odoo import fields, models, api


class VesselCode(models.Model):
    _name = 'vessel.code'
    _description = 'Vessel Code'
    
    vessel_code = fields.Char(
        string='Vessel Code', 
        required=True)
    name = fields.Char(
        string='Name', 
        required=False)
    type = fields.Char(
        string='Type', 
        required=False)
    shipping_line = fields.Many2one(
        comodel_name='shipping.line',
        string='Shipping Line',
        required=False)
    ship_owner = fields.Char(
        string='Ship Owner',
        required=False)
    nrt = fields.Float(
        string='NRT',
        required=False)
    grt = fields.Float(
        string='GRT',
        required=False)
    country_flag = fields.Char(
        string='Country Flag',
        required=False)
    year_build = fields.Integer(
        string='Year Build',
        required=False)
