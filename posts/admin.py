from django.contrib import admin



from .models import Post



# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ["__str__","timestamp" ]
	list_filter = ['timestamp']
	search_fields = ['title', 'content']
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)