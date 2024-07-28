def setup(app):
    app.connect('html-page-context', print_context_variables, priority=1000)


def print_context_variables(app, pagename, templatename, context, doctree):
    print('Context variables:')
    for k in sorted(context.keys()):
        print(f'{k}: {context[k]}')
    breakpoint()
