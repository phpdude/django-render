from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.functional import wraps
from render import correct_path

__author__ = 'phpdude'

def renderer(prefix=""):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            template_name, context_processors = '', {}

            mimetype = getattr(settings, 'DEFAULT_CONTENT_TYPE', 'text/html')
            module_name = func.__module__.split(".")[0]

            response = func(request, *args, **kwargs)
            if isinstance(response, HttpResponse):
                return response

            if response is None:
                response = func.__name__ + ".html"
            elif isinstance(response, dict):
                response = (func.__name__ + ".html", response)

            if isinstance(response, basestring):
                template_name = response
            elif isinstance(response, (tuple, list)):
                if len(response) == 2:
                    template_name, context_processors = response
                elif len(response) == 3:
                    template_name, context_processors, mimetype = response

            if prefix:
                if isinstance(template_name, (list, tuple)):
                    template_name = map(correct_path, template_name)
                else:
                    template_name = correct_path(template_name, prefix)
            else:
                template_name = correct_path(template_name, module_name)

            context_processors['App'] = module_name
            context_processors['View'] = func.__name__
            context_processors['Layout'] = correct_path('base.html', prefix or module_name)

            return render_to_response(template_name, context_processors, context_instance=RequestContext(request), mimetype=mimetype)

        return wrapper

    return renderer

render = renderer()
