from odoo import fields,models


class ResPartner(models.Model):
    _inherit = "res.partner"

    asset_count = fields.Integer("Assets", compute='_compute_asset_count')
    owner_count = fields.Integer("Owner", compute='_compute_owner_count')


    def _compute_asset_count(self):
        for asset in self:
            asset.asset_count = self.env['asset.asset'].search_count([('partner_id', '=', self.id)])


    def _compute_owner_count(self):
        for owner in self:
            owner.owner_count = self.env['asset.asset'].search_count([('owner_id', '=', self.id)])


    def action_view_partner_assets(self):
        action = self.env['ir.actions.act_window']._for_xml_id('mgf_assets.asset_asset_all_action')
        action["domain"] = [("partner_id", "=", self.id)]
        return action

    def action_view_owner_assets(self):
        action = self.env['ir.actions.act_window']._for_xml_id('mgf_assets.asset_asset_all_action')
        action["domain"] = [("owner_id", "=", self.id)]
        return action