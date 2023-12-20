from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Blog(models.Model):
    objects = None
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_date = models.DateField(auto_now_add=True)
    article_image = ProcessedImageField(upload_to='blog_photos',
                                             processors=[ResizeToFill(360,300)],
                                             format='JPEG',
                                             options={'quality':60})
    article_image_thumbnail = ImageSpecField(source = 'article_image',
                                        processors=[ResizeToFill(360, 300)],
                                        format='JPEG',
                                        options={'quality': 60})

    category = models.CharField(max_length=50, null=True, blank=True)
    main_article = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=100)
    comment_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
