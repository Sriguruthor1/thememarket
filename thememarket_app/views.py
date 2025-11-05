from django.shortcuts import render, get_object_or_404
from .models import (
    SiteSettings, NavigationMenu, HeroSection, Category, Theme, 
    Page, FooterSection, SocialLink, Testimonial, ContactInfo,
    # Home Page Models
    HeroBanner, CategorySection, FeaturedSection, PopularSection, NewSection,
    WhyChooseSection, NewsletterSection, TestimonialsSection,
    # About Page Models
    AboutHero, AboutMission, AboutValues, AboutTeam,
    # Contact Page Models
    ContactHero, ContactForm, ContactOffice,
    # Themes Page Models
    ThemesHero, ThemesFilter, ThemesGrid,
    # Templates Page Models
    TemplatesHero, HTMLTemplatesSection, UITemplatesSection,
    # Other Page Models
    LoginPageContent, CartPageContent, CheckoutPageContent, PaymentPageContent, PaymentSuccessPageContent
)

def get_common_context():
    """Get common context data for all views"""
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None
    
    return {
        'site_settings': site_settings,
        'navigation_menus': NavigationMenu.objects.filter(is_active=True),
        'footer_sections': FooterSection.objects.prefetch_related('links'),
        'social_links': SocialLink.objects.filter(is_active=True),
    }

def home(request):
    context = get_common_context()
    context.update({
        'hero_banner': HeroBanner.objects.filter(is_active=True).first(),
        'category_section': CategorySection.objects.filter(is_active=True).first(),
        'featured_section': FeaturedSection.objects.filter(is_active=True).first(),
        'popular_section': PopularSection.objects.filter(is_active=True).first(),
        'new_section': NewSection.objects.filter(is_active=True).first(),
        'why_choose_section': WhyChooseSection.objects.filter(is_active=True).prefetch_related('features').first(),
        'newsletter_section': NewsletterSection.objects.filter(is_active=True).first(),
        'testimonials_section': TestimonialsSection.objects.filter(is_active=True).prefetch_related('testimonials').first(),
        'categories': Category.objects.filter(is_featured=True)[:8],
        'featured_themes': Theme.objects.filter(is_featured=True)[:9],
        'popular_themes': Theme.objects.filter(is_popular=True)[:9],
        'new_themes': Theme.objects.filter(is_new=True)[:9],
    })
    return render(request, 'home.html', context)

def about(request):
    context = get_common_context()
    context.update({
        'about_hero': AboutHero.objects.filter(is_active=True).first(),
        'about_mission': AboutMission.objects.filter(is_active=True).first(),
        'about_values': AboutValues.objects.filter(is_active=True).prefetch_related('values').first(),
        'about_team': AboutTeam.objects.filter(is_active=True).prefetch_related('members').first(),
    })
    return render(request, 'about.html', context)

def contact(request):
    context = get_common_context()
    context.update({
        'contact_hero': ContactHero.objects.filter(is_active=True).first(),
        'contact_form': ContactForm.objects.filter(is_active=True).first(),
        'contact_office': ContactOffice.objects.filter(is_active=True).first(),
        'contact_info': ContactInfo.objects.first(),
    })
    return render(request, 'contact.html', context)

def themes(request):
    context = get_common_context()
    category_slug = request.GET.get('category')
    theme_type = request.GET.get('type')
    
    themes_queryset = Theme.objects.all()
    
    if category_slug:
        themes_queryset = themes_queryset.filter(category__slug=category_slug)
    
    if theme_type:
        themes_queryset = themes_queryset.filter(theme_type=theme_type)
    
    themes_grid = ThemesGrid.objects.filter(is_active=True).first()
    items_per_page = themes_grid.items_per_page if themes_grid else 20
    
    context.update({
        'themes_hero': ThemesHero.objects.filter(is_active=True).first(),
        'themes_filter': ThemesFilter.objects.filter(is_active=True).first(),
        'themes_grid': themes_grid,
        'themes': themes_queryset[:items_per_page],
        'categories': Category.objects.all(),
        'selected_category': category_slug,
        'selected_type': theme_type,
    })
    return render(request, 'themes.html', context)

def template_page(request):
    context = get_common_context()
    context.update({
        'templates_hero': TemplatesHero.objects.filter(is_active=True).first(),
        'html_templates_section': HTMLTemplatesSection.objects.filter(is_active=True).first(),
        'ui_templates_section': UITemplatesSection.objects.filter(is_active=True).first(),
        'html_templates': Theme.objects.filter(theme_type='html')[:12],
        'ui_templates': Theme.objects.filter(theme_type='ui')[:12],
    })
    return render(request, 'template.html', context)

def login_page(request):
    context = get_common_context()
    context.update({
        'login_contents': LoginPageContent.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'login.html', context)

def cart(request):
    context = get_common_context()
    context.update({
        'cart_contents': CartPageContent.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'cart.html', context)

def checkout(request):
    context = get_common_context()
    context.update({
        'checkout_contents': CheckoutPageContent.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'checkout.html', context)

def payment(request):
    context = get_common_context()
    context.update({
        'payment_contents': PaymentPageContent.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'payment.html', context)

def payment_success(request):
    context = get_common_context()
    context.update({
        'payment_success_contents': PaymentSuccessPageContent.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'payment_success.html', context)