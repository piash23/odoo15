from odoo import fields, models, api


class FreightCharge(models.Model):
    _name = "freight.charge"
    _description = "Freight Charge Description"

    charge_table_no = fields.Char(string="Charge Table No", readonly=True)
    description = fields.Text(string="Description", required=False)
    job_type = fields.Char(string="Job Type", required=False)
    module = fields.Char(string="Module", required=False)
    est_transit_time = fields.Integer(string="Est. Transit Time", required=False)
    frequency = fields.Char(string="Frequency", required=False)
    customer_code = fields.Char(string="Customer Code", required=False)
    port_of_loading = fields.Many2one(
        comodel_name="port.info", string="Port Of Loading", required=False
    )
    port_of_discharge = fields.Many2one(
        comodel_name="port.info", string="Port Of Discharge", required=False
    )
    destination = fields.Many2one(
        comodel_name="res.country.state", string="Destination", required=False
    )
    valid_flag = fields.Boolean(string="Valid Flag", required=False)
    standard_charge_flag = fields.Boolean(string="Standard Charge Flag", required=False)

    via_port_1 = fields.Char(string="Via Port1", required=False)
    via_port_2 = fields.Char(string="Via Port2", required=False)

    frt_collect = fields.Char(string="Frt Collect", required=False)

    effective_date = fields.Date(string="Effective_date", required=False)
    expiry_date = fields.Date(string="Expiry date", required=False)
    note = fields.Text(string="Note", required=False)
    charge_lines = fields.One2many(
        comodel_name="freight.charge.lines",
        inverse_name="charge_id",
        string="Charge Lines",
        required=False,
    )


class FreightChargeLine(models.Model):
    _name = "freight.charge.lines"
    _description = "Freight Charge Line Description"

    item_code = fields.Char(string="Item Code", required=False)
    description = fields.Text(string="Description", required=False)
    qty = fields.Float(string="Qty", digits=(10, 4), required=False)

    cargo = fields.Selection(
        string="Cargo",
        selection=[
            ("fcl", "FCL"),
            ("lcl", "LCL"),
        ],
        default="fcl",
    )
    dg = fields.Char(string="DG", required=False)
    uom = fields.Many2one(comodel_name="uom.uom", string="UOM", required=False)
    chg = fields.Boolean(string="Chg", required=False)
    vat = fields.Many2one(comodel_name="account.tax", string="Vat", required=False)
    p_c = fields.Char(string="P/c", required=False)
    chg_unit = fields.Char(string="Chg Unit", required=False)
    cont = fields.Char(string="Cont", required=False)
    rate = fields.Char(string="Rate", default="Std Rate")
    Unit = fields.Char(string="Unit", default="DEFAULT")
    curr = fields.Many2one(comodel_name="res.currency", string="Curr", required=False)
    min_amt = fields.Float(string="MinAmt", required=False)
    amt = fields.Float(string="Amt", digits=(10, 4), required=False)
    cost = fields.Float(string="Cost", required=False)
    charge_id = fields.Many2one(
        comodel_name="freight.charge", string="Charge ID", required=False
    )
