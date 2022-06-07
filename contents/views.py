from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post , Category, bloodbank, blooddonors, places
from .forms import  PostSearchForm,bloodbanksearchForm,blooddonorsearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q 

def home(request):
    all_posts = Post.newmanager.all()
    return render(request, 'blog/index.html', {'posts': all_posts})


def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')


    fav = bool

    if post.favourites.filter(id=request.user.id).exists():
        fav = True
    return render(request, 'blog/single.html', {'post': post })


class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context

def post_search(request):
    form = PostSearchForm()
    q = ''
    c=''
    l=''
    results=[]
    query=Q()
    if "q" in request.GET:
        form=PostSearchForm(request.GET)
        form.full_clean()
        if form.is_valid():
            q=form.cleaned_data['q']
            c=form.cleaned_data['c']
            l=form.cleaned_data['l']
            if c is not None:
                query &= Q(category=c)
            if l is not None:
                query &= Q(place=l)    
            if q is not None:
                query &= Q(title__contains=q)    

    results =Post.objects.filter(query)
    return render(request,'blog/search.html',
           {'form':form,'q':q,'results':results}
           )    

def bloodbank_search(request):
    form = bloodbanksearchForm()
    x=''
    bloodresults=[]
    query=Q()
    if "x" in request.GET:
        form=bloodbanksearchForm(request.GET)
        form.full_clean()
        if form.is_valid():
            x=form.cleaned_data['x']
            if x is not None:
                query &= Q(excerpt=x)    

    bloodresults = bloodbank.objects.filter(query)
    return render(request,'blog/searchbloood.html',
           {'form':form,'q':x,'results':bloodresults}
           )    

def blooddonor_search(request):
    form = blooddonorsearchForm()
    y=''
    blooddonorsresults=[]
    query=Q()
    if "y" in request.GET:
        form=blooddonorsearchForm(request.GET)
        form.full_clean()
        if form.is_valid():
            y=form.cleaned_data['y']
            if y is not None:
                query &= Q(blood_group=y)    

    blooddonorsresults = blooddonors.objects.filter(query)
    return render(request,'blog/searchblooddonors.html',
           {'form':form,'q':y,'results':blooddonorsresults}
           )   
          