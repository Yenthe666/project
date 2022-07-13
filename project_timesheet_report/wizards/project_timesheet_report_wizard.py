
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectTimesheetReportWizard(models.TransientModel):
    _name = 'project.timesheet.report.wizard'
    _description = "Project Timesheet Report Wizard"

    projects_ids = fields.Many2many(
        'project.project',
        string="Projects",
        domain="[('allow_timesheets','=', True)]",
        required=True,
        default=lambda self: self.env.context.get('active_ids', None),
    )

    from_date = fields.Date(
        string="Start Date",
        required=True,
        default=lambda self: fields.Date.add(fields.Date.today(), day=1)
    )

    to_date = fields.Date(
        string="End Date",
        required=True,
        default=lambda self: fields.Date.add(fields.Date.today(), months=+1, day=1, days=-1)
    )

    def action_print_project_timesheet_report(self):
        data = {
            'ids': self.ids,
            'model': 'account.analytic.line',
            'form': self.read(['from_date', 'to_date', 'projects_ids'])[0]
        }
        if data.get('form').get('to_date') < data.get('form').get('from_date'):
            raise ValidationError(_('The start date should fall before the end date.'))
        return self.env.ref('project_timesheet_report.project_timesheet_report').report_action([], data=data)
