# -- coding: utf-8 --
{
    'name': 'Project Task Stage Email Reminders',
    'summary': 'Project Task Stage Email Reminders',
    'description': 'Send reminders when project tasks are in a stage for a number of days',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '14.0.1.0.0',
    'website': 'https://www.mainframemonkey.com',
    'author': 'Mainframe Monkey',
    'depends': ['project', 'mail'],
    'data': [
        'security/ir.model.access.csv',

        'views/project_project_views.xml',
        'views/project_task_type_views.xml',
        'views/task_mail_rule_views.xml',

        'data/task_mail_rule_cron.xml',
    ],

    'installable': True,
}
