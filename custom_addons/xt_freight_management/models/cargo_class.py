from odoo import fields, models, api


class CargoClass(models.Model):
    _name = "cargo.class"
    _description = "Cargo Class"

    trx_no = fields.Integer(string="Trx No", required=True)
    cargo_class_code = fields.Integer(string="Cargo Class Code", required=True)
    cargo_class_description = fields.Text(
        string="Cargo Class Description", required=False
    )
