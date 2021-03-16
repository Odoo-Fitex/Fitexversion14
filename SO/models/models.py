 # -*- coding: utf-8 -*-
from odoo import models, fields, api


class action_SO(models.Model):
    _inherit = 'sale.order'  

    dummy_field = fields.Char(string="DUmmy")
