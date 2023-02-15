from odoo import api, fields, models, _


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    mfm_project_stage_id = fields.Many2one(
        "project.project.stage",
        string="Project stage",
        help="Move project to selected stage when all task are moved to this stage."
    )
