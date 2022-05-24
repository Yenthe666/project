# -- coding: utf-8 --
from odoo import models, fields, _, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    task_mail_rule_ids = fields.One2many(
        comodel_name='task.mail.rule',
        inverse_name='project_id',
        string="Task email rules",
        context={'active_test': False}
    )

    task_mail_rule_count = fields.Integer(
        string='Task email rules count',
        compute='_compute_task_mail_rule_count'
    )

    def _compute_task_mail_rule_count(self):
        self.task_mail_rule_count = len(self.task_mail_rule_ids)

    def action_view_task_mail_rules(self):
        """
        :return: Tree view with all existing rules and context to create a new rule for the current project
        """
        return {
            "name": _("Task reminder rules"),
            "type": "ir.actions.act_window",
            "res_model": "task.mail.rule",
            "domain": [('id', 'in', self.task_mail_rule_ids.ids)],
            "view_type": "list",
            "view_mode": "list,form",
            "target": "current",
            "context": {
                'default_project_id': self.id,
                'active_test': False
            }
        }
