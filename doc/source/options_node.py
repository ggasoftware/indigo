from docutils import nodes
from sphinx.errors import SphinxError
import sphinx.ext.doctest
from sphinx.directives import CodeBlock
from sphinx.util import parselinenos
from sphinx.util.nodes import set_source_info
from docutils.nodes import fully_normalize_name as normalize_name
from docutils.transforms import Transform
from docutils.transforms.parts import ContentsFilter
from docutils.parsers.rst import Directive, directives

class OptionsNodesError(SphinxError):
    category = "OptionsNode error"

class optioninfo(nodes.section, nodes.Element):
    pass

class optionslist(nodes.General, nodes.Element):
    pass

def visit_optioninfo_node(self, node):
    self.visit_section(node)

def depart_optioninfo_node(self, node):
    self.depart_section(node)

class OptionsDirective(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 4

    option_spec = dict(
        name = str,
        type = str,
        default = str,
        short = str
    )

    def make_field(self, name, content):
        fieldname = nodes.field_name('', name)
        fieldbody = nodes.field_body('', nodes.paragraph('', '', content))
        return nodes.field('', fieldname, fieldbody)

    def run(self):
        name = self.options.get('name')

        env = self.state.document.settings.env

        targetid = "indigo-option-%d" % env.new_serialno('indigo-option')
        targetnode = nodes.target('', '', ids=[targetid])

        section_node = optioninfo()
        section_node['names'].append(normalize_name(name))
        section_node['ids'].append(normalize_name(name))
        titlenode = nodes.title('', name + ' = ' + self.options.get('default'))
        section_node += titlenode

        new_list = nodes.field_list()
        new_list += self.make_field('type', nodes.Text(self.options.get('type')))
        new_list += self.make_field('default', nodes.Text(self.options.get('default')))
        new_list += self.make_field('description', nodes.Text(self.options.get('short')))

        section_node += new_list

        text = '\n'.join(self.content)
        if text:
            self.state.nested_parse(self.content, self.content_offset, section_node)

        if not hasattr(env, 'indigo_options'):
            env.indigo_options = []

        env.indigo_options.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'name': name,
            'type': self.options.get('type'),
            'default': self.options.get('default'),
            'short':self.options.get('short'),
            'target': targetnode
        })

        return [ targetnode, section_node ]

def purge_indigo_options(app, env, docname):
    if not hasattr(env, 'indigo_options'):
        return
    env.indigo_options = [opt for opt in env.indigo_options
                          if opt['docname'] != docname]

def createRowEntry (node):
    entry = nodes.entry()
    paragraph = nodes.paragraph()
    paragraph += node
    entry += paragraph
    return entry

def createRowEntryText (text):
    return createRowEntry(nodes.Text(text))

def process_indigo_option_nodes(app, doctree, fromdocname):
    env = app.builder.env

    for node in doctree.traverse(optionslist):
        content = []

        tbl = nodes.table()
        tgroup = nodes.tgroup(cols=4)
        tbl += tgroup

        tgroup += nodes.colspec(colwidth=35)
        tgroup += nodes.colspec(colwidth=9)
        tgroup += nodes.colspec(colwidth=9)
        tgroup += nodes.colspec(colwidth=73)

        thead = nodes.thead()
        tgroup += thead
        row = nodes.row()
        thead += row
        row += createRowEntryText('Name')
        row += createRowEntryText('Type')
        row += createRowEntryText('Default')
        row += createRowEntryText('Short description')

        tbody = nodes.tbody()
        tgroup += tbody

        content.append(tbl)

        sorted_options = sorted(env.indigo_options, key=lambda o:o['name'])

        for opt_info in sorted_options:
            row = nodes.row()
            tbody += row

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.Text(opt_info['name'], opt_info['name'])
            newnode['refdocname'] = opt_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, opt_info['docname'])
            newnode['refuri'] += '#' + normalize_name(opt_info['name'])
            newnode.append(innernode)

            row += createRowEntry(newnode)
            row += createRowEntryText(opt_info['type'])
            row += createRowEntryText(opt_info['default'])
            row += createRowEntryText(opt_info['short'])

        node.replace_self(content)

class OptionsTableDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0

    option_spec = dict()

    def run(self):
        optlist = optionslist('')
        env = self.state.document.settings.env
        optlist['docname'] = env.docname
        return [ optlist ]

def indigo_option_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Link to an Indigo option

    Returns 2 part tuple containing list of nodes to insert into the
    document and a list of system messages.  Both are allowed to be
    empty.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called us.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    """
    env = inliner.document.settings.env
    app = env.app

    opts = [opt for opt in env.indigo_options if opt['name'] == text]
    if len(opts) == 0:
        raise ValueError("Cannot find option " + slug)

    opt_info = opts[0]

    newnode = nodes.reference('', '')
    innernode = nodes.Text(opt_info['name'], opt_info['name'])
    newnode['refdocname'] = opt_info['docname']
    newnode['refuri'] = app.builder.get_relative_uri(
        env.docname, opt_info['docname'])
    newnode['refuri'] += '#' + normalize_name(opt_info['name'])
    newnode.append(innernode)

    return [newnode], []

def setup(app):
    app.add_directive('indigo_option', OptionsDirective)
    app.add_directive('indigo_options_table', OptionsTableDirective)

    app.add_node(optionslist)
    app.add_node(optioninfo,
                 html=(visit_optioninfo_node, depart_optioninfo_node),
                 latex=(visit_optioninfo_node, depart_optioninfo_node),
                 text=(visit_optioninfo_node, depart_optioninfo_node))

    app.connect('doctree-resolved', process_indigo_option_nodes)
    app.connect('env-purge-doc', purge_indigo_options)

    app.add_role('optref', indigo_option_role)