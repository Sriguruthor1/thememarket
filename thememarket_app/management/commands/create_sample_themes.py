from django.core.management.base import BaseCommand
from thememarket_app.models import *
import random

class Command(BaseCommand):
    help = 'Create sample themes for testing'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample themes...')
        
        # Get categories
        categories = Category.objects.all()
        if not categories:
            self.stdout.write(self.style.ERROR('No categories found. Run setup_admin_data first.'))
            return
        
        # Sample theme data
        themes_data = [
            {
                'title': 'Flatsome - Multi-Purpose Responsive Theme',
                'description': 'A powerful and flexible WordPress theme perfect for any business or personal website. Features drag-and-drop page builder, WooCommerce integration, and responsive design.',
                'price': 59.00,
                'original_price': 89.00,
                'theme_type': 'wordpress',
                'is_featured': True,
                'is_popular': True,
                'rating': 4.8,
                'downloads': 205
            },
            {
                'title': 'Avada - Website Builder For WordPress',
                'description': 'The most popular WordPress theme with over 700,000 sales. Includes Fusion Builder, multiple demos, and extensive customization options.',
                'price': 69.00,
                'original_price': 99.00,
                'theme_type': 'wordpress',
                'is_featured': True,
                'rating': 4.9,
                'downloads': 156
            },
            {
                'title': 'Restaurant Website - Food & Drink Theme',
                'description': 'Perfect for restaurants, cafes, and food businesses. Features online menu, reservation system, and beautiful food gallery.',
                'price': 49.00,
                'theme_type': 'wordpress',
                'is_popular': True,
                'rating': 4.7,
                'downloads': 89
            },
            {
                'title': 'Business Pro - Corporate Theme',
                'description': 'Professional corporate theme for businesses and agencies. Clean design, portfolio showcase, and team member sections.',
                'price': 45.00,
                'theme_type': 'wordpress',
                'is_new': True,
                'rating': 4.6,
                'downloads': 312
            },
            {
                'title': 'Creative Studio - Agency Portfolio',
                'description': 'Modern portfolio theme for creative agencies and freelancers. Stunning animations and project showcase capabilities.',
                'price': 29.00,
                'theme_type': 'html',
                'is_featured': True,
                'rating': 4.8,
                'downloads': 198
            },
            {
                'title': 'ShopMaster - E-commerce Theme',
                'description': 'Complete e-commerce solution with product catalog, shopping cart, and payment integration. Mobile-optimized design.',
                'price': 39.00,
                'theme_type': 'wordpress',
                'is_popular': True,
                'rating': 4.7,
                'downloads': 267
            },
            {
                'title': 'Zenix - Modern Dashboard',
                'description': 'Professional admin dashboard template with charts, tables, and modern UI components. Perfect for web applications.',
                'price': 99.00,
                'theme_type': 'html',
                'is_new': True,
                'rating': 4.9,
                'downloads': 145
            },
            {
                'title': 'Blogify - Minimal Blog Theme',
                'description': 'Clean and minimal blog theme focused on readability and content. SEO optimized with social sharing features.',
                'price': 25.00,
                'theme_type': 'wordpress',
                'is_new': True,
                'rating': 4.5,
                'downloads': 178
            },
            {
                'title': 'TechStart - Technology Startup',
                'description': 'Modern theme for technology startups and SaaS companies. Features pricing tables, team sections, and product showcases.',
                'price': 55.00,
                'theme_type': 'html',
                'is_featured': True,
                'rating': 4.8,
                'downloads': 234
            },
            {
                'title': 'PhotoPro - Photography Portfolio',
                'description': 'Stunning photography portfolio theme with fullscreen galleries, lightbox effects, and client proofing features.',
                'price': 35.00,
                'theme_type': 'wordpress',
                'is_popular': True,
                'rating': 4.6,
                'downloads': 189
            }
        ]
        
        created_count = 0
        for theme_data in themes_data:
            # Get random category
            category = random.choice(categories)
            
            # Create slug from title
            slug = theme_data['title'].lower().replace(' ', '-').replace('--', '-')
            slug = ''.join(c for c in slug if c.isalnum() or c == '-')
            
            # Check if theme already exists
            if not Theme.objects.filter(slug=slug).exists():
                theme = Theme.objects.create(
                    title=theme_data['title'],
                    slug=slug,
                    description=theme_data['description'],
                    category=category,
                    theme_type=theme_data['theme_type'],
                    price=theme_data['price'],
                    original_price=theme_data.get('original_price'),
                    is_featured=theme_data.get('is_featured', False),
                    is_popular=theme_data.get('is_popular', False),
                    is_new=theme_data.get('is_new', False),
                    rating=theme_data['rating'],
                    downloads=theme_data['downloads']
                )
                created_count += 1
                self.stdout.write(f'Created theme: {theme.title}')
        
        # Create some testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'Web Developer',
                'company': 'TechCorp',
                'content': 'The quality of themes on this marketplace is outstanding. I\'ve built over 20 client sites using templates from here and they never disappoint.',
                'rating': 5,
                'is_featured': True
            },
            {
                'name': 'Michael Chen',
                'position': 'Agency Owner',
                'company': 'Creative Solutions',
                'content': 'As an agency, we rely on high-quality templates to deliver projects quickly. The variety and quality here are unmatched in the industry.',
                'rating': 5,
                'is_featured': True
            },
            {
                'name': 'Emily Rodriguez',
                'position': 'Freelance Designer',
                'company': 'Design Studio',
                'content': 'I love how easy it is to customize these themes. The documentation is excellent and the support from authors is fantastic.',
                'rating': 5,
                'is_featured': True
            }
        ]
        
        testimonial_count = 0
        for testimonial_data in testimonials_data:
            if not Testimonial.objects.filter(name=testimonial_data['name']).exists():
                Testimonial.objects.create(**testimonial_data)
                testimonial_count += 1
                self.stdout.write(f'Created testimonial: {testimonial_data["name"]}')
        
        self.stdout.write(self.style.SUCCESS(f'\nSample data created successfully!'))
        self.stdout.write(f'Created {created_count} themes')
        self.stdout.write(f'Created {testimonial_count} testimonials')
        self.stdout.write('\nVisit http://localhost:8000/ to see the themes in action!')