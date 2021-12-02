from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from todaymovieapp.decorators import todaymovie_ownership_required
from todaymovieapp.forms import TodaymovieUpdateForm
from todaymovieapp.models import todaymovie

has_ownership = [todaymovie_ownership_required, login_required]

def main(request):
    if request.method == "POST":
        temp = request.POST.get('main_input')
        new_main = todaymovie()
        new_main.text = temp
        new_main.save()

        return HttpResponseRedirect(reverse('todaymovie:main'))
    else:
        main_list = todaymovie.objects.all()
        return render(request, 'todaymovieapp/main.html', context={'main_list': main_list})

class TodaymovieCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('todaymovieapp:main')
    template_name = 'todaymovieapp/create.html'

class TodaymovieDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'todaymovieapp/detail.html'

    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(TodaymovieDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class TodaymovieDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('todaymovieapp:login')
    template_name = 'todaymovieapp/delete.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class TodaymovieUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = TodaymovieUpdateForm
    success_url = reverse_lazy('todaymovieapp:main')
    template_name = 'todaymovieapp/update.html'