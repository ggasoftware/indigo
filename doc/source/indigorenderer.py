import hashlib
import os

from docutils import nodes
from docutils.parsers.rst import directives
from indigo import Indigo, IndigoException
from indigo_renderer import IndigoRenderer
from indigo_inchi import IndigoInchi
from sphinx.errors import SphinxError
from sphinx.util import relative_uri

DEFAULT_FORMATS = dict(html='svg', latex='pdf', text=None)

indigo = Indigo()
indigoRenderer = IndigoRenderer(indigo)
indigoInchi = IndigoInchi(indigo)

def get_hashid(text, options):
    hashkey = text.encode('utf-8') + str(options)
    hashid = hashlib.sha1(hashkey).hexdigest()
    return hashid

class IndigoRendererError(SphinxError):
    category = 'IndigoRenderer error'

class IndigoRendererDirective(directives.images.Image):
    has_content = True
    required_arguments = 0
    own_option_spec = dict(
        indigooptions = str,
        indigoobjecttype = str,
        indigoloadertype = str
    )

    option_spec = directives.images.Image.option_spec.copy()
    option_spec.update(own_option_spec)

    def run(self):
        self.arguments = ['']
        indigorenderer_options = dict([(k,v) for k,v in self.options.items()
                                      if k in self.own_option_spec])

        (image_node,) = directives.images.Image.run(self)
        if isinstance(image_node, nodes.system_message):
            return [image_node]
        text = '\n'.join(self.content)
        image_node.indigorenderer = dict(text=text, options=indigorenderer_options)
        if indigorenderer_options['indigoobjecttype'] == 'code':
             literal = nodes.literal_block(text, text)
             literal['language'] = 'python'
             return [nodes.transition(), literal, image_node, nodes.transition()]
        else:
            return [image_node]

def render_indigorenderer_images(app, doctree):
    for img in doctree.traverse(nodes.image):
        if not hasattr(img, 'indigorenderer'):
            continue

        text = img.indigorenderer['text']
        options = img.indigorenderer['options']
        try:
            relative_path = render_indigorenderer(app, text, options)
            img['uri'] = relative_path

        except IndigoRendererError, exc:
            app.builder.warn('indigorenderer error: ' + str(exc))
            img.replace_self(nodes.literal_block(text, text))
            continue

def executeIndigoCode(text, absolute_path):
    exec(text.replace('result.png', absolute_path))

def render(indigo, options, text, absolute_path):
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
        executeIndigoCode(text, absolute_path)

def render_indigorenderer(app, text, options):
    format_map = DEFAULT_FORMATS.copy()
    format_map.update(app.builder.config.indigorenderer_format)
    output_format = format_map[app.builder.format]
    hashid = get_hashid(text,options)
    output_filename = 'indigorenderer_%s.%s' % (hashid, output_format)

    if app.builder.format == 'html':
        output_folder = relative_uri(app.builder.env.docname,'_images')
        relative_path = os.path.join(output_folder, output_filename)
        absolute_path = os.path.join(app.builder.outdir, '_images', output_filename)
    else:
        relative_path = output_filename
        absolute_path = os.path.join(app.builder.outdir, output_filename)

    try:
        # Set defaul options
        indigo.setOption('render-bond-length', '20')
        indigo.setOption('render-relative-thickness', '1.3')
        indigo.setOption('render-coloring', True)
        if 'indigooptions' in options:
            strings = options['indigooptions'][1:-1].split(';')
            for string in strings:
                key, value = string.split('=')
                indigo.setOption(key, value.replace('"', ''))
        indigo.setOption('render-output-format', output_format)
        render(indigo, options, text, absolute_path)
    except IndigoException, exc:
        raise IndigoRendererError(exc)

    return relative_path

def setup(app):
    app.add_directive('indigorenderer', IndigoRendererDirective)
    app.connect('doctree-read', render_indigorenderer_images)
    app.add_config_value('indigorenderer_format', DEFAULT_FORMATS, 'html')
