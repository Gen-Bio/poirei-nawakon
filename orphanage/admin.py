from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Donor, 
    GalleryCategory, 
    GalleryImage, 
    StudentAchievement, 
    AboutPage, 
    DonatePage
)

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'banner_preview', 'website', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    
    def banner_preview(self, obj):
        if obj.banner:
            return format_html('<img src="{}" width="150" height="50" />', obj.banner.url)
        return "-"
    banner_preview.short_description = 'Banner Preview'
    
    def save_model(self, request, obj, form, change):
        if not change:  # Only show on creation
            self.message_user(request, "Please ensure the banner image is 300x100 pixels for optimal display.")
        super().save_model(request, obj, form, change)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_count')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryImageInline]
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Number of Images'

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_preview', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'title', 'date', 'image_preview')
    list_filter = ('date',)
    search_fields = ('student_name', 'title', 'description')
    date_hierarchy = 'date'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'

class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    
    def has_add_permission(self, request):
        # Only allow one About Page instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

class DonatePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    
    def has_add_permission(self, request):
        # Only allow one Donate Page instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

# Register models
admin.site.register(Donor, DonorAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(StudentAchievement, StudentAchievementAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(DonatePage, DonatePageAdmin)
