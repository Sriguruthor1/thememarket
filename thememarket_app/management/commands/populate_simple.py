from django.core.management.base import BaseCommand
from thememarket_app.models import (
    SiteSettings, NavigationMenu, HeroSection, HeroStats, Category, Theme,
    Page, FooterSection, FooterLink, SocialLink, Testimonial, ContactInfo
)

class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **options):
        self.stdout.write('Populating database with initial data...')

        # Site Settings
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_name': 'ThemeMarket',
                'site_tagline': 'Build Stunning Websites Faster',
                'logo_text': 'ThemeMarket',
                'primary_color': '#5c2dd5',
                'secondary_color': '#7b3fe4',
                'accent_color': '#4ade80',
            }
        )
        if created:
            self.stdout.write('+ Site settings created')

        # Navigation Menu
        nav_items = [
            {'title': 'Home', 'url': '/', 'order': 1},
            {'title': 'Themes', 'url': '/themes/', 'order': 2},
            {'title': 'Templates', 'url': '/template/', 'order': 3},
            {'title': 'About Us', 'url': '/about/', 'order': 4},
            {'title': 'Contact', 'url': '/contact/', 'order': 5},
        ]
        
        for item in nav_items:
            nav, created = NavigationMenu.objects.get_or_create(
                title=item['title'],
                defaults=item
            )
            if created:
                self.stdout.write(f'+ Navigation item "{item["title"]}" created')

        # Hero Section
        hero, created = HeroSection.objects.get_or_create(
            defaults={
                'badge_text': 'NEW',
                'main_title': 'Build Stunning Websites Faster',
                'highlighted_text': 'Faster',
                'description': 'Discover premium themes and templates for your next project. Choose from thousands of professional designs.',
                'search_placeholder': 'Search for themes, templates, plugins...',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Hero section created')
            
            # Hero Stats
            stats = [
                {'icon_class': 'fas fa-users', 'number': '50K+', 'label': 'Happy Customers', 'order': 1},
                {'icon_class': 'fas fa-download', 'number': '100K+', 'label': 'Downloads', 'order': 2},
                {'icon_class': 'fas fa-star', 'number': '4.9', 'label': 'Average Rating', 'order': 3},
            ]
            
            for stat in stats:
                HeroStats.objects.create(hero_section=hero, **stat)
            self.stdout.write('+ Hero stats created')

        # Categories
        categories = [
            {'name': 'WordPress Themes', 'slug': 'wordpress-themes', 'icon_class': 'fab fa-wordpress', 'is_featured': True, 'order': 1},
            {'name': 'HTML Templates', 'slug': 'html-templates', 'icon_class': 'fab fa-html5', 'is_featured': True, 'order': 2},
            {'name': 'UI Templates', 'slug': 'ui-templates', 'icon_class': 'fas fa-paint-brush', 'is_featured': True, 'order': 3},
            {'name': 'E-commerce', 'slug': 'ecommerce', 'icon_class': 'fas fa-shopping-cart', 'is_featured': True, 'order': 4},
            {'name': 'Business', 'slug': 'business', 'icon_class': 'fas fa-briefcase', 'is_featured': True, 'order': 5},
            {'name': 'Portfolio', 'slug': 'portfolio', 'icon_class': 'fas fa-folder-open', 'is_featured': True, 'order': 6},
        ]
        
        for cat_data in categories:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'+ Category "{cat_data["name"]}" created')

        # Sample Themes
        if Category.objects.exists():
            wordpress_cat = Category.objects.get(slug='wordpress-themes')
            html_cat = Category.objects.get(slug='html-templates')
            
            themes = [
                {
                    'title': 'Flatsome - Multi-Purpose WordPress Theme',
                    'slug': 'flatsome-wordpress-theme',
                    'description': 'Flatsome is the perfect theme for your shop or company website, or for all your client websites if you are an agency or freelancer.',
                    'category': wordpress_cat,
                    'theme_type': 'wordpress',
                    'price': 59.00,
                    'original_price': 99.00,
                    'is_featured': True,
                    'is_popular': True,
                    'rating': 4.8,
                    'downloads': 1250,
                },
                {
                    'title': 'Restaurant HTML Template',
                    'slug': 'restaurant-html-template',
                    'description': 'A beautiful and modern restaurant website template with booking system and menu showcase.',
                    'category': html_cat,
                    'theme_type': 'html',
                    'price': 29.00,
                    'is_new': True,
                    'rating': 4.6,
                    'downloads': 890,
                },
                {
                    'title': 'Avada - Responsive Multi-Purpose Theme',
                    'slug': 'avada-responsive-theme',
                    'description': 'Avada is the #1 selling WordPress theme on the market. Simply put, it is the most powerful theme available.',
                    'category': wordpress_cat,
                    'theme_type': 'wordpress',
                    'price': 69.00,
                    'is_featured': True,
                    'rating': 4.9,
                    'downloads': 2100,
                },
            ]
            
            for theme_data in themes:
                theme, created = Theme.objects.get_or_create(
                    slug=theme_data['slug'],
                    defaults=theme_data
                )
                if created:
                    self.stdout.write(f'+ Theme "{theme_data["title"]}" created')

        # Footer Sections
        footer_sections = [
            {
                'title': 'Products',
                'order': 1,
                'links': [
                    {'title': 'All Items', 'url': '/themes/', 'order': 1},
                    {'title': 'WordPress Themes', 'url': '/themes/?category=wordpress-themes', 'order': 2},
                    {'title': 'HTML Templates', 'url': '/themes/?category=html-templates', 'order': 3},
                    {'title': 'UI Templates', 'url': '/themes/?category=ui-templates', 'order': 4},
                    {'title': 'Plugins', 'url': '/themes/?type=plugin', 'order': 5},
                ]
            },
            {
                'title': 'Company',
                'order': 2,
                'links': [
                    {'title': 'About', 'url': '/about/', 'order': 1},
                    {'title': 'Careers', 'url': '#', 'order': 2},
                    {'title': 'Contact', 'url': '/contact/', 'order': 3},
                    {'title': 'Press', 'url': '#', 'order': 4},
                    {'title': 'Blog', 'url': '#', 'order': 5},
                ]
            },
            {
                'title': 'Support',
                'order': 3,
                'links': [
                    {'title': 'Help Center', 'url': '#', 'order': 1},
                    {'title': 'Documentation', 'url': '#', 'order': 2},
                    {'title': 'Forums', 'url': '#', 'order': 3},
                    {'title': 'Contact Support', 'url': '/contact/', 'order': 4},
                ]
            },
            {
                'title': 'Legal',
                'order': 4,
                'links': [
                    {'title': 'Terms of Service', 'url': '#', 'order': 1},
                    {'title': 'Privacy Policy', 'url': '#', 'order': 2},
                    {'title': 'License Agreement', 'url': '#', 'order': 3},
                ]
            },
        ]
        
        for section_data in footer_sections:
            links = section_data.pop('links')
            section, created = FooterSection.objects.get_or_create(
                title=section_data['title'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Footer section "{section_data["title"]}" created')
                
                for link_data in links:
                    FooterLink.objects.create(section=section, **link_data)

        # Social Links
        social_links = [
            {'platform': 'facebook', 'url': 'https://facebook.com/thememarket', 'icon_class': 'fab fa-facebook-f', 'order': 1},
            {'platform': 'instagram', 'url': 'https://instagram.com/thememarket', 'icon_class': 'fab fa-instagram', 'order': 2},
            {'platform': 'twitter', 'url': 'https://twitter.com/thememarket', 'icon_class': 'fab fa-twitter', 'order': 3},
            {'platform': 'linkedin', 'url': 'https://linkedin.com/company/thememarket', 'icon_class': 'fab fa-linkedin-in', 'order': 4},
        ]
        
        for social_data in social_links:
            social, created = SocialLink.objects.get_or_create(
                platform=social_data['platform'],
                defaults=social_data
            )
            if created:
                self.stdout.write(f'+ Social link "{social_data["platform"]}" created')

        # Contact Info
        contact_info, created = ContactInfo.objects.get_or_create(
            defaults={
                'email': 'support@thememarket.com',
                'phone': '+1 (555) 123-4567',
                'address': '123 Design Street, Creative City, CC 12345',
                'working_hours': 'Monday - Friday: 9:00 AM - 6:00 PM (EST)',
            }
        )
        if created:
            self.stdout.write('+ Contact information created')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
        self.stdout.write('You can now access the admin panel at http://127.0.0.1:8000/admin/')