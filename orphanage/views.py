from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import (
    Donor, 
    GalleryCategory, 
    GalleryImage, 
    StudentAchievement, 
    AboutPage, 
    DonatePage
)

class HomeView(TemplateView):
    template_name = 'orphanage/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_images'] = GalleryImage.get_random_featured_images(5)
        context['donors'] = Donor.objects.all()
        context['achievements'] = StudentAchievement.objects.all()[:3]
        return context

class GalleryListView(ListView):
    model = GalleryCategory
    template_name = 'orphanage/gallery.html'
    context_object_name = 'categories'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_images'] = GalleryImage.get_random_featured_images(5)
        return context

class GalleryImageListView(ListView):
    model = GalleryImage
    template_name = 'orphanage/gallery_category.html'
    context_object_name = 'images'
    
    def get_queryset(self):
        self.category = get_object_or_404(GalleryCategory, slug=self.kwargs['slug'])
        return GalleryImage.objects.filter(category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class GalleryImageDetailView(DetailView):
    model = GalleryImage
    template_name = 'orphanage/gallery_detail.html'
    context_object_name = 'image'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get related images (same category)
        related_images = GalleryImage.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        context['related_images'] = related_images
        return context

class AboutView(TemplateView):
    template_name = 'orphanage/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['about'] = AboutPage.objects.first()
        except AboutPage.DoesNotExist:
            context['about'] = None
        return context

class DonateView(TemplateView):
    template_name = 'orphanage/donate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['donate'] = DonatePage.objects.first()
        except DonatePage.DoesNotExist:
            context['donate'] = None
        return context

class StudentAchievementListView(ListView):
    model = StudentAchievement
    template_name = 'orphanage/achievements.html'
    context_object_name = 'achievements'
    paginate_by = 10

class StudentAchievementDetailView(DetailView):
    model = StudentAchievement
    template_name = 'orphanage/achievement_detail.html'
    context_object_name = 'achievement'
