

# Create your views here.
from django.views.generic import ListView

from contentapp.models import Content
from .models import Word2vec


class ContentListView(ListView):
    model = Content
    context_object_name = 'content_list'
    template_name = 'contentapp/movie.html'
    paginate_by = 10