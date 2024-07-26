"""Extends sphinx-tippy with the ability to add tooltips to fontawesome icons."""
# from docutils import nodes
from sphinx.application import Sphinx
from sphinx.roles import AnyXRefRole, XRefRole
from sphinx.util.docutils import ReferenceRole, SphinxRole


class FATooltipRefRole(AnyXRefRole):
    """Behaves the same as XRefRole, but adds the FontAwesome classes 'fa-solid',
    'fa-circle-info'"""

    def run(self):
        self.refdomain, self.reftype = '', self.name
        self.classes = ['xref', self.reftype]
        self.classes.extend(['fa', 'fa-solid', 'fa-circle-info'])
        return self.create_xref_node()



def setup(app: Sphinx):
    app.add_role('fa-ref', FATooltipRefRole())
    # from docutils.parsers.rst import roles
    # roles.register_local_role('fa-ref', FATooltipRefRole())

