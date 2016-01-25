import ast
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import Context, Template
from forms import FiddleForm
from models import Fiddle
import utils

def make_fiddle(request):

    context = {}
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FiddleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            action = request.POST.get('action','show')

            fiddle_context = form.cleaned_data.get('context')
            fiddle_template = form.cleaned_data.get('template').replace('"','\"')
            fiddle_styles = form.cleaned_data.get('styles')
            try:
                if fiddle_context and fiddle_template:
                    rendered_template = fiddle_render(fiddle_context,
                                                      fiddle_template)
                    context.update({
                        'form': form,
                        'rendered_template': rendered_template,
                        'styles': fiddle_styles
                    })

                    if action == 'save':
                        fiddle = form.save()
                        return redirect(
                            reverse('load_fiddle',
                                    args=[utils.base62_encode(fiddle.pk)])
                        )
            except ValueError as v:
                context.update({
                    'template_error':v,
                    'err_msg':'Your context dictionary is poorly formed.'
                })
            #except Exception as e:
                context.update({
                    'err_msg':'There is an error in your template.',
                    'template_error':e,'d':dir(e)
                })
    else:
        form = FiddleForm()

    context.update({
        'form': form,
    })
    return render(request, "fiddler/on_the_roof.html", context)


def load_fiddle(request,fiddle_stub):
    fiddle_stub = utils.base62_decode(fiddle_stub)
    fiddle = get_object_or_404(Fiddle,pk=fiddle_stub)
    form = FiddleForm(instance=fiddle)

    rendered_template = fiddle_render(fiddle.context, fiddle.template)
    context = {
        'form': form,
        'rendered_template': rendered_template,
        'styles': fiddle.styles,
        'fiddle': fiddle
    }
    return render(request, "fiddler/on_the_roof.html", context)

def fiddle_render(fiddle_context, fiddle_template):
    fiddle_context = Context(ast.literal_eval(fiddle_context))
    fiddle_template = Template(fiddle_template)
    return fiddle_template.render(fiddle_context)

def home(request):
    return load_fiddle(request,'home')
