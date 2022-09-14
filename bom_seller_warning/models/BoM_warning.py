from odoo import models, fields, api


class BomWarning(models.Model):
    _inherit = "product.template"
    _description = "Create a warning to tell the customer if the MTO and Manufacture routes are selected with no BOM " \
                   "or if the MTO and buy routes are selected with no seller"
    mto_buy_check = fields.Boolean(string="mto_buy_check", compute="_check_mto_buy")
    warning_notification_mto = fields.Boolean(default=True)
    warning_notification_mrp = fields.Boolean(default=True)

    @api.constrains('route_ids', 'website_published')
    @api.depends('route_ids', 'website_published')
    def _check_mto_buy(self):
        for rec in self:
            # notification that is invisible if it is True, and it will be visible if False
            rec.warning_notification_mto = True
            rec.warning_notification_mrp = True
            # If there is an MTO and a Buy routes but no seller show a warning and don't let it be published
            if rec.env.ref('stock.route_warehouse0_mto').id in rec.route_ids.ids and \
                    rec.env.ref('purchase_stock.route_warehouse0_buy').id in rec.route_ids.ids:
                if rec.seller_ids.ids:
                    rec.warning_notification_mto = True
                else:
                    rec.warning_notification_mto = False
                    if rec.is_published:
                        if rec.website_published:
                            rec.website_published = False
                            rec.is_published = False
                    else:
                        pass
            # If there is an MTO and a Manufacture routes but no Bill of materials show a warning and don't let it be
            # published
            if rec.env.ref('stock.route_warehouse0_mto').id in rec.route_ids.ids and \
                    rec.env.ref('mrp.route_warehouse0_manufacture').id in rec.route_ids.ids:
                if rec.bom_count == 0:
                    rec.warning_notification_mrp = False
                    if rec.is_published:
                        if rec.website_published:
                            rec.website_published = False
                            rec.is_published = False
                else:
                    rec.warning_notification_mrp = True
            rec.mto_buy_check = True
