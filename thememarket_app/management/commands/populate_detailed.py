from django.core.management.base import BaseCommand
from thememarket_app.models import *

class Command(BaseCommand):
    help = 'Populate all detailed page content'

    def handle(self, *args, **options):
        self.stdout.write('Populating detailed page content...')

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

        # HOME PAGE
        # Hero Banner
        hero_banner, created = HeroBanner.objects.get_or_create(
            defaults={
                'badge_text': 'NEW',
                'main_title': 'Build Stunning Websites Faster',
                'highlighted_word': 'Faster',
                'subtitle': 'Discover premium themes and templates for your next project. Choose from thousands of professional designs.',
                'search_placeholder': 'Search for themes, templates, plugins...',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Hero banner created')

        # Category Section
        category_section, created = CategorySection.objects.get_or_create(
            defaults={
                'title': 'Browse by Category',
                'subtitle': 'Find the perfect theme for your project',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Category section created')

        # Featured Section
        featured_section, created = FeaturedSection.objects.get_or_create(
            defaults={
                'title': 'Featured Themes',
                'subtitle': 'Hand-picked themes by our team',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Featured section created')

        # Popular Section
        popular_section, created = PopularSection.objects.get_or_create(
            defaults={
                'title': 'Popular Themes',
                'subtitle': 'Most downloaded themes',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Popular section created')

        # New Section
        new_section, created = NewSection.objects.get_or_create(
            defaults={
                'title': 'New Themes',
                'subtitle': 'Latest additions to our collection',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ New section created')

        # Why Choose Section with Features
        why_choose, created = WhyChooseSection.objects.get_or_create(
            defaults={
                'title': 'Why Choose ThemeMarket?',
                'subtitle': 'Everything you need to build amazing websites',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Why choose section created')
            
            features = [
                {'icon_class': 'fas fa-headset', 'title': '24/7 Support', 'description': 'Our dedicated support team is here to help you anytime', 'order': 1},
                {'icon_class': 'fas fa-sync-alt', 'title': 'Regular Updates', 'description': 'Authors constantly update items with new features and fixes', 'order': 2},
                {'icon_class': 'fas fa-award', 'title': 'Elite Authors', 'description': 'Work with the best designers and developers in the industry', 'order': 3},
                {'icon_class': 'fas fa-dollar-sign', 'title': 'Great Value', 'description': 'Competitive pricing with frequent sales and special offers', 'order': 4},
            ]
            
            for feature_data in features:
                FeatureCard.objects.create(section=why_choose, **feature_data)

        # Newsletter Section
        newsletter, created = NewsletterSection.objects.get_or_create(
            defaults={
                'title': 'Stay Updated',
                'subtitle': 'Get the latest themes, exclusive deals, and design inspiration delivered to your inbox weekly',
                'email_placeholder': 'Enter your email',
                'button_text': 'Subscribe',
                'privacy_text': 'By subscribing, you agree to our Privacy Policy and consent to receive updates',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Newsletter section created')

        # Testimonials Section
        testimonials_section, created = TestimonialsSection.objects.get_or_create(
            defaults={
                'title': 'What Our Customers Say',
                'subtitle': 'Join thousands of satisfied customers',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Testimonials section created')

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

        # ABOUT PAGE
        about_hero, created = AboutHero.objects.get_or_create(
            defaults={
                'title': 'About ThemeMarket',
                'subtitle': 'Your premier destination for high-quality website themes and templates',
                'description': 'We have been serving the web development community since 2020, providing professional designs that help businesses and individuals create stunning websites.',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ About hero created')

        about_mission, created = AboutMission.objects.get_or_create(
            defaults={
                'title': 'Our Mission',
                'subtitle': 'Democratizing web design',
                'content': 'To democratize web design by making professional, high-quality themes and templates accessible to everyone, regardless of their technical expertise.',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ About mission created')

        # CONTACT PAGE
        contact_hero, created = ContactHero.objects.get_or_create(
            defaults={
                'title': 'Get in Touch',
                'subtitle': 'Have questions about our themes or need support? We are here to help!',
                'description': 'Reach out to us using the contact information below or send us a message.',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Contact hero created')

        contact_form, created = ContactForm.objects.get_or_create(
            defaults={
                'title': 'Send us a Message',
                'subtitle': 'We will get back to you within 24 hours',
                'name_placeholder': 'Your Name',
                'email_placeholder': 'Your Email',
                'subject_placeholder': 'Subject',
                'message_placeholder': 'Your Message',
                'button_text': 'Send Message',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Contact form created')

        # THEMES PAGE
        themes_hero, created = ThemesHero.objects.get_or_create(
            defaults={
                'title': 'Browse Themes',
                'subtitle': 'Discover thousands of professional themes and templates',
                'description': 'Find the perfect theme for your next project from our curated collection.',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Themes hero created')

        # TEMPLATES PAGE
        templates_hero, created = TemplatesHero.objects.get_or_create(
            defaults={
                'title': 'HTML & UI Templates',
                'subtitle': 'Ready-to-use templates for modern websites',
                'description': 'Choose from our collection of HTML and UI templates.',
                'is_active': True,
            }
        )
        if created:
            self.stdout.write('+ Templates hero created')

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

        self.stdout.write(self.style.SUCCESS('All detailed content populated successfully!'))