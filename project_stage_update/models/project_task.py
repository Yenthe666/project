from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    project_stage_id = fields.Many2one(
        'project.project.stage',
        string='Project stage'
    )

    def write(self, vals):
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
        if self.project_stage_id:
            open_tasks = self.sudo().search_count([
                ('stage_id.is_finished', '=', False),
                ('project_id', '=', self.project_id.id),
                ('project_stage_id', '=', self.project_stage_id.id),
            ])
            if open_tasks <= 0:
                self.project_id.stage_id = self.project_stage_id.id

        return super(ProjectTask, self).write(vals)
