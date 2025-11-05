from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import os
from thememarket_app.models import (
    NavigationMenu,
    HeroBanner,
    CategorySection,
    FeaturedSection,
    PopularSection,
    NewSection,
    WhyChooseSection,
    FeatureCard,
    NewsletterSection,
    TestimonialsSection,
    CustomerTestimonial,
    FooterSection,
    FooterLink,
    SocialLink,
)

class Command(BaseCommand):
    help = 'Populates the database from HTML files'

    def handle(self, *args, **options):
        self.stdout.write('Starting database population from HTML files...')
        
        # Path to the templates directory
        # Path to the templates directory. The command is run from `thememarket_project`,
        # so os.getcwd() is the correct base.
        template_dir = os.path.join(os.getcwd(), 'templates')
        
        # Populate from home.html
        home_html_path = os.path.join(template_dir, 'home.html')
        if os.path.exists(home_html_path):
            with open(home_html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                self.populate_home_page(soup, template_dir)
        else:
            self.stdout.write(self.style.WARNING(f'File not found: {home_html_path}'))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))

    def populate_home_page(self, soup, template_dir):
        self.stdout.write('Populating home page content...')

        # Populate HeroBanner
        hero_section = soup.find('section', class_='hero-banner')
        if hero_section:
            main_title = hero_section.find('h1').text.strip()
            subtitle = hero_section.find('p').text.strip()
            HeroBanner.objects.get_or_create(
                main_title=main_title,
                subtitle=subtitle,
                defaults={'is_active': True}
            )
            self.stdout.write(self.style.SUCCESS('HeroBanner populated.'))
        else:
            self.stdout.write(self.style.WARNING('HeroBanner section not found.'))

        # Populate NavigationMenu from base.html
        base_html_path = os.path.join(template_dir, 'base.html')
        if os.path.exists(base_html_path):
            with open(base_html_path, 'r', encoding='utf-8') as f:
                base_soup = BeautifulSoup(f.read(), 'html.parser')
                nav_menu = base_soup.find('nav')
                if nav_menu:
                    for i, link in enumerate(nav_menu.find_all('a')):
                        NavigationMenu.objects.get_or_create(
                            title=link.text.strip(),
                            url=link['href'],
                            defaults={'order': i, 'is_active': True}
                        )
                    self.stdout.write(self.style.SUCCESS('NavigationMenu populated.'))
                else:
                    self.stdout.write(self.style.WARNING('NavigationMenu not found in base.html.'))
        else:
            self.stdout.write(self.style.WARNING(f'File not found: {base_html_path}'))