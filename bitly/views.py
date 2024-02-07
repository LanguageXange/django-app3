from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse

# Create your views here.

from .models import Link
from .forms import LinkForm
def index(request):
    links = Link.objects.all()
    context = {"links":links}
    return render(request,'bitly/index.html',context)


# shortened url -> final destination
def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click() # increment clicks
    # redirect
    return redirect(link.url)



def add_link(request):
    # print(request.POST) ## <QueryDict: {'csrfmiddlewaretoken':['xxxx'], 'mylink':['somethinghere']}>
    if request.method == 'POST':
        # form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            # process data
            print(form.cleaned_data)
            form.save()
            return redirect(reverse('home'))
    else:
        form = LinkForm()

    context = {
        'myform':form
    }
    return render(request,'bitly/create.html',context)


