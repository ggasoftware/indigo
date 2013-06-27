from collections import defaultdict
import hashlib
import os
import traceback

import re
import sys
from docutils import nodes
from docutils.parsers.rst import directives
from indigo import Indigo, IndigoException
from indigo_renderer import IndigoRenderer
from indigo_inchi import IndigoInchi
from sphinx.errors import SphinxError
from sphinx.util import relative_uri
from sphinx import addnodes

DEFAULT_FORMATS = dict(html='svg', latex='pdf', text=None)

indigo = None
indigoRenderer = None
indigoInchi = None

absolutePaths = {}
outputData = defaultdict(str)

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.data = ''

    def write(self, message):
        #self.terminal.write(message)
        global outputData
        outputData[self] += message

    def flush(self):
        self.terminal.flush()

    def read(self):
        return self.data

def resetIndigo():
    global indigo, indigoRenderer, indigoInchi

    indigo = Indigo()
    indigoRenderer = IndigoRenderer(indigo)
    indigoInchi = IndigoInchi(indigo)

    # Set default options
    indigo.setOption('render-bond-length', '30')
    indigo.setOption('render-relative-thickness', '1.3')
    indigo.setOption('render-coloring', False)
    indigo.setOption('render-comment-font-size', 14.0)
    indigo.setOption('render-comment-offset', '10')

def get_hashid(text, options):
    hashkey = text.encode('utf-8') + str(options)
    hashid = hashlib.sha1(hashkey).hexdigest()
    return hashid

class IndigoRendererError(SphinxError):
    category = 'IndigoRenderer error'

class IndigoRendererDirective(directives.images.Figure):
    has_content = True
    required_arguments = 0

    own_option_spec = dict(
        indigooptions = str,
        indigoobjecttype = str,
        indigoloadertype = str,
        includecode = str,
        imagename = str,
        downloads = str,
        noimage = directives.flag
    )

    option_spec = directives.images.Image.option_spec.copy()
    option_spec.update(own_option_spec)

    def run(self):
        self.arguments = ['']
        indigorenderer_options = dict([(k,v) for k,v in self.options.items()
                                      if k in self.own_option_spec])

        text = '\n'.join(self.content)
        (image_node,) = directives.images.Image.run(self)
        if isinstance(image_node, nodes.system_message):
            return [image_node, ]
        image_node.indigorenderer = dict(text=text, options=indigorenderer_options)
        blocks = []
        if indigorenderer_options['indigoobjecttype'] == 'code':
            literal = nodes.literal_block(text, text, line=self.lineno)
            #literal['linenos'] = True
            literal['language'] = 'python'
            blocks = [literal]
            if 'downloads' in self.options:
                blocks.append(nodes.Text('Input:     '))
                for file in self.options['downloads'].split(','):
                    download = addnodes.download_reference("", "")
                    download += nodes.literal(file, file)
                    download['reftarget'] = file
                    blocks.append(download)
                    blocks.append(nodes.Text('     '))
                blocks.append(nodes.line())
            
        blocks.append(image_node)
           
        return blocks

def render_indigorenderer_images(app, doctree):
    for img in doctree.traverse(nodes.image):
        if not hasattr(img, 'indigorenderer'):
            continue

        text = img.indigorenderer['text']
        options = img.indigorenderer['options']
        try:
            relative_paths, output = render_indigorenderer(app, text, options, os.path.dirname(doctree.attributes['source']), os.path.abspath(os.curdir))
            imgnodes = []
            if 'noimage' not in options:
                for relative_path in relative_paths:
                    newimg = img.copy()
                    newimg['uri'] = relative_path
                    newimg['scale'] = 1.0 / float(len(relative_paths))
                    imgnodes.append(newimg)
                    span = img.copy()
                    span['uri'] = os.path.join(os.path.dirname(app.builder.outdir), '..', 'source', '_images', 'span.png')
                    imgnodes.append(span)
            if output:
                if 'noimage' not in options:
                    newline = nodes.line()
                    imgnodes.append(newline)
                title = nodes.Text('Output:')
                imgnodes.append(title)
                literal = nodes.literal_block(output, output)
                literal['classes'] += ['output']
                imgnodes.append(literal)
            img.replace_self(imgnodes)
        except IndigoRendererError, exc:
            app.builder.warn('indigorenderer error: ' + str(exc))
            img.replace_self(nodes.literal_block(text, text))
            continue

def executeIndigoCode(text, absolute_path, relativePath, rstdir, curdir, options):
    try:
        if 'includecode' in options:
            import codeblockimport
            for name in options['includecode'].split(','):
                exec(codeblockimport.codeDict[name], globals())
                
        text = text.replace('result.png', absolute_path)

        result = re.search('result_(.*)\.png', text, re.MULTILINE)
        relativePaths = []
        while result:
            new_absolute_path = absolute_path.replace('.png', result.group(1) + '.png').replace('.svg', result.group(1) + '.svg').replace('.pdf', result.group(1) + '.pdf')
            relativePaths.append(relativePath.replace('.png', result.group(1) + '.png').replace('.svg', result.group(1) + '.svg').replace('.pdf', result.group(1) + '.pdf'))
            text = text.replace(result.group(0), new_absolute_path)
            result = re.search('result_(.*)\.png', text, re.MULTILINE)

        if not len(relativePaths):
            relativePaths.append(relativePath)

        os.chdir(rstdir)
        logger = Logger()
        sys.stdout = logger
        exec(text, globals())
        os.chdir(curdir)
        global outputData
        sys.stdout = sys.__stdout__
        return outputData[logger], relativePaths
    except Exception as e:
        traceback.print_exc()

def render(indigo, options, text, absolute_path, relativePath, rstdir, curdir):
    indigo_object_type = options['indigoobjecttype']
    indigo_loader_type = options['indigoloadertype']
    loader = None
    if indigo_object_type == 'molecule':
        if indigo_loader_type == 'text':
            loader = indigo.loadMolecule
        elif indigo_loader_type == 'file':
            loader = indigo.loadMoleculeFromFile
    elif indigo_object_type == 'queryMolecule':
        if indigo_loader_type == 'text':
            loader = indigo.loadQueryMolecule
        elif indigo_loader_type == 'file':
            loader = indigo.loadQueryMoleculeFromFile
    elif indigo_object_type == 'reaction':
        if indigo_loader_type == 'text':
            loader = indigo.loadReaction
        elif indigo_loader_type == 'file':
            loader = indigo.loadReactionFromFile
    elif indigo_object_type == 'queryReaction':
        if indigo_loader_type == 'text':
            loader = indigo.loadQueryReaction
        elif indigo_loader_type == 'file':
            loader = indigo.loadQueryReactionFromFile
    elif indigo_object_type == 'smarts':
        if indigo_loader_type == 'text':
            loader = indigo.loadSmarts
        elif indigo_loader_type == 'file':
            loader = indigo.loadSmartsFromFile
    elif indigo_object_type == 'reactionSmarts':
        if indigo_loader_type == 'text':
            loader = indigo.loadReactionSmarts
        elif indigo_loader_type == 'file':
            loader = indigo.loadReactonSmartsFromFile
    elif indigo_object_type == 'code':
        loader = executeIndigoCode
    if not loader:
        raise IndigoRendererError('Cannot find indigo loader for object type: %s, %s' % (indigo_object_type, indigo_loader_type))
    if loader != executeIndigoCode:
        indigoRenderer.renderToFile(loader(text), absolute_path)
    else:
        return executeIndigoCode(text, absolute_path, relativePath, rstdir, curdir, options)

def render_indigorenderer(app, text, options, rstdir, curdir):
    # Reset Indigo to use new fresh options
    resetIndigo()

    format_map = DEFAULT_FORMATS.copy()
    format_map.update(app.builder.config.indigorenderer_format)
    output_format = format_map[app.builder.format]
    hashid = get_hashid(text, options)
    output_filename = 'indigorenderer_%s.%s' % (hashid, output_format) if not 'imagename' in options else options['imagename'] + '.' + output_format
    relative_path = ''

    if app.builder.format == 'html':
        output_folder = relative_uri(app.builder.env.docname,'_images')
        relative_path = os.path.join(output_folder, output_filename)
        absolute_path = os.path.join(app.builder.outdir, '_images', output_filename)
    else:
        relative_path = output_filename
        absolute_path = os.path.join(app.builder.outdir, output_filename)
    absolute_path = absolute_path.replace('\\', '\\\\')
    relative_paths = [relative_path, ]
    output = None
    try:
        if 'indigooptions' in options:
            strings = options['indigooptions'][1:-1].split(';')
            for string in strings:
                key, value = string.split('=')
                indigo.setOption(key, value.replace('"', ''))
        indigo.setOption('render-output-format', output_format)
        result = render(indigo, options, text, absolute_path, relative_path, rstdir, curdir)
        if result:
            output, relative_paths = result
    except IndigoException, exc:
        raise IndigoRendererError(exc)
    return relative_paths, output

def setup(app):
    app.add_directive('indigorenderer', IndigoRendererDirective)
    app.connect('doctree-read', render_indigorenderer_images)
    app.add_config_value('indigorenderer_format', DEFAULT_FORMATS, 'html')
