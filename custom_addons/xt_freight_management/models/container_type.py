from odoo import fields, models, api


class ContainerType(models.Model):
    _name = "container.type"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Container Type"

    container_code = fields.Char(string="Container Code", required=True)
    description = fields.Text(string="Description", required=False)
    size = fields.Char(string="Size", required=True)
    no_of_teu = fields.Float(string="No. Of TEU", required=False)
    max_cubic_ft = fields.Float(
        string="Max Cubic Ft",
        digits=(10, 4),
        required=False,
    )
    max_volume = fields.Float(string="Max Volume in m3", digits=(10, 4), required=False)
    max_weight = fields.Float(string="Max Weight in kg", digits=(10, 4), required=False)
    temperature_flag = fields.Char(string="Temperature flag", required=False)
