# -- coding: utf-8 --
from odoo import models, fields, api, _
from odoo.exceptions import  ValidationError


class TaskMailRule(models.Model):
    _name = "task.mail.rule"
    _description = "Email Reminders for project tasks"
    _order = "create_date asc"

    name = fields.Char(
        string='Name',
        required=True
    )

    stage_id = fields.Many2one(
        comodel_name='project.task.type',
        string="Stage",
        domain="[('project_ids', '=', project_id)]",
        required=True
    )

    email_template_id = fields.Many2one(
        comodel_name='mail.template',
        string="Email Template",
        domain=[('model', '=', 'project.task')],
        required=True
    )

    send_reminder_after = fields.Integer(
        string="Send Reminder After",
        required=True
    )

    project_id = fields.Many2one(
        comodel_name='project.project',
        string="Project",
        required=True,
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    @api.onchange('email_template_id')
    def _onchange_email_template_id(self):
        for rule in self:
            if not rule.name:
                rule.name = rule.email_template_id.name

    @api.constrains('send_reminder_after')
    def _constrains_send_reminder_after(self):
        for rule in self:
            if rule.send_reminder_after < 1:
                raise ValidationError(_('The reminder must be sent at least after one day.'))
