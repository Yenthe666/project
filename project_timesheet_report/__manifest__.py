# -*- coding: utf-8 -*-

{
    'name': "Project Timesheet Report",
    'version': '14.0.1.0.0',
    'summary': """Export worked hours from employees based on project(s)""",
    'description': """
        This Module allows you to get your Project's Timesheet based on Given Date range.
    """,
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'category': 'Project',
    'depends': ['hr_timesheet'],
    'data': [
            'security/ir.model.access.csv',
            'report/project_timesheet_report_template.xml',
            'report/report_view.xml',
            'wizards/project_timesheet_report_wizard_view.xml',
             ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
