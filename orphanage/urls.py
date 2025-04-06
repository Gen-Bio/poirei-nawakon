from django.urls import path
from . import views

app_name = 'orphanage'

urlpatterns = [
    # Home page
    path('', views.HomeView.as_view(), name='home'),
    
    # Gallery pages
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('gallery/category/<slug:slug>/', views.GalleryImageListView.as_view(), name='gallery_category'),
    path('gallery/image/<slug:slug>/', views.GalleryImageDetailView.as_view(), name='gallery_detail'),
    
    # About page
    path('about/', views.AboutView.as_view(), name='about'),
    
    # Donate page
    path('donate/', views.DonateView.as_view(), name='donate'),
    
    # Student achievements
    path('achievements/', views.StudentAchievementListView.as_view(), name='achievements'),
    path('achievements/<int:pk>/', views.StudentAchievementDetailView.as_view(), name='achievement_detail'),
]