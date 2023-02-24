from odoo import api, fields, models, _


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    project_stage_id = fields.Many2one(
        "project.project.stage",
        string="Move project stage to",
        help="The project stage that you configure here will define to which project stage the project will move "
             "when the last task is moved out of this stage."
    )

    is_finished = fields.Boolean(
        string='Final stage of a task',
        help='If this boolean is checked on we will exclude tasks in this stage as those tasks are finished.'
    )
