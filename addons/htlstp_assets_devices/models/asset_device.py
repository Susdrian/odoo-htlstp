from odoo import fields,models

class AssetAsset(models.Model):
    _inherit = "asset.asset"

    type = fields.Selection(selection_add=[('device', 'Device')], ondelete={'device': 'set default'})

    configuration = fields.Text("Configuration", copy=False)


    device_type_id = fields.Many2one("asset.device.type", string="Device Type", copy=False)
    application_version_ids = fields.Many2many("asset.application.version", string="Application")


