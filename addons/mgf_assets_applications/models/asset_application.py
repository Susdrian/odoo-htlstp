from odoo import fields, models


class AssetApplication(models.Model):
    _name = "asset.application"
    _description = "Asset Application"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Service Types must be unique"),
    ]

    name = fields.Char("Name", required=True)

    publisher_id = fields.Many2one("res.partner", string="Publisher", copy=False)

    version_ids = fields.One2many("asset.application.version", "application_id", string="Versions")