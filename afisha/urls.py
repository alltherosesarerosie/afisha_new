from django.contrib import admin
from django.urls import path
from movie_app import views
from movie_app.views import movie_review_list_view, director_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directors/', views.director_list_view),
    path('directors/<int:pk>/', views.director_detail_view),
    path('movies/',views.movie_list_view),
    path('movies/<int:pk>/', views.movie_detail_view),
    path('reviews/', views.movie_list_view),
    path('reviews/<int:pk>/', views.movie_detail_view),
    path('movies_review/', movie_review_list_view, name='movie-review-list'),
    path('directors_list/', director_list_view, name='director-list'),
]
