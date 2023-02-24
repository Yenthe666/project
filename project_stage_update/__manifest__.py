{
    'name': 'Project stage update',
    'version': '16.0.1.0.0',
    'category': 'Services/Project',
    'summary': """Automatically updates Project stage when all task are in same stage.""",
    'description': """Automatically updates Project stage when all task are in same stage.""",
    'author': "Mainframe Monkey",
    'website': "https://www.mainframemonkey.com",
    'depends': ['project'],
    'data': [
        'views/project_task_type_views.xml',
        'views/project_task_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
