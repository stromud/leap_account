from odoo import models


class Property(models.Model):
    _inherit = "leap.property"


    
    def sold_action(self):

        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        self.env["account.move"].create({
            'partner_id':self.partner_id.id,
            'move_type':'out_invoice',
            'journal_id':journal.id,
            'invoice_line_ids':[
            (
                0,
                0,
                {
                    'name':self.name,
                    'quantity':1,
                    'price_unit':self.selling_price *1.06,
                },
            ),
            (
                0,
                0,
                {
                    'name':'administrative fees',
                    'quantity':1,
                    'price_unit': 100.0,
                }
            
            )

            ],
        })
        return super().sold_action()