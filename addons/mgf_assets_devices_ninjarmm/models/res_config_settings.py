from odoo import fields,models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    ninjarmm_keyid = fields.Char("NinjaRMM Access Key ID")
    ninjarmm_secret = fields.Char("NinjaRMM Secret Access Key")