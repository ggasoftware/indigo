from sphinx.errors import SphinxError
from docutils.parsers.rst import Directive
from sphinx.directives import CodeBlock

class CodeExampleError(SphinxError):
    category = "CodeExample error"

class CodeExampleDirective(Directive):
    has_content = True
    required_arguments = 0

    def run(self):
        #TODO: Continue
        pass

def processCodeExampleText():
    pass

def setup(app):
    app.add_config_value('codeexample', False, False)
    app.add_directive('codeexample', CodeExampleDirective)
    app.connect('doctree-read', processCodeExampleText)
