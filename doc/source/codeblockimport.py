from docutils import nodes
from sphinx.errors import SphinxError
from sphinx.directives import CodeBlock
from docutils.parsers.rst import directives

codeDict = dict()

class CodeError(SphinxError):
    category = "Code error"

def registerCodeDict (name, code):
    if name in codeDict:
        raise RuntimeError("Code with name " + codename + " has already been defined")
    codeDict[name] = code

class CodeDirective(CodeBlock):
    has_content = True
    required_arguments = 0
    optional_arguments = 0

    option_spec = dict(
        name = str,
        includecode = str,
        hidden = directives.flag
    )

    def run(self):
        global codeDict
        code = u'\n'.join(self.content)
        
        codename = self.options['name']
        
        included_code = ""
        if 'includecode' in self.options:
            for name in self.options['includecode'].split(','):
                included_code += codeDict[name] + "\n"
        
        registerCodeDict(codename, included_code + "\n\n" + code)
        
        if 'hidden' in self.options:
            return []
            
        nodeList = []
        literal = nodes.literal_block(code, code)
        literal['language'] = 'python'
        nodeList.append(literal)
            
        return nodeList

def setup(app):
    app.add_config_value('code', False, False)
    app.add_directive('code', CodeDirective)
