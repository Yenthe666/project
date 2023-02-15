from odoo import api, fields, models, _


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    project_stage_id = fields.Many2one(
        "project.project.stage",
        string="Move project stage to",
        help="The project stage that you configure here will define to which project stage the project will move "
             "when the last task is moved out of this stage."
    )
