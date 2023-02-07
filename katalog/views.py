from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

menu = [{'title':'Главная сраница', 'url_name':'home'},
        {'title':'Каталог','url_name':'katalog'},
        {'title':'Контакты', 'url_name':'about'},

        ]
def home(request):
    towar = Towar.objects.all()[:3]
    cats = Category.objects.all()
    return render(request, 'katalog/home.html', {'towar': towar, 'title':'Главная страница', 'menu':menu})


def katalog(request):
    towar = Towar.objects.all()
    cats = Category.objects.all()

    context = {
        'towar': towar,
        'title':'Каталог товаров',
        'menu':menu,
        'cats':cats,
        'cat_selected':0,
    }
    return render(request, 'katalog/katalog_list.html', context=context)


def post(request, post_id):
    post = get_object_or_404(Towar, pk=post_id)
    context = {'post': post,
               'menu': menu,
               'title': "Подробно о товаре"}
    return render(request, 'katalog/post.html', context=context,)


def about(request):
    return render(request, 'katalog/about.html',{'title':'Контакты', 'menu':menu})


def show_category(request, cat_id,):
    towar = Towar.objects.filter(cat_id=cat_id)
    cats= Category.objects.all()
    context = {
        'towar': towar,
        'title': 'Поиск по категории',
        'menu': menu,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'katalog/katalog_list.html', context=context)