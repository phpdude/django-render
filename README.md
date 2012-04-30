Render: render sugar for Django
==========================================

This package provides decorators for templates rendering and CBV mixin in request context with simple code use.

__Important:__ all template renders goes in request context. Sessions, cookies, meta, etc is available from templates.

Installation
------------

You can install library via pip.
    pip install django-render

Supports coffin (jinja2 adapter for django)
-------------------------

You can select template render engine via settings.py directive.

    RENDER_ENGINE='coffin'

django-render will use coffin adapter for rendering templates transparent.

Usage in functional views
-------------------------

It support simple template rendering with decorator function. It is basic use example. Will be
rendered template "APPNAME/VIEWNAME.html"

    from render.mixins import render
    @render
    def index():
        #index view logic goes here
        return {
            'var1': val1,
            'var2': val2,
        }

    from render.mixins import render
    @render
    def index():
        #index view logic goes here
        return {
            'var1': val1,
            'var2': val2,
        }, 'text/plain'

You can override VIEWNAME part in template path. See example.

    from render.mixins import render
    @render
    def all():
        #all view logic goes here
        return 'index.html', {
            'var1': val1,
            'var2': val2,
        }

You can override APPNAME part in template path. See example.

    from render.mixins import renderer
    @renderer("otherapp")
    def all():
        #all view logic goes here
        return 'index.html', {
            'var1': val1,
            'var2': val2,
        }

Or you can return "ready to use HttpResponse" object. render wrapepr just return it.

    from render.mixins import render
    @render
    def all():
        if some_logic:
            return HttpResponse("It's ok too")
        #all view logic goes here
        return 'index.html', {
            'var1': val1,
            'var2': val2,
        }

Usage in Class Based Views
--------------------------

It supports basic TemplateView's like

    class Index(RenderViewMixin, TemplateView):
        pass

It calculates template name as APP/VIEW.html

You can override heuristic by declaring template_name variable like

    class Index(RenderViewMixin, TemplateView):
        template_name = 'custom.html'

This call APP/custom.html. Or you can add full template path like

    class Index(RenderViewMixin, TemplateView):
        template_name = 'otherapp/custom.html'

Then will be called 'otherapp/custom.html'

Like functional view you can use render sugar in get/post/delete/etc request to your CBV.

    class Index(RenderViewMixin, TemplateView):
        def get(self, request, *args, **kwargs):
            return {
                "title": 'My awesome title!'
            }

Supported all sugar with defining template name, context data and mimetype.

    class Index(RenderViewMixin, TemplateView):
        def get(self, request, *args, **kwargs):
            return 'print.html', {
                "title": 'My awesome title!'
            }, 'text/plain'

It works and with global template_name defining.

    class Index(RenderViewMixin, TemplateView):
        template_name = 'default.html'
        def get(self, request, *args, **kwargs):
            return {
                "title": 'My awesome title!'
            }, 'text/plain'

Template processing
-------------------

Into template context render add few variables.

*  __App__ - Application name, where was called view
*  __View__ - View function name
*  __Layout__ - Base layout path. Compiles from APPNAME and base.html. Example: for news app it will be equal "news/base.html"

Example in template:
    {% extends Layout %}

    <div class="{{ App }}_{{ View }}">{% block content %}</div>

It is clean & dry helper! Use it :-)

phpdude
