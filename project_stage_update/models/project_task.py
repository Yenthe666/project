from odoo import api, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.constrains("stage_id")
    def _update_project_state(self):
        """
            Update the project stage if all tasks are moved outside of a specific stage.
            For example: Project "A" has the project stages "Backlog", "In progress", "Done"
            The project has the same task stages "Backlog", "In progress", "Done".
            When we would now configure on the project task stage that when all tasks are moved out of the stage
            "Backlog" that it should move the project it's stage to "In progress" this code would check it.
            So, when the last task moves out of a stage and this stage has a project stage configured we will also
            automatically update the project it's stage.
            This makes the project stage management easier to automate.
        """
        for task in self:
            stage_id = task.stage_id
            if stage_id.project_stage_id:
                project = task.project_id
                if not any(task.stage_id != stage_id for task in project.task_ids):
                    project.sudo().stage_id = stage_id.project_stage_id.id
