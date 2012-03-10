# encoding: utf-8
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.functional import wraps
from render import correct_path

__author__ = 'phpdude'

MIMETYPE = getattr(settings, 'DEFAULT_CONTENT_TYPE')

def renderer(prefix=None):
	tplprefix = prefix.rstrip('/') + "/" if prefix else ""

	def renderer(func):
		@wraps(func)
		def wrapper(request, *args, **kwargs):
			template_name, mimetype, context_processors = '', '', ''

			response = func(request, *args, **kwargs)
			if isinstance(response, HttpResponse):
				return response

			if response is None:
				response = func.__name__ + ".html"
			elif isinstance(response, dict):
				response = (func.__name__ + ".html", response)

			if isinstance(response, basestring):
				template_name = response
				context_processors = {}
				mimetype = MIMETYPE
			elif isinstance(response, (tuple, list)):
				len_tuple = len(response)
				if len_tuple == 2:
					template_name, context_processors = response
					mimetype = MIMETYPE
				elif len_tuple == 3:
					template_name, context_processors, mimetype = response

			if tplprefix:
				if isinstance(template_name, (list, tuple)):
					template_name = map(correct_path, template_name)
				else:
					template_name = correct_path(template_name, tplprefix)
			else:
				template_name = correct_path(template_name, func.__module__.split(".")[0] + "/")

			context_processors['_app'] = func.__module__.split(".")[0]
			context_processors['_view'] = func.__name__
			context_processors['layout'] = correct_path('base.html', tplprefix or func.__module__.split(".")[0] + "/")

			return render_to_response(template_name, context_processors, context_instance=RequestContext(request), mimetype=mimetype)

		return wrapper

	return renderer

render = renderer()
