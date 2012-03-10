Render: render decorator helper for Django
==========================================

This package provides function decorator for templates rendering in request context with dry use.

Usecase
-------

It support simple template rendering with decorator function. It is basic use example. Will be
rendered template "APPNAME/VIEWNAME.html"

	from render.template import render
	@render
	def index():
		//index view logic goes here
		return {
			'var1': val1,
			'var2': val2,
		}

You can override VIEWNAME part in template path. See example.

	from render.template import render
	@render
	def all():
		//all view logic goes here
		return 'index.html', {
			'var1': val1,
			'var2': val2,
		}

You can override APPNAME part in template path. See example.

	from render.template import renderer
	@renderer("otherapp")
	def all():
		//all view logic goes here
		return 'index.html', {
			'var1': val1,
			'var2': val2,
		}

Or you can return "ready to use HttpResponse" object. render wrapepr just return it.

	from render.template import render
	@render
	def all():
		if some_logic:
			return HttpResponse("It's ok too")
		//all view logic goes here
		return 'index.html', {
			'var1': val1,
			'var2': val2,
		}

It is clean & dry helper! Use it :-)

phpdude
