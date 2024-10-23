from odoo import fields,models


class ResPartner(models.Model):
    _inherit = "res.partner"

    ninjarmm_company_id = fields.Integer("NinjaRMM Company ID")

