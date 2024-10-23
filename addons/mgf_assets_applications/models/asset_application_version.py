from odoo import fields,models

class AssetApplicationVersion(models.Model):
    _name = "asset.application.version"
    _description = "Asset Application Version"

    version = fields.Char("Version", required=True)

    application_id = fields.Many2one("asset.application", string="Application", required=True)
    publisher_id = fields.Char(related="application_id.publisher_id.name", string="Publisher")
