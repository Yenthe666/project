# -- coding: utf-8 --
from odoo import models, fields, _, api
from odoo.exceptions import UserError

from odoo.exceptions import  ValidationError


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    task_mail_rule_ids = fields.One2many(
        comodel_name='task.mail.rule',
        inverse_name='stage_id',
        string="Mail rules",
        context={'active_test': False}
    )

    default_project_id = fields.Integer(
        string='Default project',
        compute='_compute_default_project_id'
    )

    @api.onchange('project_ids')
    def _compute_default_project_id(self):
        """
        Set default project id for rules when the stage has only one project configured
        """
        for record in self:
            if len(record.project_ids) == 1:
                record.default_project_id = record.project_ids.id
            else:
                record.default_project_id = 0

    def unlink(self):
        """
        Raise an error when there are still rules configured for the stage that will be deleted.
        """
        for record in self:
            if record.task_mail_rule_ids:
                raise UserError(_('There are e-mail reminder rules configured for this stage. Please remove them or change them so they belong to another stage first.'))
        super(ProjectTaskType, self).unlink()

    @api.constrains('project_ids')
    def _constrains_project_ids(self):
        """
        Raise an error when there are still rules configured for the project that will be removed from the stage.
        """
        for stage in self:
            for rule in stage.task_mail_rule_ids:
                if rule.project_id not in stage.project_ids:
                    raise ValidationError(_('The rule %s is still linked to project %s, while the project is no longer configured for this stage.') % (rule.name, rule.project_id.name))
