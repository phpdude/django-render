from django.conf import settings

__author__ = 'phpdude'
__version__ = (0, 2, 0)

def correct_path(template_name, prefix):
    if template_name.startswith('/'):
        return template_name[1:]
    return "/".join((x.strip("/") for x in (prefix, template_name))).lstrip("/")


def process_response(response, tplname):
    template_name, context_processors, mimetype = '', {}, getattr(settings, 'DEFAULT_CONTENT_TYPE', 'text/html')

    if response is None:
        response = tplname + ".html"
    elif isinstance(response, dict):
        response = (tplname + ".html", response)

    if isinstance(response, basestring):
        template_name = response
    elif isinstance(response, (tuple, list)):
        if not isinstance(response[0], basestring):
            response = (tplname + ".html",) + tuple(response)
        if len(response) == 2:
            template_name, context_processors = response
        elif len(response) == 3:
            template_name, context_processors, mimetype = response

    return template_name, context_processors, mimetype
