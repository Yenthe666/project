from odoo import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.constrains("stage_id")
    def _update_project_state(self):
        """
            Update stage on project if all task are moved to same stage
        """
        for task in self:
            stage_id = task.stage_id
            if stage_id.mfm_project_stage_id:
                project = task.project_id
                if not any(task.stage_id != stage_id for task in project.task_ids):
                    project.stage_id = stage_id.mfm_project_stage_id.id
