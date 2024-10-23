from odoo import _, models
from odoo.tools import format_date


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    """ Changed to Calculate Subscription Period from Start to End of Period Month and Prepaid Subscriptions based on prepayment setting"""
    def _prepare_invoice_line(self, **optional_values):
        self.ensure_one()
        res = super()._prepare_invoice_line(**optional_values)
        if self.display_type:
            return res
        elif self.temporal_type == 'subscription' or self.order_id.subscription_management == 'upsell':
            reccurence_id = self.order_id.recurrence_id
            description = "%s - %s" % (self.name, self.order_id.recurrence_id.duration_display)
            lang_code = self.order_id.partner_id.lang
            period = self.order_id.get_period_data()
            new_period_start = period['subscription_start_date']
            next_invoice_date = period['next_invoice_date']
            period_start = period['start']
            period_end = period['end']

            format_start = format_date(self.env, period_start, lang_code=lang_code)
            format_end = format_date(self.env, period_end, lang_code=lang_code)

            #Adds Date to SO Line
            #description += _("\n%s to %s", format_start, format_end)

            qty_to_invoice = self._get_subscription_qty_to_invoice(
                last_invoice_date=new_period_start,
                next_invoice_date=next_invoice_date
            )
            subscription_end_date = next_invoice_date
            res['quantity'] = qty_to_invoice.get(self.id, 0.0)

            res.update({
                'name': description,
                'subscription_start_date': new_period_start,
                'subscription_end_date': subscription_end_date,
                'subscription_id': self.order_id.id,
            })

        elif self.order_id.is_subscription:
            # This is needed in case we only need to invoice this line
            res.update({
                'subscription_id': self.order_id.id,
            })
        return res
