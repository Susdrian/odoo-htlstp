from odoo import fields,models

class AssetDeviceType(models.Model):
    _name = "asset.device.type"
    _description = "Asset Device Type"
    _order = "sequence, name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "Device Types must be unique"),
    ]

    name = fields.Char("Name", required=True)
    sequence = fields.Integer("Sequence", default=10)