from django.http import HttpResponseForbidden

from projectapp.models import Project


def project_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Project.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated