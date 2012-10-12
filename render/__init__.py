__author__ = 'phpdude'
__version__ = (0, 3, 5)

def correct_path(template_name, prefix):
    if template_name.startswith('/'):
        return template_name[1:]
    return "/".join((x.strip("/") for x in (prefix, template_name))).lstrip("/")


def process_response(response, tplname):
    from django.conf import settings

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


def render_template(template_name, context_processors=None, context_instance=None, mimetype=None):
    from django.conf import settings
    if getattr(settings, 'RENDER_ENGINE', 'django').lower() == 'coffin':
        from coffin.shortcuts import render_to_response
    else:
        from django.shortcuts import render_to_response

    return render_to_response(template_name,
        dictionary=context_processors,
        context_instance=context_instance,
        mimetype=mimetype
    )
