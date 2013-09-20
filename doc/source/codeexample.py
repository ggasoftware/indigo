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

    option_spec = dict(
        language = str,
    )

    def translateCode(self, code, outputLanguage):
        if outputLanguage == 'java':
            return code.replace('using', 'import')
        elif outputLanguage == 'csharp':
            return code
        elif outputLanguage == 'python':
            return code.replace('IndigoObject', '').replace('Indigo ', ' ').replace('Indigo ', ' ')
        return code

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

        specified_language = self.options.get('language')
        light = self.options.get('light', False)

        nodeList = []
        languageDict = {'python': 'Python', 'java': 'Java', 'csharp': 'C#'}
        for language in languageDict:
            if specified_language is not None and specified_language != language:
                continue
            if not light:
                language_title = nodes.Text(languageDict[language] + ':', language)
                nodeList.append(language_title)

            literal = nodes.literal_block(self.translateCode(code, language), self.translateCode(code, language))
            literal['language'] = language
            if hl_lines is not None:
                literal['highlight_args'] = {'hl_lines': hl_lines}
            set_source_info(self, literal)
            nodeList.append(literal)
        return nodeList

def setup(app):
    app.add_config_value('codeexample', False, False)
    app.add_directive('codeexample', CodeExampleDirective)
