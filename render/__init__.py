__author__ = 'phpdude'
__version__ = (0, 1, 0)

def correct_path(template_name, prefix):
    if template_name.startswith('/'):
        return template_name[1:]
    return '%s%s' % (prefix, template_name)
