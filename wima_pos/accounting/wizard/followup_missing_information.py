from odoo import models, _


class FollowupMissingInformation(models.TransientModel):
    _name = "account_followup.missing.information.wizard"
    _description = "Followup missing information wizard"

    def view_partners_action(self):
        """ Returns a list view containing all the partners with missing information with the option to edit in place.
        """
        view_id = self.env.ref('wima_pos.missing_information_view_tree').id

        return {
            'name': _('Missing information'),
            'res_model': 'res.partner',
            'view_mode': 'tree',
            'views': [(view_id, 'tree')],
            'domain': [('id', 'in', self.env.context.get('default_partner_ids', []))],
            'type': 'ir.actions.act_window',
        }
