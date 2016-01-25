import ast
from django.template import Context, Template
from forms import FiddleForm
from django.shortcuts import render

def make_fiddle(request):
    rendered_template = ""
    fiddle_styles = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FiddleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            fiddle_context = form.cleaned_data.get('context')
            fiddle_template = form.cleaned_data.get('template').replace('"','\"')
            fiddle_styles = form.cleaned_data.get('styles')
            
            print 'this', fiddle_context, fiddle_template
            
            if fiddle_context and fiddle_template:
                fiddle_context = Context(ast.literal_eval(fiddle_context))
                fiddle_template = Template(fiddle_template)
                rendered_template = fiddle_template.render(fiddle_context)

    else:
        form = FiddleForm()

    context = {
        'form': form,
        'rendered_template': rendered_template,
        'styles': fiddle_styles
    }
    return render(request, "fiddler/on_the_roof.html", context)
