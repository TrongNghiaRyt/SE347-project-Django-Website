from django.db import models
from a1test.models import *

KINDS = (
    ('KN', 'Khái niệm'),
    ('QT', 'Qui tắc'),
    ('TD', 'Tốc độ'),
    ('NV', 'Nghiệp vụ'),
    ('VH', 'Văn hóa'),
    ('KT', 'Kỹ thuật'),
    ('CT', 'Cấu tạo'),
    ('BB', 'Biển báo'),
    ('SH', 'Sa hình'),
)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    discription = models.TextField()
    kind = models.CharField(max_length=2, choices=KINDS)

    def __str__(self):
        return self.title

class BlogContent(models.Model):
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    detail = models.TextField()

    def __str__(self):
        return self.title