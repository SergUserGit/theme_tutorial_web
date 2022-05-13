{
    'name': 'Sergiy Podriezienko theme',
    'description': 'Sergiy Podriezienko theme',
    'version': '1.3',
    'author': 'Sergiy Podriezienko',
    'category': 'Theme/Creative',
    'assets': {'web.assets_frontend': ['theme_tutorial/static/scss/style.scss'],
               'web._assets_primary_variables': ['theme_tutorial/static/scss/primary_variables.scss'],
               'web._assets_frontend_helpers': ['theme_tutorial/static/src/scss/bootstrap_overridden.scss'],
               'website.assets_editor': ['theme_tutorial/static/src/js/tutorial_editor.js']},
    'depends': ['website'],
    'data': ['views/layout.xml',
             'views/pages.xml',
             'views/snippets.xml',
             'views/options.xml'],
    'installable': True,
    'auto_install': False,
}
