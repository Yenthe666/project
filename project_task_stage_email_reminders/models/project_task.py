# -- coding: utf-8 --
from odoo import models, fields, api
from datetime import timedelta
from datetime import date


class ProjectTask(models.Model):
    _inherit = "project.task"

    def send_email_reminder(self):
        """
        Search all project tasks that are in a stage that is configured for reminders.
        Then send out the reminder if it is the correct day.
        """
        stages_with_reminder = self.env['project.task.type'].search([
            ('lead_mail_rule_ids', '!=', False)
        ])

        tasks = self.env['project.task'].search([('stage_id', 'in', stages_with_reminder.ids)])

        today = date.today()

        for task in tasks:
            for task_rule in task.stage_id.task_mail_rule_ids.filtered(lambda rule: rule.active):
                reminder_day = task_rule.send_reminder_after
                new_reminder_date = (task.date_last_stage_update + timedelta(reminder_day)).date()
                if new_reminder_date == today:
                    task_rule.email_template_id.use_default_to = True
                    task.message_post_with_template(task_rule.email_template_id.id)
