import time
import random

from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView

from announcement_app.models import Announcement
from announcement_app.services import get_page_urls_and_views, get_data_from_page


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement_list.html'


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement_app/announcement_detail.html'


class AnnouncementParseView(View):
    def get(self, request, *args, **kwargs):
        main_url = request.GET.get('url')
        if not main_url:
            main_url = 'vladivostok/service/construction/guard/+/Системы+видеонаблюдения/'

        self.delete_existing_announcements()

        urls, views = get_page_urls_and_views(main_url)

        for i, url in enumerate(urls):
            time.sleep(random.uniform(2, 5))
            data = get_data_from_page(url)
            if data:
                announcement = Announcement(
                    title=data.get('title', ''),
                    author=data.get('author', ''),
                    view_count=int(views[i]),
                    place=i
                )
                announcement.save()

        return JsonResponse({'message': 'Data parsed and saved'}, status=201)

    @staticmethod
    def delete_existing_announcements():
        Announcement.objects.all().delete()
