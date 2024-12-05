from odoo import fields,models

class AssetAsset(models.Model):
    _name = "asset.asset"
    _description = "Asset"


    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    asset_type = fields.Selection([('general', 'General')], required=True, default='general')

    partner_id = fields.Many2one("res.partner", string="Partner", copy=False, domain = "[('is_company', '=', True)]")
    owner_id = fields.Many2one("res.partner", string="Asset Owner", copy=False, domain="[('parent_id', '=', partner_id)]", required=True)