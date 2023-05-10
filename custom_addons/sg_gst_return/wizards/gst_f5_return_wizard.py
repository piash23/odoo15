from odoo import fields, models, _, api
from odoo.exceptions import ValidationError
import time
from datetime import datetime
from dateutil import relativedelta
from odoo.tools.misc import formatLang


class GstF5ReturnWizard(models.TransientModel):
    _name = 'gst.f5.return.wizard'
    _inherit = 'account.common.report'

    target_move = fields.Selection([('posted', 'All Posted Entries'),
                                    ('all', 'All Entries'),
                                    ], string='Target Moves', required=True, default='posted')
    # journal_ids = fields.Many2many(
    #     comodel_name='account.journal',
    #     string='Journals',
    #     required=True,
    #     default=lambda self: self.env['account.journal'].search([('company_id', '=', self.company_id.id)]),
    #     domain="[('company_id', '=', company_id)]",
    # )
    date_from = fields.Date('Start Date', required=True, default=lambda *a: time.strftime('%Y-%m-01'))
    date_to = fields.Date('End Date', required=True, default=lambda *a: str(
        datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10])
    box10 = fields.Float('Box 10 (GST Refunds Claimed)')
    box11 = fields.Float('Box 11 (Bad Debt Relief Claimed)')
    box12 = fields.Float('Box 12 (Pre-Registration Claimed)')

    @api.constrains('date_from', 'date_to')
    def date_constrains(self):
        if self.date_to < self.date_from:
            raise ValidationError(_('From date cannot be less than the to date.'))

    def print_pdf(self):
        data = self._prepare_data()
        return self.env.ref(
            'sg_gst_return.gst_return_report_f5_tmpl').with_context(
            landscape=False).report_action(self, data=data)

    def _prepare_data(self):
        tax_list = []
        move_line_obj = self.env['account.move.line']
        account_tax = self.env['account.tax']
        config_obj = self.env['gst.f5.report.config']
        box1 = box2 = box3 = box4 = box5 = box6 = box7 = box8 = box9 = box10 = box11 = box12 = box13 = 0.00
        tot = tot_tax = pur_tax = tot_pur = tot_rated = 0.0
        box1_tot = box2_tot = box3_tot = box5_tot = box6_tot = box7_tot = box9_tot = box13_tot = 0.0
        box10 = self.box10
        box11 = self.box11
        box12 = self.box12
        date_from = self.date_from
        date_to = self.date_to
        company_id = self.env.company
        company_name = self.env.company.name
        gst_no = company_id.vat or False

        domain = [('date', '>=', date_from), ('date', '<=', date_to)]
        if self.target_move == 'posted':
            domain += [('move_id.state', '=', 'posted')]

        # tax_ids_box1 = account_tax.search([('name', 'in', ['Sales Tax 7% SR','Sales Tax 7% DS'])])
        tax_ids_box1 = account_tax.search(
            [('category_ids', 'in', self.env.ref('sg_gst_return.standard_rated_supplies').id)])
        move_lines = move_line_obj.search(domain + [('tax_ids', 'in', tax_ids_box1.ids)])
        if move_lines and move_lines.ids:
            for move in move_lines:
                box1_tot += move.credit

        # tax_ids_box2 = account_tax.search([('name', 'in', ['Sales Tax 0% OS','Sales Tax 0% ZR'])])
        tax_ids_box2 = account_tax.search([('category_ids', 'in', self.env.ref('sg_gst_return.zero_rated_supplies').ids)])
        move_lines2 = move_line_obj.search(domain + [('tax_ids', 'in', tax_ids_box2.ids)])
        if move_lines2 and move_lines2.ids:
            for move2 in move_lines2:
                box2_tot += move2.credit

        # tax_ids_box3 = account_tax.search([('name', 'in', ['Sales Tax 0% ES33','Sales Tax 0% ESN33'])])
        tax_ids_box3 = account_tax.search([('category_ids', 'in', self.env.ref('sg_gst_return.exempt_supplies').ids)])
        move_lines3 = move_line_obj.search(domain + [('tax_ids', 'in', tax_ids_box3.ids)])
        if move_lines3 and move_lines3.ids:
            for move3 in move_lines3:
                box3_tot += move3.credit

        # tax_ids_box5 = account_tax.search([('name', 'in', ['Purchase Tax 0% EP','Purchase Tax 0% ME','Purchase Tax 0% NR','Purchase Tax 0% OP',
        #                                                    'Purchase Tax 0% ZP','Purchase Tax 7% BL','Purchase Tax 7% IM','Purchase Tax 7% TX7',
        #                                                    'Purchase Tax 7% TX-E33','Purchase Tax 7% TX-N33','Purchase Tax 7% TX-RE'])])
        tax_ids_box5 = account_tax.search(
            [('category_ids', 'in', self.env.ref('sg_gst_return.taxable_purchases').ids)])
        move_lines5 = move_line_obj.search(domain + [('tax_ids', 'in', tax_ids_box5.ids)])
        if move_lines5 and move_lines5.ids:
            for move5 in move_lines5:
                box5_tot += move5.debit

        move_lines6 = move_line_obj.search(domain + [('tax_line_id', 'in', tax_ids_box1.ids)])
        if move_lines6 and move_lines6.ids:
            for move6 in move_lines6:
                box6_tot += move6.credit
                box6_tot -= move6.debit

        move_lines7 = move_line_obj.search(domain + [('tax_line_id', 'in', tax_ids_box5.ids)])
        if move_lines7 and move_lines7.ids:
            for move7 in move_lines7:
                box7_tot += move7.debit
                box7_tot -= move7.credit

        # tax_ids_box9 = account_tax.search([('name', 'in', ['Purchase Tax MES'])])
        tax_ids_box9 = account_tax.search(
            [('category_ids', 'in', self.env.ref('sg_gst_return.goods_imported_under_this_scheme').ids)])
        move_lines9 = move_line_obj.search(domain + [('tax_ids', 'in', tax_ids_box9.ids)])
        if move_lines9 and move_lines9.ids:
            for move9 in move_lines9:
                box9_tot += move9.debit

        tax_ids_box13 = [13, 14]
        move_lines13 = move_line_obj.search(domain + [('account_id.user_type_id', 'in', tax_ids_box13)])
        if move_lines13 and move_lines13.ids:
            for move13 in move_lines13:
                box13_tot += move13.credit
                box13_tot -= move13.debit

        box1 = box1_tot
        box2 = box2_tot
        box3 = box3_tot
        box4 = box1_tot + box2_tot + box3_tot
        box5 = box5_tot
        box6 = box6_tot
        box7 = box7_tot
        box8 = box7_tot - box6_tot
        box9 = box9_tot
        box13 = box13_tot

        tax_list.append({'name': company_name or '',
                         'gst_no': gst_no or 0.0,
                         'date_start': date_from or False,
                         'date_end': date_to or False,
                         'box1': formatLang(self.env, abs(box1 or 0.0)),
                         'box2': formatLang(self.env, abs(box2 or 0.0)),
                         'box3': formatLang(self.env, abs(box3 or 0.0)),
                         'box4': formatLang(self.env, abs(box4 or 0.0)),
                         'box5': formatLang(self.env, abs(box5 or 0.0)),
                         'box6': formatLang(self.env, abs(box6 or 0.0)),
                         'box7': formatLang(self.env, abs(box7 or 0.0)),
                         'box8': formatLang(self.env, (box8 or 0.0)),
                         'box9': formatLang(self.env, abs(box9 or 0.0)),
                         'box10': formatLang(self.env, abs(box10 or 0.0)),
                         'box11': formatLang(self.env, abs(box11 or 0.0)),
                         'box12': formatLang(self.env, abs(box12 or 0.0)),
                         'box13': formatLang(self.env, (box13 or 0.0))})
        # return tax_list

        data = {
            'model': "gst.f5.return.wizard",
            'form': self.read()[0],
            'csr': tax_list,
            'currency_id': self.env.company.currency_id
        }
        return data