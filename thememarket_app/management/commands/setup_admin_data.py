from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from thememarket_app.models import *

class Command(BaseCommand):
    help = 'Setup initial admin data for the website'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial admin data...')
        
        # Create Site Settings
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
            self.stdout.write(self.style.SUCCESS('Site Settings created'))
        
        # Create Navigation Menu
        nav_items = [
            ('Home', '/', 1),
            ('Themes', '/themes/', 2),
            ('Templates', '/template/', 3),
            ('About Us', '/about/', 4),
            ('Contact', '/contact/', 5),
        ]
        
        for title, url, order in nav_items:
            nav, created = NavigationMenu.objects.get_or_create(
                title=title,
                defaults={'url': url, 'order': order, 'is_active': True}
            )
            if created:
                self.stdout.write(f'Navigation item "{title}" created')
        
        # Create Hero Banner
        hero_banner, created = HeroBanner.objects.get_or_create(
            defaults={
                'badge_text': '50,000+ Premium Templates Available',
                'main_title': 'Build Stunning Websites Faster',
                'highlighted_word': 'Faster',
                'subtitle': 'Access thousands of professionally designed WordPress themes and templates. Launch your dream website in minutes, not months.',
                'search_placeholder': 'Search for WordPress, E-commerce....',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Hero Banner created'))
        
        # Create Categories
        categories_data = [
            ('WordPress', 'wordpress', 'fab fa-wordpress', '#1e90ff', True),
            ('E-commerce', 'ecommerce', 'fas fa-shopping-cart', '#00bcd4', True),
            ('Photography', 'photography', 'fas fa-camera', '#7b3fe4', True),
            ('Business', 'business', 'fas fa-briefcase', '#8bc34a', True),
            ('Blog & Magazine', 'blog', 'fas fa-newspaper', '#e91e63', True),
            ('Mobile Apps', 'mobile', 'fas fa-mobile-alt', '#ff5722', True),
            ('Marketing', 'marketing', 'fas fa-bullhorn', '#daa520', True),
            ('Technology', 'tech', 'fas fa-microchip', '#2196f3', True),
        ]
        
        for name, slug, icon, color, is_featured in categories_data:
            category, created = Category.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'icon_class': icon,
                    'color': color,
                    'is_featured': is_featured,
                    'description': f'Professional {name.lower()} themes and templates'
                }
            )
            if created:
                self.stdout.write(f'Category "{name}" created')
        
        # Create Section Headers
        sections_data = [
            (CategorySection, {'title': 'Browse by Category', 'subtitle': 'Find the perfect template for your project'}),
            (FeaturedSection, {'title': 'Featured WordPress Themes', 'subtitle': 'Every week, our staff personally hand-pick some of the best new website themes from our collection.'}),
            (PopularSection, {'title': 'Popular Themes', 'subtitle': 'Most downloaded themes'}),
            (NewSection, {'title': 'New Arrivals', 'subtitle': 'Fresh templates added this week'}),
            (WhyChooseSection, {'title': 'Why Choose Our Marketplace', 'subtitle': 'Everything you need to build amazing websites'}),
            (NewsletterSection, {'title': 'Stay Updated', 'subtitle': 'Get the latest themes, exclusive deals, and design inspiration delivered to your inbox weekly'}),
            (TestimonialsSection, {'title': 'What Our Customers Say', 'subtitle': 'Join thousands of satisfied customers'}),
        ]
        
        for model_class, data in sections_data:
            obj, created = model_class.objects.get_or_create(defaults=data)
            if created:
                self.stdout.write(f'{model_class.__name__} created')
        
        # Create Why Choose Features
        why_choose = WhyChooseSection.objects.first()
        if why_choose:
            features_data = [
                ('Quality Guaranteed', 'All items are reviewed by our team to ensure the highest standards', 'fas fa-shield-alt', '#e3f7e3', '#2ecc71'),
                ('Instant Downloads', 'Get immediate access to your purchases, no waiting required', 'fas fa-download', '#e3f7e3', '#2ecc71'),
                ('24/7 Support', 'Our dedicated support team is here to help you anytime', 'fas fa-headset', '#e3f7e3', '#2ecc71'),
                ('Regular Updates', 'Authors constantly update items with new features and fixes', 'fas fa-sync-alt', '#e3f7e3', '#2ecc71'),
                ('Elite Authors', 'Work with the best designers and developers in the industry', 'fas fa-award', '#e3f7e3', '#2ecc71'),
                ('Great Value', 'Competitive pricing with frequent sales and special offers', 'fas fa-dollar-sign', '#e3f7e3', '#2ecc71'),
            ]
            
            for i, (title, desc, icon, bg_color, icon_color) in enumerate(features_data):
                feature, created = FeatureCard.objects.get_or_create(
                    section=why_choose,
                    title=title,
                    defaults={
                        'description': desc,
                        'icon_class': icon,
                        'background_color': bg_color,
                        'icon_color': icon_color,
                        'order': i
                    }
                )
                if created:
                    self.stdout.write(f'Feature "{title}" created')
        
        # Create Footer Sections
        footer_data = [
            ('Products', [
                ('All Items', '#'),
                ('WordPress Themes', '/themes/?type=wordpress'),
                ('HTML Templates', '/template/'),
                ('UI Templates', '/template/'),
                ('Plugins', '#'),
            ]),
            ('Company', [
                ('About', '/about/'),
                ('Careers', '#'),
                ('Contact', '/contact/'),
                ('Press', '#'),
                ('Blog', '#'),
            ]),
            ('Support', [
                ('Help Center', '#'),
                ('Documentation', '#'),
                ('Forums', '#'),
                ('Contact Support', '/contact/'),
            ]),
            ('Legal', [
                ('Terms of Service', '#'),
                ('Privacy Policy', '#'),
                ('License Agreement', '#'),
            ]),
        ]
        
        for section_title, links in footer_data:
            footer_section, created = FooterSection.objects.get_or_create(
                title=section_title,
                defaults={'order': len(footer_data)}
            )
            if created:
                self.stdout.write(f'Footer section "{section_title}" created')
            
            for i, (link_title, url) in enumerate(links):
                link, created = FooterLink.objects.get_or_create(
                    section=footer_section,
                    title=link_title,
                    defaults={'url': url, 'order': i, 'is_active': True}
                )
                if created:
                    self.stdout.write(f'  Footer link "{link_title}" created')
        
        # Create Social Links
        social_data = [
            ('facebook', 'https://facebook.com', 'fab fa-facebook-f'),
            ('instagram', 'https://instagram.com', 'fab fa-instagram'),
            ('twitter', 'https://twitter.com', 'fab fa-twitter'),
            ('linkedin', 'https://linkedin.com', 'fab fa-linkedin-in'),
        ]
        
        for i, (platform, url, icon) in enumerate(social_data):
            social, created = SocialLink.objects.get_or_create(
                platform=platform,
                defaults={'url': url, 'icon_class': icon, 'order': i, 'is_active': True}
            )
            if created:
                self.stdout.write(f'Social link "{platform}" created')
        
        # Create Contact Info
        contact_info, created = ContactInfo.objects.get_or_create(
            defaults={
                'email': 'support@thememarket.com',
                'phone': '+1 (555) 123-4567',
                'address': '123 Design Street, Creative City, CC 12345',
                'working_hours': 'Monday - Friday: 9:00 AM - 6:00 PM EST'
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Contact Info created'))
        
        # Create About Page Content
        about_hero, created = AboutHero.objects.get_or_create(
            defaults={
                'title': 'About ThemeMarket',
                'subtitle': 'Your premier destination for high-quality website themes and templates',
                'description': 'We are passionate about helping creators, businesses, and developers build stunning websites with ease. Our marketplace features thousands of professionally designed themes and templates.',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('About Hero created'))
        
        about_mission, created = AboutMission.objects.get_or_create(
            defaults={
                'title': 'Our Mission',
                'subtitle': 'Democratizing web design',
                'content': 'We believe that everyone should have access to beautiful, professional website designs. Our mission is to bridge the gap between high-quality design and affordability, making it possible for anyone to create stunning websites.',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('About Mission created'))
        
        # Create Contact Page Content
        contact_hero, created = ContactHero.objects.get_or_create(
            defaults={
                'title': 'Get in Touch',
                'subtitle': 'Have questions about our themes or need support? We are here to help!',
                'description': 'Our dedicated support team is available to assist you with any questions, technical issues, or guidance you may need.',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Contact Hero created'))
        
        contact_form, created = ContactForm.objects.get_or_create(
            defaults={
                'title': 'Send us a Message',
                'subtitle': 'We\'ll get back to you within 24 hours',
                'name_placeholder': 'Your Name',
                'email_placeholder': 'Your Email',
                'subject_placeholder': 'Subject',
                'message_placeholder': 'Your Message',
                'button_text': 'Send Message',
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Contact Form created'))
        
        self.stdout.write(self.style.SUCCESS('\nInitial admin data setup complete!'))
        self.stdout.write(self.style.WARNING('\nNext steps:'))
        self.stdout.write('1. Run: python manage.py runserver')
        self.stdout.write('2. Access admin at: http://localhost:8000/admin/')
        self.stdout.write('3. Login with: admin (no password set)')
        self.stdout.write('4. Visit website: http://localhost:8000/')