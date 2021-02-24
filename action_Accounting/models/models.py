# -*- coding: utf-8 -*-
from odoo import models, fields, api


from odoo import models, fields, api


class action_accounting(models.Model):
    _inherit = "account.move.line"
    
    today = fields.Date(string="Today", default=fields.Date.context_today)
    general_balance = fields.Monetary(string='Balance', store=True,
                                      compute='compute_balance')

    @api.depends('debit', 'credit')
    def compute_balance(self):   
           for line in self:
            if line.general_balance:
                line.general_balance = line.debit - line.credit
            else:
                line.general_balance = 0
        
#     def open_action(self):
#         """return action based on type for related journals"""
#         action_name = self._context.get('action_name')

#         # Find action based on journal.
#         if not action_name:
# #             if self.account_id.id == 819:
#             action_name = 'action_treasury_egp'
#         if '.' not in action_name:
#             action_name = 'account.%s' % action_name

#         action = self.env.ref(action_name).read()[0]
#         context = self._context.copy()
#         if 'context' in action and type(action['context']) == str:
#             context.update(ast.literal_eval(action['context']))
#         else:
#             context.update(action.get('context', {}))
#         action['context'] = context
#         action['context'].update({
#             'default_journal_id': self.id,
#             'search_default_journal_id': self.id,
#         })

#         domain_type_field = action['res_model'] == 'account.move.line' and 'move_id.type' or 'type' # The model can be either account.move or account.move.line

#         if self.type == 'sale':
#             action['domain'] = [(domain_type_field, 'in', ('out_invoice', 'out_refund', 'out_receipt'))]
#         elif self.type == 'purchase':
#             action['domain'] = [(domain_type_field, 'in', ('in_invoice', 'in_refund', 'in_receipt'))]

#         return action
