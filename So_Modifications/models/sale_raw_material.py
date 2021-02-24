# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    # is_dying = fields.Boolean(string="Is a Dying", default=False)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    raw_material_ids = fields.One2many('sale.raw.material', 'sale_order_id')
    type = fields.Selection([('lana', 'لنا'), ('gher', 'للغير')], required=True)
    is_dying_company = fields.Boolean(rdefault=False, compute='compute_is_dying')

    def create_po(self):
        arr = []
        if self.raw_material_ids:
            for raw in self.raw_material_ids:
                dic = {'product_id': raw.product_id.id, 'product_qty': raw.value, 'product_uom': raw.uom_id.id}
                arr.append(dic)
        if arr:
            print("Yes ARR")
            return {
                'name': _('PO'),
                'res_model': 'purchase.order',
                'view_mode': 'form',
                'view_id': self.env.ref('purchase.purchase_order_form').id,
                'context': {'default_order_line': arr},
                'target': 'new',
                'type': 'ir.actions.act_window',
            }
        else:
            print("NO ARR")
            return {
                'name': _('PO'),
                'res_model': 'purchase.order',
                'view_mode': 'form',
                'view_id': self.env.ref('purchase.purchase_order_form').id,
                # 'context': {'order_line': arr},
                'target': 'new',
                'type': 'ir.actions.act_window',
            }

    def create_receive(self):
        arr = []
        if self.raw_material_ids:
            for raw in self.raw_material_ids:
                dic = {'product_id': raw.product_id.id, 'product_uom_qty': raw.value, 'product_uom': raw.uom_id.id}
                arr.append(dic)
        if arr:
            print("Yes ARR INV")
            return {
                'name': _('Receive Products'),
                'res_model': 'stock.picking',
                'view_mode': 'form',
                'view_id': self.env.ref('stock.view_picking_form').id,
                'context': {'default_move_lines': arr},
                'target': 'new',
                'type': 'ir.actions.act_window',
            }
        else:
            print("NO ARR")
            return{
                'name': _('Receive Products'),
                'res_model': 'stock.picking',
                'view_mode': 'form',
                'view_id': self.env.ref('stock.view_picking_form').id,
                # 'context': {'default_move_ids_without_package': arr},
                'target': 'new',
                'type': 'ir.actions.act_window',
            }

    def create_bom(self):
        return {
            'name': _('BOM'),
            'res_model': 'mrp.bom',
            'view_mode': 'form',
            'view_id': self.env.ref('mrp.mrp_bom_form_view').id,
            # 'target': 'new',
            'type': 'ir.actions.act_window',
        }

    @api.depends('partner_id')
    def compute_is_dying(self):
        print("IS Dying")
        self.ensure_one()
        dying_group_id = self.env.ref('So_Modifications.group_dying_company_user').id
        if dying_group_id in self.env.user.groups_id.ids:
            self.is_dying_company = True
            self.type = 'gher'
        else:
            self.is_dying_company = False


class SaleRawMaterial(models.Model):
    _name = 'sale.raw.material'

    product_id = fields.Many2one('product.product', string="Product")
    uom_id = fields.Many2one(related="product_id.uom_id", string="Unit Of Measure")
    value = fields.Float(string="Value")
    sale_order_id = fields.Many2one('sale.order')






