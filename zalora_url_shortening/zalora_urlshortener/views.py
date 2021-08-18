'''
Shortener views
'''
from django.shortcuts import render 

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Shortener

from .forms import ShortenerForm


import qrcode
import qrcode.image.svg
from io import BytesIO




# Create your views here.

def home_view(request):
    
    template = 'zalora_urlshortener/home.html'

    
    context = {}

    # Empty form
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)

        if used_form.is_valid():
            
            shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            
            long_url = shortened_object.long_url 
             
            context['new_url']  = new_url
            context['long_url'] = long_url

            factory = qrcode.image.svg.SvgImage
            img = qrcode.make(new_url, image_factory=factory, box_size=20)
            stream = BytesIO()
            img.save(stream)
            context["svg"] = stream.getvalue().decode()
             
            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)

        shortener.uuid += 1        

        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('Sorry this link is broken :(')