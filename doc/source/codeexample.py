from docutils import nodes
from sphinx.errors import SphinxError
import  sphinx.ext.doctest
from sphinx.directives import CodeBlock
from sphinx.util import parselinenos
from sphinx.util.nodes import set_source_info

class CodeExampleError(SphinxError):
    category = "CodeExample error"

class CodeExampleDirective(CodeBlock):
    has_content = True
    required_arguments = 0
    optional_arguments = 2


    def translateCode(self, javaCode, outputLanguage):
        #if outputLanguage == 'java':
        #    return javaCode
        #elif outputLanguage == 'csharp':
        #    #return javaCode.replace('import', 'using')
        #elif outputLanguage == 'python':
        return javaCode

    def run(self):
        code = u'\n'.join(self.content)

        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = [x+1 for x in parselinenos(linespec, nlines)]
            except ValueError, err:
                document = self.state.document
                return [document.reporter.warning(str(err), line=self.lineno)]
        else:
            hl_lines = None

        nodeList = []
        line = nodes.transition()
        nodeList.append(line)
        languageDict = {'python': 'Python', 'java': 'Java', 'csharp': 'C#'}
        for language in languageDict:
            language_title = nodes.Text(languageDict[language] + ':', language)
            nodeList.append(language_title)
            literal = nodes.literal_block(self.translateCode(code, language), self.translateCode(code, language))
            literal['language'] = language
            literal['linenos'] = 'linenos' in self.options
            if hl_lines is not None:
                literal['highlight_args'] = {'hl_lines': hl_lines}
            set_source_info(self, literal)
            nodeList.append(literal)
        line = nodes.transition()
        nodeList.append(line)
        #TODO: execute python code
        return nodeList

def setup(app):
    app.add_config_value('codeexample', False, False)
    app.add_directive('codeexample', CodeExampleDirective)
