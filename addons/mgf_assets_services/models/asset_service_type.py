from odoo import fields,models

class AssetServiceType(models.Model):
    _name = "asset.service.type"
    _description = "Asset Service Type"
    _order = "sequence, name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Service Types must be unique"),
    ]

    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)
    application = fields.Boolean("Application", help="Check if the Service is realted to an specific Application like NextCloud or Moodle")