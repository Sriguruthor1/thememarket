from django.core.management.base import BaseCommand
from thememarket_app.models import (
    HomePageSection, FeatureItem, AboutPageContent, TeamMember, ContactPageContent,
    ThemesPageContent, TemplatePageContent, LoginPageContent, CartPageContent,
    CheckoutPageContent, PaymentPageContent, PaymentSuccessPageContent
)

class Command(BaseCommand):
    help = 'Populate all page-specific content'

    def handle(self, *args, **options):
        self.stdout.write('Populating page-specific content...')

        # Home Page Sections
        home_sections = [
            {
                'section_type': 'features',
                'title': 'Why Choose ThemeMarket?',
                'subtitle': 'Everything you need to build amazing websites',
                'content': 'We provide the best themes and templates with premium support.',
                'order': 1,
                'features': [
                    {'icon_class': 'fas fa-headset', 'title': '24/7 Support', 'description': 'Our dedicated support team is here to help you anytime', 'color': '#2ecc71', 'order': 1},
                    {'icon_class': 'fas fa-sync-alt', 'title': 'Regular Updates', 'description': 'Authors constantly update items with new features and fixes', 'color': '#2ecc71', 'order': 2},
                    {'icon_class': 'fas fa-award', 'title': 'Elite Authors', 'description': 'Work with the best designers and developers in the industry', 'color': '#2ecc71', 'order': 3},
                    {'icon_class': 'fas fa-dollar-sign', 'title': 'Great Value', 'description': 'Competitive pricing with frequent sales and special offers', 'color': '#2ecc71', 'order': 4},
                ]
            },
            {
                'section_type': 'newsletter',
                'title': 'Stay Updated',
                'subtitle': 'Get the latest themes, exclusive deals, and design inspiration delivered to your inbox weekly',
                'content': 'By subscribing, you agree to our Privacy Policy and consent to receive updates',
                'order': 2,
            },
            {
                'section_type': 'testimonials',
                'title': 'What Our Customers Say',
                'subtitle': 'Join thousands of satisfied customers',
                'content': '',
                'order': 3,
            },
        ]

        for section_data in home_sections:
            features = section_data.pop('features', [])
            section, created = HomePageSection.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Home section "{section_data["title"]}" created')
                
                for feature_data in features:
                    FeatureItem.objects.create(section=section, **feature_data)

        # About Page Sections
        about_sections = [
            {
                'section_type': 'hero',
                'title': 'About ThemeMarket',
                'subtitle': 'Your premier destination for high-quality website themes and templates',
                'content': 'We have been serving the web development community since 2020, providing professional designs that help businesses and individuals create stunning websites.',
                'order': 1,
            },
            {
                'section_type': 'mission',
                'title': 'Our Mission',
                'subtitle': 'Democratizing web design',
                'content': 'To democratize web design by making professional, high-quality themes and templates accessible to everyone, regardless of their technical expertise.',
                'order': 2,
            },
            {
                'section_type': 'values',
                'title': 'Why Choose Us?',
                'subtitle': 'What sets us apart',
                'content': '<ul><li>Premium quality designs</li><li>Regular updates and support</li><li>Easy customization</li><li>Responsive designs</li><li>SEO optimized</li></ul>',
                'order': 3,
            },
        ]

        for section_data in about_sections:
            section, created = AboutPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ About section "{section_data["title"]}" created')

        # Contact Page Sections
        contact_sections = [
            {
                'section_type': 'hero',
                'title': 'Get in Touch',
                'subtitle': 'Have questions about our themes or need support? We are here to help!',
                'content': 'Reach out to us using the contact information below or send us a message.',
                'order': 1,
            },
            {
                'section_type': 'office_info',
                'title': 'Support Hours',
                'subtitle': 'When we are available',
                'content': 'Monday - Friday: 9:00 AM - 6:00 PM (EST)<br>Saturday: 10:00 AM - 4:00 PM (EST)<br>Sunday: Closed',
                'order': 2,
            },
        ]

        for section_data in contact_sections:
            section, created = ContactPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Contact section "{section_data["title"]}" created')

        # Themes Page Sections
        themes_sections = [
            {
                'section_type': 'hero',
                'title': 'Browse Themes',
                'subtitle': 'Discover thousands of professional themes and templates',
                'content': 'Find the perfect theme for your next project from our curated collection.',
                'order': 1,
            },
        ]

        for section_data in themes_sections:
            section, created = ThemesPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Themes section "{section_data["title"]}" created')

        # Template Page Sections
        template_sections = [
            {
                'section_type': 'hero',
                'title': 'HTML & UI Templates',
                'subtitle': 'Ready-to-use templates for modern websites',
                'content': 'Choose from our collection of HTML and UI templates.',
                'order': 1,
            },
        ]

        for section_data in template_sections:
            section, created = TemplatePageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Template section "{section_data["title"]}" created')

        # Login Page Sections
        login_sections = [
            {
                'section_type': 'hero',
                'title': 'Welcome Back',
                'subtitle': 'Sign in to your account',
                'content': 'Access your purchased themes and manage your account.',
                'order': 1,
            },
        ]

        for section_data in login_sections:
            section, created = LoginPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Login section "{section_data["title"]}" created')

        # Cart Page Sections
        cart_sections = [
            {
                'section_type': 'hero',
                'title': 'Shopping Cart',
                'subtitle': 'Review your selected items',
                'content': 'Your cart items are listed below.',
                'order': 1,
            },
        ]

        for section_data in cart_sections:
            section, created = CartPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Cart section "{section_data["title"]}" created')

        # Checkout Page Sections
        checkout_sections = [
            {
                'section_type': 'hero',
                'title': 'Checkout',
                'subtitle': 'Complete your purchase',
                'content': 'Please provide your billing information to complete the purchase.',
                'order': 1,
            },
        ]

        for section_data in checkout_sections:
            section, created = CheckoutPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Checkout section "{section_data["title"]}" created')

        # Payment Page Sections
        payment_sections = [
            {
                'section_type': 'hero',
                'title': 'Payment',
                'subtitle': 'Secure payment processing',
                'content': 'Your payment information is secure and encrypted.',
                'order': 1,
            },
        ]

        for section_data in payment_sections:
            section, created = PaymentPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Payment section "{section_data["title"]}" created')

        # Payment Success Page Sections
        success_sections = [
            {
                'section_type': 'hero',
                'title': 'Payment Successful!',
                'subtitle': 'Thank you for your purchase',
                'content': 'Your payment has been processed successfully.',
                'order': 1,
            },
            {
                'section_type': 'next_steps',
                'title': 'What\'s Next?',
                'subtitle': 'Download your themes',
                'content': 'You can now download your purchased themes from your account dashboard.',
                'order': 2,
            },
        ]

        for section_data in success_sections:
            section, created = PaymentSuccessPageContent.objects.get_or_create(
                section_type=section_data['section_type'],
                defaults=section_data
            )
            if created:
                self.stdout.write(f'+ Payment Success section "{section_data["title"]}" created')

        self.stdout.write(self.style.SUCCESS('All page content populated successfully!'))