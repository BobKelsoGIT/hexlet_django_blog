from django.conf import settings
from django.shortcuts import render
from django.views import View


# def index(request):
#     context = {
#         'app_name': settings.APP_NAME,
#     }
#     return render(request, 'articles/index.html', context)

class IndexView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        context = {
            'app_name': settings.APP_NAME,
            'article_text': f'Статья номер {article_id}. Тег {tags}',
        }
        return render(request, 'articles/index.html', context)
