from django.views.generic.base import TemplateView

class PostsPageView(TemplateView):
    template_name = "posts/list.html"