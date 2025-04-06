from django.db import models
from django.utils.text import slugify
import random

class Donor(models.Model):
    """Model for donors with banner images that will scroll horizontally"""
    name = models.CharField(max_length=100)
    banner = models.ImageField(upload_to='donors/', help_text="Upload banner image (300x100 pixels)")
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class GalleryCategory(models.Model):
    """Categories for organizing gallery images"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Gallery Categories"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    """Model for gallery images with title and description"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    is_featured = models.BooleanField(default=False, help_text="Feature this image on the homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def get_random_featured_images(cls, count=5):
        """Get random featured images for homepage slideshow"""
        featured = list(cls.objects.filter(is_featured=True))
        if len(featured) <= count:
            return featured
        return random.sample(featured, count)

class StudentAchievement(models.Model):
    """Model for student achievements and activities"""
    student_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.student_name} - {self.title}"

class AboutPage(models.Model):
    """Model for About Us page content"""
    title = models.CharField(max_length=200, default="About Us")
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

class DonatePage(models.Model):
    """Model for Donate page content"""
    title = models.CharField(max_length=200, default="Donate")
    content = models.TextField()
    bank_details = models.TextField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Donate Page"
        verbose_name_plural = "Donate Page"
