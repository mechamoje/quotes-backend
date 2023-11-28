from django.contrib import admin
from .models import Quote, Author, Favorite

admin.site.register(Quote)
admin.site.register(Author)
admin.site.register(Favorite)
