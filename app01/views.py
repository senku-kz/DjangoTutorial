from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *


# Create your views here.
def task_01(request):
    return HttpResponse("Страница приложения app01.")


def task_02(request):
    return HttpResponse("<h1>Страница приложения app01.</h1>")


def task_03(request, cat_id):
    return HttpResponse(f"<h1>Страница приложения app01.</h1><p>{cat_id}</p>")


def task_04(request, cat):
    return HttpResponse(f"<h1>Страница приложения app01.</h1><p>{cat}</p>")


def task_05(request, year):
    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")


def task_06(request):
    """Get parameters from GET/POST"""
    if request.GET:
        print("GET:", request.GET)
        t = request.GET
        return HttpResponse(f"<h1>Страница приложения app01.</h1><p>{t['type']}</p><p>{t['name']}</p>")

    if request.POST:
        print("POST:", request.POST)
        t = request.POST
        return HttpResponse(f"<h1>Страница приложения app01.</h1><p>{t['type']}</p><p>{t['name']}</p>")


def task_07(request, year):
    """Page not found"""
    if int(year) > 2023:
        raise Http404()

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")


def task_08(request, year):
    """Redirect 302"""
    if int(year) > 2023:
        return redirect("/app01/task01/")

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")


def task_09(request, year):
    """Redirect 301"""
    if int(year) > 2023:
        return redirect("/app01/task01/", permanent=True)

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")


def task_10(request, year):
    """Redirect 302"""
    if int(year) > 2023:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам.</h1><p>{year}</p>")


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'app01/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


@login_required
def about(request):
    return render(request, "app01/about.html", {'menu': menu, 'title': 'about site'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'app01/addpage.html'
    success_url = reverse_lazy('home')

    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'app01/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context = dict(list(context.items()) + list(c_def.items()))
        return context


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'app01/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Категория - ' + str(context['posts'][0].cat),
            cat_selected=context['posts'][0].cat_id
        )
        context = dict(list(context.items()) + list(c_def.items()))
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена.")
