from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('katalog/',views.katalog, name='katalog'),
    path('katalog/posts/<int:post_id>/',views.post, name='post'),
    path('about/',views.about, name='about'),
    path('cetegory/<int:cat_id>/',views.show_category, name='category'),
]
