from odoo import fields,models

class AssetServiceType(models.Model):
    _name = "asset.device.type"
    _description = "Asset Device Type"
    _order = "sequence, name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Service Types must be unique"),
    ]

    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)