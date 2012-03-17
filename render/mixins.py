# encoding: utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic.base import View
from render import process_response, correct_path

__author__ = 'phpdude'

class RenderViewMixin():
    template_name = None

    def get_template_names(self):
        if self.template_name is None:
            template_name = ".".join((self.__module__, self.__class__.__name__)).lower().replace('.views.', '.')
            return ["%s.html" % template_name.replace('.', '/')]
        else:
            return [self.template_name]

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in View.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        self.request = request
        self.args = args
        self.kwargs = kwargs

        response = handler(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            return response

        module_name = self.__module__.split('.')[0]
        template_name = self.get_template_names()[0][:-5] #strip .html extension
        template_name, context_processors, mimetype = process_response(response, template_name)
        if not template_name.__contains__('/'):
            template_name = correct_path(template_name, module_name)

        context_processors['App'] = module_name
        context_processors['View'] = self.__class__.__name__.lower()
        context_processors['Layout'] = correct_path('base.html', module_name)

        return render_to_response(template_name, context_processors, context_instance=RequestContext(request), mimetype=mimetype)
