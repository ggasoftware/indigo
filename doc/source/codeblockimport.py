from docutils import nodes
from sphinx.errors import SphinxError
from sphinx.directives import CodeBlock

codeDict = dict()

class CodeError(SphinxError):
    category = "Code error"

class CodeDirective(CodeBlock):
    has_content = True
    required_arguments = 0
    optional_arguments = 0

    option_spec = dict(
        name = str
    )

    def run(self):
        global codeDict
        code = u'\n'.join(self.content)
        codeDict[self.options['name']] = code
        nodeList = []
        literal = nodes.literal_block(code, code)
        literal['language'] = 'python'
        nodeList.append(literal)

        return nodeList

def setup(app):
    app.add_config_value('code', False, False)
    app.add_directive('code', CodeDirective)
