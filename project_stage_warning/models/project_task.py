# -- coding: utf-8 --
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _inherit = "project.task"

    def write(self, values):
        if values.get('stage_id'):
            new_stage = self.env['project.task.type'].browse(values.get('stage_id'))
            end_sequence = new_stage.sequence
            for task in self:
                start_sequence = task.stage_id.sequence
                skipped_stage = self.env['project.task.type'].search([
                    ('sequence', '<', end_sequence),
                    ('sequence', '>', start_sequence),
                    ('project_ids', '=', task.project_id.id),
                    ('show_warning_when_stage_skipped', '=', True)
                ], limit=1)
                if skipped_stage:
                    raise UserError(_('You cannot skip stage %s. You must go through that stage first.') % skipped_stage.name)

        super(ProjectTask, self).write(values)
