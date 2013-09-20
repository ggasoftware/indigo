import sys, os
fn = __file__

dll_full_path = "../dist/python"
if not os.path.exists(dll_full_path):
    sys.path.insert(0, "../api/python")
    sys.path.insert(0, "../api/plugins/renderer/python")
    sys.path.insert(0, "../api/plugins/inchi/python")
    sys.path.insert(0, "../api/plugins/bingo/python")
else:
    sys.path.insert(0, dll_full_path)

builder = 'html'    
    
lst = [fn, '-c', 'source', '-b', builder, 'source', 'build/' + builder]

images_dir = 'build/' + builder + '/_images'
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

from sphinx import main
main(lst)
