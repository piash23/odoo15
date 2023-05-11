from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Division(models.Model):
    _name = "division"
    _description = "Division"
    _order = "id desc"

    name = fields.Char("Name", required=True, help='Name of the division')
    code = fields.Char("Code", help='Code for the division')
    active = fields.Boolean("Active", default=True)

    @api.constrains("name")
    def _check_unique_name(self):
        for rec in self:
            if rec.name:
                msg = "'%s' already exists!" % rec.name
                envobj = self.env['division'].search([('id', '!=', rec.id), ('name', '=', rec.name), '|', ('active', '=', True), ('active', '=', False)], limit=1)
                if envobj:
                    raise ValidationError(msg)

    @api.constrains("code")
    def _check_unique_code(self):
        for rec in self:
            if rec.code:
                msg = "'%s' already exists!" % rec.code
                envobj = self.env['division'].search([('id', '!=', rec.id), ('name', '=', rec.code), '|', ('active', '=', True), ('active', '=', False)], limit=1)
                if envobj:
                    raise ValidationError(msg)