from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

from markdown_deux import markdown

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=220)
	content = models.TextField()
	image = models.FileField(null=True, blank=True)
	timestamp = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(unique=True)

	def __str__(self):		
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={'slug' : self.slug })

	def markdown(self):	
		return mark_safe(markdown(self.content))


	class Meta:
		ordering = ["-timestamp"]