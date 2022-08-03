# -- coding: utf-8 --
{
    'name': 'Project Stage Warning',
    'summary': 'Show warning when project stage is skipped',
    'description': 'Show warning when project stage is skipped',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '14.0.1.0.0',
    'website': 'https://www.mainframemonkey.com',
    'author': 'Mainframe Monkey',
    'depends': ['project'],
    'data': [
        'views/project_task_type_views.xml',
    ],
    'license': 'LGPL-3',
}
