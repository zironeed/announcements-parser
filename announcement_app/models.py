from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Announcement title')
    author = models.CharField(max_length=255, verbose_name='Announcement author')
    view_count = models.PositiveIntegerField(default=0, verbose_name='Announcement view count')
    place = models.PositiveSmallIntegerField(default=1, verbose_name='Announcement place')

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return f'{self.title}'
