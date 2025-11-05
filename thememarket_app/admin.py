from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .admin_groups import admin_site
from .models import (
    SiteSettings, NavigationMenu, HeroSection, HeroStats, Category, Theme, ThemeImage,
    Page, FooterSection, FooterLink, SocialLink, Testimonial, ContactInfo,
    # Home Page Models
    HeroBanner, HeroImage, CategorySection, FeaturedSection, PopularSection, NewSection,
    WhyChooseSection, FeatureCard, NewsletterSection, TestimonialsSection, CustomerTestimonial,
    # About Page Models
    AboutHero, AboutMission, AboutValues, ValueItem, AboutTeam, TeamMember,
    # Contact Page Models
    ContactHero, ContactForm, ContactOffice,
    # Themes Page Models
    ThemesHero, ThemesFilter, ThemesGrid,
    # Templates Page Models
    TemplatesHero, HTMLTemplatesSection, UITemplatesSection,
    # Other Page Models
    LoginPageContent, CartPageContent, CheckoutPageContent, PaymentPageContent, PaymentSuccessPageContent
)

class SiteSettingsAdmin(ModelAdmin):
    list_display = ['site_name', 'site_tagline']
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_tagline', 'logo_text')
        }),
        ('Colors', {
            'fields': ('primary_color', 'secondary_color', 'accent_color')
        }),
    )
    
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
admin_site.register(SiteSettings, SiteSettingsAdmin)

class NavigationMenuAdmin(ModelAdmin):
    list_display = ['title', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']
admin_site.register(NavigationMenu, NavigationMenuAdmin)

class HeroStatsInline(TabularInline):
    model = HeroStats
    extra = 1
    fields = ['icon_class', 'number', 'label', 'order']

class HeroSectionAdmin(ModelAdmin):
    list_display = ['main_title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('badge_text', 'main_title', 'highlighted_text', 'description')
        }),
        ('Search', {
            'fields': ('search_placeholder',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    inlines = [HeroStatsInline]
    
    def has_add_permission(self, request):
        return not HeroSection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
admin_site.register(HeroSection, HeroSectionAdmin)

class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug', 'icon_class', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    list_filter = ['is_featured']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order']
    search_fields = ['name', 'description']
admin_site.register(Category, CategoryAdmin)

class ThemeImageInline(TabularInline):
    model = ThemeImage
    extra = 1
    fields = ['image', 'alt_text', 'is_primary', 'order']

class ThemeAdmin(ModelAdmin):
    list_display = ['title', 'category', 'theme_type', 'price', 'is_featured', 'is_popular', 'is_new', 'rating', 'downloads']
    list_editable = ['is_featured', 'is_popular', 'is_new', 'price']
    list_filter = ['category', 'theme_type', 'is_featured', 'is_popular', 'is_new', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']
    inlines = [ThemeImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category', 'theme_type')
        }),
        ('Pricing', {
            'fields': ('price', 'original_price')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('URLs', {
            'fields': ('preview_url', 'download_url')
        }),
        ('Status & Features', {
            'fields': ('is_featured', 'is_popular', 'is_new')
        }),
        ('Statistics', {
            'fields': ('rating', 'downloads')
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['created_at', 'updated_at']
        return []
admin_site.register(Theme, ThemeAdmin)

class PageAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at', 'updated_at']
    list_editable = ['is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'content')
        }),
        ('SEO', {
            'fields': ('meta_description',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(Page, PageAdmin)

class FooterLinkInline(TabularInline):
    model = FooterLink
    extra = 1
    fields = ['title', 'url', 'order', 'is_active']

class FooterSectionAdmin(ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    ordering = ['order']
    inlines = [FooterLinkInline]
admin_site.register(FooterSection, FooterSectionAdmin)

class SocialLinkAdmin(ModelAdmin):
    list_display = ['platform', 'url', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['platform', 'is_active']
    ordering = ['order']
admin_site.register(SocialLink, SocialLinkAdmin)

class TestimonialAdmin(ModelAdmin):
    list_display = ['name', 'company', 'rating', 'is_featured', 'order']
    list_editable = ['is_featured', 'order', 'rating']
    list_filter = ['rating', 'is_featured']
    search_fields = ['name', 'company', 'content']
    ordering = ['order']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'company', 'avatar')
        }),
        ('Testimonial', {
            'fields': ('content', 'rating')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        }),
    )
admin_site.register(Testimonial, TestimonialAdmin)

class ContactInfoAdmin(ModelAdmin):
    list_display = ['email', 'phone']
    fieldsets = (
        ('Contact Details', {
            'fields': ('email', 'phone')
        }),
        ('Address & Hours', {
            'fields': ('address', 'working_hours')
        }),
    )
    
    def has_add_permission(self, request):
        return not ContactInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
admin_site.register(ContactInfo, ContactInfoAdmin)

# HOME PAGE ADMIN
class HeroImageInline(TabularInline):
    model = HeroImage
    extra = 1
    fields = ['image', 'title', 'category', 'is_large', 'order']

class HeroBannerAdmin(ModelAdmin):
    list_display = ['main_title', 'is_active']
    inlines = [HeroImageInline]
    fieldsets = (
        ('Content', {
            'fields': ('badge_text', 'main_title', 'highlighted_word', 'subtitle')
        }),
        ('Search', {
            'fields': ('search_placeholder',)
        }),
        ('Media', {
            'fields': ('background_image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(HeroBanner, HeroBannerAdmin)

class CategorySectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(CategorySection, CategorySectionAdmin)

class FeaturedSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(FeaturedSection, FeaturedSectionAdmin)

class PopularSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(PopularSection, PopularSectionAdmin)

class NewSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(NewSection, NewSectionAdmin)

class FeatureCardInline(TabularInline):
    model = FeatureCard
    extra = 1
    fields = ['icon_class', 'title', 'description', 'background_color', 'icon_color', 'order']

class WhyChooseSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    inlines = [FeatureCardInline]
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(WhyChooseSection, WhyChooseSectionAdmin)

class NewsletterSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Form', {
            'fields': ('email_placeholder', 'button_text')
        }),
        ('Privacy', {
            'fields': ('privacy_text',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(NewsletterSection, NewsletterSectionAdmin)

class CustomerTestimonialInline(TabularInline):
    model = CustomerTestimonial
    extra = 1
    fields = ['name', 'position', 'avatar', 'rating', 'content', 'order']

class TestimonialsSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    inlines = [CustomerTestimonialInline]
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(TestimonialsSection, TestimonialsSectionAdmin)

# ABOUT PAGE ADMIN
class AboutHeroAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Media', {
            'fields': ('background_image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(AboutHero, AboutHeroAdmin)

class AboutMissionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'content')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(AboutMission, AboutMissionAdmin)

class ValueItemInline(TabularInline):
    model = ValueItem
    extra = 1
    fields = ['title', 'description', 'icon_class', 'order']

class AboutValuesAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    inlines = [ValueItemInline]
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(AboutValues, AboutValuesAdmin)

class TeamMemberInline(TabularInline):
    model = TeamMember
    extra = 1
    fields = ['name', 'position', 'photo', 'bio', 'email', 'order']

class AboutTeamAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    inlines = [TeamMemberInline]
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(AboutTeam, AboutTeamAdmin)

# CONTACT PAGE ADMIN
class ContactHeroAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Media', {
            'fields': ('background_image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(ContactHero, ContactHeroAdmin)

class ContactFormAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle')
        }),
        ('Form Fields', {
            'fields': ('name_placeholder', 'email_placeholder', 'subject_placeholder', 'message_placeholder', 'button_text')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(ContactForm, ContactFormAdmin)

class ContactOfficeAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'content', 'is_active']
admin_site.register(ContactOffice, ContactOfficeAdmin)

# THEMES PAGE ADMIN
class ThemesHeroAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Media', {
            'fields': ('background_image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(ThemesHero, ThemesHeroAdmin)

class ThemesFilterAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'is_active']
admin_site.register(ThemesFilter, ThemesFilterAdmin)

class ThemesGridAdmin(ModelAdmin):
    list_display = ['title', 'items_per_page', 'is_active']
    fields = ['title', 'subtitle', 'items_per_page', 'is_active']
admin_site.register(ThemesGrid, ThemesGridAdmin)

# TEMPLATES PAGE ADMIN
class TemplatesHeroAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description')
        }),
        ('Media', {
            'fields': ('background_image',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
admin_site.register(TemplatesHero, TemplatesHeroAdmin)

class HTMLTemplatesSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'description', 'is_active']
admin_site.register(HTMLTemplatesSection, HTMLTemplatesSectionAdmin)

class UITemplatesSectionAdmin(ModelAdmin):
    list_display = ['title', 'is_active']
    fields = ['title', 'subtitle', 'description', 'is_active']
admin_site.register(UITemplatesSection, UITemplatesSectionAdmin)

class LoginPageContentAdmin(ModelAdmin):
    list_display = ['section_type', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['section_type', 'is_active']
    ordering = ['order']
admin_site.register(LoginPageContent, LoginPageContentAdmin)

class CartPageContentAdmin(ModelAdmin):
    list_display = ['section_type', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['section_type', 'is_active']
    ordering = ['order']
admin_site.register(CartPageContent, CartPageContentAdmin)

class CheckoutPageContentAdmin(ModelAdmin):
    list_display = ['section_type', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['section_type', 'is_active']
    ordering = ['order']
admin_site.register(CheckoutPageContent, CheckoutPageContentAdmin)

class PaymentPageContentAdmin(ModelAdmin):
    list_display = ['section_type', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['section_type', 'is_active']
    ordering = ['order']
admin_site.register(PaymentPageContent, PaymentPageContentAdmin)

class PaymentSuccessPageContentAdmin(ModelAdmin):
    list_display = ['section_type', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter = ['section_type', 'is_active']
    ordering = ['order']
admin_site.register(PaymentSuccessPageContent, PaymentSuccessPageContentAdmin)