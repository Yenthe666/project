# -- coding: utf-8 --
from odoo import models, fields, _, api


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    show_warning_when_stage_skipped = fields.Boolean(
        string='Show warning when stage is skipped'
    )
