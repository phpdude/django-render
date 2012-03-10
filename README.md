Render: render decorator helper for Django
==========================================

This package provides function decorator for templates rendering in request context with dry use.

Usecase
-------

It support simple template rendering with decorator function

	@render
	def index():
		//index view logic goes here
		return {
			'var1': val1,
			'var2': val2,
		}
