from odoo import fields, models, api


class PortInfo(models.Model):
    _name = "port.info"
    _description = "Details about Ports"

    port_code = fields.Char(string="Port Code", required=True)
    name = fields.Char(string="Name", required=False)
    country_id = fields.Many2one(
        comodel_name="res.country", string="Country", required=True
    )
    country_code = fields.Char(related="country_id.code", readonly=True, string="Country Code")
    created_by = fields.Char(string='Created By', readonly=True)
    dg_cargo = fields.Char(string="DG Cargo", required=False)

    @api.model
    def create(self, vals):
        # Set the created_by field to the current user
        vals['created_by'] = self.env.user.name
        return super(PortInfo, self).create(vals)
