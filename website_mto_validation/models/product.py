from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Create a warning to tell the customer if the MTO and Manufacture routes are selected with no BOM " \
                   "or if the MTO and buy routes are selected with no seller to avoid failures on Order creation"

    warning_notification_buy = fields.Boolean(compute='_compute_mto_buy', default=False, store=True, readonly=True)
    warning_notification_mrp = fields.Boolean(compute='_compute_mto_buy', default=False, store=True, readonly=True)

    @api.constrains('route_ids', 'website_published')
    def _check_mto_buy(self):
        for p in self:
            if (p.warning_notification_buy or p.warning_notification_mrp) and p.website_published:
                raise ValidationError(_('Published MTO products need to have a BoM or a Supplier'))

    @api.depends('route_ids', 'website_published')
    def _compute_mto_buy(self):
        for rec in self:
            # for Buy route
            if rec.env.ref('stock.route_warehouse0_mto').id in rec.route_ids.ids and \
                    rec.env.ref('purchase_stock.route_warehouse0_buy').id in rec.route_ids.ids:
                rec.warning_notification_buy = not rec.seller_ids.ids
            # for Manufacture route
            elif rec.env.ref('stock.route_warehouse0_mto').id in rec.route_ids.ids and \
                    rec.env.ref('mrp.route_warehouse0_manufacture').id in rec.route_ids.ids:
                rec.warning_notification_mrp = rec.bom_count == 0
            else:
                rec.warning_notification_buy = False
                rec.warning_notification_mrp = False
