
from odoo import api, fields, models


class ProjectTimesheetReportPDF(models.AbstractModel):
    _name = 'report.project_timesheet_report.timesheet_report_template'
    _description = "Project Timesheet Report Template"

    def _get_timesheet_datas(self, data):
        from_date = fields.Datetime.to_datetime(data.get('from_date'))
        to_date = fields.Datetime.to_datetime(data.get('to_date'))
        projects_ids = data.get('projects_ids')
        return self.env['account.analytic.line'].search([
                                                        ('project_id', 'in', projects_ids),
                                                        ('date', '>=', from_date),
                                                        ('date', '<=', to_date)])

    @api.model
    def _get_report_values(self, docids, data):
        report_tmpl = self.env['ir.actions.report']._get_report_from_name('project_timesheet_report.timesheet_report_template')
        docs = self._get_timesheet_datas(data.get('form'))
        return {'doc_ids': docids,
                'doc_model': report_tmpl.model,
                'docs': docs,
                'data': data,
                }
