from odoo import api, models, fields


class SaleOrderRecurrence(models.Model):
    _inherit = 'sale.temporal.recurrence'

    draft = fields.Boolean('Draft Invoice', help='Enable if Invoice should only be created as Draft and not be posted', default=False)
    prepayment  = fields.Boolean('Prepay Invoice', help='Enable if Invoice is Prepaid for the Next Payment period', default=False)

    @api.depends('duration', 'unit')
    def _compute_duration_display(self):
        for record in self:
            record.duration_display = "%s %s" % (
                record.duration, record._get_unit_label(record.duration).capitalize()
            )