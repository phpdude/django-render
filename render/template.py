from django.http import HttpResponse
from django.template.context import RequestContext
from django.utils.functional import wraps
from render import correct_path, process_response, render_template

__author__ = 'phpdude'

def renderer(prefix=""):
    def renderer(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            module_name = func.__module__.split(".")[0]

            response = func(request, *args, **kwargs)
            if isinstance(response, HttpResponse):
                return response

            template_name, context_processors, mimetype = process_response(response, func.__name__)

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

            return render_template(template_name, context_processors, context_instance=RequestContext(request),
                mimetype=mimetype)

        return wrapper

    return renderer

render = renderer()
