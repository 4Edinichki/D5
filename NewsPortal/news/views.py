from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime


class PostList(ListView):
    model = Post
    ordering = 'id'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ArticleList(PostList):
    template_name = 'article.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect('//')
    form = PostForm()
    return render(request, 'news_edit.html', {'form': form})


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        post.category_news = self.model.NEWS
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        post.category_news = self.model.ARTICLE
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        if post.category_news(current_url.split('/')[0]) == 'NW':
            post.category_news = self.model.NEWS
        else:
            return reverse_lazy('news_list')
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

    # def form_valid(self, form):
    #     current_url = self.request.path
    #     post = form.save(commit=False)
    #     if
