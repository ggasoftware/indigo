import os
from docutils import nodes
from docutils.parsers.rst import directives
from indigo import Indigo, IndigoException
from indigo_renderer import IndigoRenderer
from indigo_inchi import IndigoInchi
from sphinx.errors import SphinxError
from sphinx.util import relative_uri

DEFAULT_FORMATS = dict(html='svg', latex='pdf', text=None, xml=None)

class IndigoImageError(SphinxError):
    category = 'IndigoImage error'

class IndigoImageDirective(directives.images.Image):
    has_content = True
    required_arguments = 0

    own_option_spec = dict(
        imagename = str
    )

    option_spec = directives.images.Image.option_spec.copy()
    option_spec.update(own_option_spec)

    def run(self):
        self.arguments = ['']
        options = dict([(k,v) for k,v in self.options.items() if k in self.own_option_spec])
        (image_node,) = directives.images.Image.run(self)
        image_node.indigoimage = dict(text='\n'.join(self.content), options=options)

        return [image_node, ]


def render_indigoimage_images(app, doctree):
    for img in doctree.traverse(nodes.image):
        if not hasattr(img, 'indigoimage'):
            continue

        text = img.indigoimage['text']
        options = img.indigoimage['options']
        try:
            relative_path = get_relative_path(app, text, options)
            if relative_path:
                relative_path = relative_path.replace('\\', '/')
            img['uri'] = relative_path

        except IndigoImageError, exc:
            app.builder.warn('indigorenderer error: ' + str(exc))
            img.replace_self(nodes.literal_block(text, text))
            continue

def get_relative_path(app, text, options):
    # Reset Indigo to use new fresh options
    format_map = DEFAULT_FORMATS.copy()
    output_format = format_map[app.builder.format]
    if output_format is None:
        return None
    output_filename = options['imagename'] + '.' + output_format

    if app.builder.format == 'html':
        output_folder = relative_uri(app.builder.env.docname,'_images')
        relative_path = os.path.join(output_folder, output_filename)
    else:
        relative_path = output_filename
    return relative_path

def setup(app):
    app.add_directive('indigoimage', IndigoImageDirective)
    app.connect('doctree-read', render_indigoimage_images)
    app.add_config_value('indigoimage_format', DEFAULT_FORMATS, 'html')