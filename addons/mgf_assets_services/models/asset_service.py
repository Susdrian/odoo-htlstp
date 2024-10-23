from odoo import fields,models

class AssetAsset(models.Model):
    _inherit = "asset.asset"

    type = fields.Selection(selection_add=[('service', 'Service')], ondelete={'service': 'set default'})

    configuration = fields.Text("Configuration", copy=False)
    access_uri = fields.Char("Access URI", copy=False)

    service_type_id = fields.Many2one("asset.service.type", string="Service Type", copy=False)
    service_type_application = fields.Boolean(related="service_type_id.application")
    application_version_ids = fields.Many2many("asset.application.version", string="Application")


