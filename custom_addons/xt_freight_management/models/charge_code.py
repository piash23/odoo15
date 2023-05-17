from odoo import fields, models, api


class ChargeCode(models.Model):
    _name = "charge.code"
    _description = "Charge Code"

    item_code = fields.Char(string="Item Code", required=True)
    item_short_code = fields.Char(string="Item Short Code", required=False)
    item_description = fields.Text(string="Item Description", required=False)
    sales_cost = fields.Float(string="Sales/Cost", required=False)
    local_name = fields.Char(string="Local Name", required=False)
    charge_type = fields.Char(string="Charge Type", required=False)
    change_unit = fields.Char(string="Change Unit", required=False)
    module = fields.Char(string="Module", required=False)
    department_code = fields.Char(string="Department Code", required=False)
    cost_center_code = fields.Char(string="Cost Center Code", required=False)
    sales_account = fields.Many2one(
        comodel_name="account.account", string="Sales Account", required=False
    )
    cost_account = fields.Many2one(
        comodel_name="account.account", string="Cost Account", required=False
    )

    # problem here is understanding
    # sales_im_service_fee = fields.Float(
    #     string='IM-SERVICE-FEE',
    #     required=False)
    # cost_im_service_fee = fields.Float(
    #     string='IM-SERVICE-FEE',
    #     required=False)
    #################################
    sales_provision_account = fields.Many2one(
        comodel_name="account.account", string="Sales Provision Account", required=False
    )
    provision_account = fields.Many2one(
        comodel_name="account.account", string="Provision Account", required=False
    )
    billing_curr_code = fields.Many2one(
        comodel_name="res.currency", string="Billing Curr Code", required=False
    )
    code = fields.Char(string="Code", required=False)

    unit_of_measure = fields.Many2one(
        comodel_name="uom.uom", string="Unit Of Measurement", required=False
    )
    cost = fields.Float(string="Cost", required=False)
    consolidation_item_code = fields.Char(
        string="Consolidation Item Code", required=False
    )
    site_code = fields.Char(string="Site Code", required=False)
    sales_analysis_code = fields.Char(string="Sales Analysis Code", required=False)
    cost_analysis_code = fields.Char(string="Cost Analysis Code", required=False)
    charge_code_lines = fields.Many2one(
        comodel_name="charge.code.line", string="Charge Code Lines", required=False
    )


class ChargeCodeLine(models.Model):
    _name = "charge.code.line"
    _description = "Charge Code Line Description"

    module = fields.Char(string="Module", required=False)
    job_type = fields.Char(string="Job_type", required=False)
    sales_acc_code = fields.Many2one(
        comodel_name="account.account", string="Sales Acc Code", required=False
    )
    sales_description = fields.Text(string="Sales Description", required=False)
    cost_acc_code = fields.Many2one(
        comodel_name="account.account", string="Cost Acc Code", required=False
    )
    cost_description = fields.Text(string="Cost Description", required=False)
    charge_code_id = fields.Many2one(
        comodel_name="charge.code", string="Charge_code_id"
    )
