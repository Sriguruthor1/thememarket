from django.db import models
from django.core.validators import URLValidator
from tinymce.models import HTMLField

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="ThemeMarket")
    site_tagline = models.CharField(max_length=200, default="Build Stunning Websites Faster")
    logo_text = models.CharField(max_length=50, default="ThemeMarket")
    primary_color = models.CharField(max_length=7, default="#5c2dd5")
    secondary_color = models.CharField(max_length=7, default="#7b3fe4")
    accent_color = models.CharField(max_length=7, default="#4ade80")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return self.site_name

class NavigationMenu(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Navigation Menu"
        verbose_name_plural = "Navigation Menus"
    
    def __str__(self):
        return self.title

class HeroSection(models.Model):
    badge_text = models.CharField(max_length=100, default="NEW")
    main_title = models.CharField(max_length=200, default="Build Stunning Websites Faster")
    highlighted_text = models.CharField(max_length=100, default="Faster")
    description = HTMLField(default="Discover premium themes and templates for your next project")
    search_placeholder = models.CharField(max_length=100, default="Search for themes, templates, plugins...")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"
    
    def __str__(self):
        return self.main_title

class HeroStats(models.Model):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.CASCADE, related_name='stats')
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class (e.g., fas fa-users)")
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Hero Stat"
        verbose_name_plural = "Hero Stats"
    
    def __str__(self):
        return f"{self.number} {self.label}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = HTMLField(blank=True)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class")
    color = models.CharField(max_length=7, default="#5c2dd5")
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Theme(models.Model):
    THEME_TYPES = [
        ('wordpress', 'WordPress Theme'),
        ('html', 'HTML Template'),
        ('ui', 'UI Template'),
        ('plugin', 'Plugin'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='themes')
    theme_type = models.CharField(max_length=20, choices=THEME_TYPES, default='wordpress')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='themes/', blank=True, null=True)
    preview_url = models.URLField(blank=True, validators=[URLValidator()])
    download_url = models.URLField(blank=True, validators=[URLValidator()])
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    downloads = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Theme"
        verbose_name_plural = "Themes"
    
    def __str__(self):
        return self.title
    
    @property
    def discount_percentage(self):
        if self.original_price and self.original_price > self.price:
            return int(((self.original_price - self.price) / self.original_price) * 100)
        return 0

class ThemeImage(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='theme_images/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Theme Image"
        verbose_name_plural = "Theme Images"
    
    def __str__(self):
        return f"{self.theme.title} - Image {self.order}"

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = HTMLField()
    meta_description = models.CharField(max_length=160, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
    
    def __str__(self):
        return self.title

class FooterSection(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Footer Section"
        verbose_name_plural = "Footer Sections"
    
    def __str__(self):
        return self.title

class FooterLink(models.Model):
    section = models.ForeignKey(FooterSection, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"
    
    def __str__(self):
        return f"{self.section.title} - {self.title}"

class SocialLink(models.Model):
    SOCIAL_PLATFORMS = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('github', 'GitHub'),
    ]
    
    platform = models.CharField(max_length=20, choices=SOCIAL_PLATFORMS)
    url = models.URLField(validators=[URLValidator()])
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
    
    def __str__(self):
        return self.platform.title()

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    content = HTMLField()
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.name} - {self.company}"

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    working_hours = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
    
    def __str__(self):
        return f"Contact Info - {self.email}"

# HOME PAGE MODELS
class HeroBanner(models.Model):
    badge_text = models.CharField(max_length=50, default="NEW")
    main_title = models.CharField(max_length=200)
    highlighted_word = models.CharField(max_length=50, help_text="Word to highlight in title")
    subtitle = models.TextField()
    search_placeholder = models.CharField(max_length=100)
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Hero Banner"
        verbose_name_plural = "Hero Banners"
    
    def __str__(self):
        return self.main_title

class HeroImage(models.Model):
    hero = models.ForeignKey(HeroBanner, on_delete=models.CASCADE, related_name='hero_images')
    image = models.ImageField(upload_to='hero_images/')
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    is_large = models.BooleanField(default=False, help_text="Large template image")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Hero Image"
        verbose_name_plural = "Hero Images"
    
    def __str__(self):
        return f"{self.title} - {self.category}"

class CategorySection(models.Model):
    title = models.CharField(max_length=200, default="Browse by Category")
    subtitle = models.CharField(max_length=300, default="Find the perfect theme for your project")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Category Section"
        verbose_name_plural = "Category Sections"
    
    def __str__(self):
        return self.title

class FeaturedSection(models.Model):
    title = models.CharField(max_length=200, default="Featured Themes")
    subtitle = models.CharField(max_length=300, default="Hand-picked themes by our team")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Featured Section"
        verbose_name_plural = "Featured Sections"
    
    def __str__(self):
        return self.title

class PopularSection(models.Model):
    title = models.CharField(max_length=200, default="Popular Themes")
    subtitle = models.CharField(max_length=300, default="Most downloaded themes")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Popular Section"
        verbose_name_plural = "Popular Sections"
    
    def __str__(self):
        return self.title

class NewSection(models.Model):
    title = models.CharField(max_length=200, default="New Themes")
    subtitle = models.CharField(max_length=300, default="Latest additions to our collection")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "New Section"
        verbose_name_plural = "New Sections"
    
    def __str__(self):
        return self.title

class WhyChooseSection(models.Model):
    title = models.CharField(max_length=200, default="Why Choose ThemeMarket?")
    subtitle = models.CharField(max_length=300, default="Everything you need to build amazing websites")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Why Choose Section"
        verbose_name_plural = "Why Choose Sections"
    
    def __str__(self):
        return self.title

class FeatureCard(models.Model):
    section = models.ForeignKey(WhyChooseSection, on_delete=models.CASCADE, related_name='features')
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class")
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_color = models.CharField(max_length=7, default="#e3f7e3")
    icon_color = models.CharField(max_length=7, default="#2ecc71")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Feature Card"
        verbose_name_plural = "Feature Cards"
    
    def __str__(self):
        return self.title

class NewsletterSection(models.Model):
    title = models.CharField(max_length=200, default="Stay Updated")
    subtitle = models.TextField(default="Get the latest themes, exclusive deals, and design inspiration delivered to your inbox weekly")
    email_placeholder = models.CharField(max_length=100, default="Enter your email")
    button_text = models.CharField(max_length=50, default="Subscribe")
    privacy_text = models.TextField(default="By subscribing, you agree to our Privacy Policy and consent to receive updates")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Newsletter Section"
        verbose_name_plural = "Newsletter Sections"
    
    def __str__(self):
        return self.title

class TestimonialsSection(models.Model):
    title = models.CharField(max_length=200, default="What Our Customers Say")
    subtitle = models.CharField(max_length=300, default="Join thousands of satisfied customers")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Testimonials Section"
        verbose_name_plural = "Testimonials Sections"
    
    def __str__(self):
        return self.title

class CustomerTestimonial(models.Model):
    section = models.ForeignKey(TestimonialsSection, on_delete=models.CASCADE, related_name='testimonials')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    content = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Customer Testimonial"
        verbose_name_plural = "Customer Testimonials"
    
    def __str__(self):
        return f"{self.name} - {self.position}"

# ABOUT PAGE MODELS
class AboutHero(models.Model):
    title = models.CharField(max_length=200, default="About ThemeMarket")
    subtitle = models.TextField(default="Your premier destination for high-quality website themes and templates")
    description = models.TextField()
    background_image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "About Hero"
        verbose_name_plural = "About Heroes"
    
    def __str__(self):
        return self.title

class AboutMission(models.Model):
    title = models.CharField(max_length=200, default="Our Mission")
    subtitle = models.CharField(max_length=300, default="Democratizing web design")
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "About Mission"
        verbose_name_plural = "About Missions"
    
    def __str__(self):
        return self.title

class AboutValues(models.Model):
    title = models.CharField(max_length=200, default="Why Choose Us?")
    subtitle = models.CharField(max_length=300, default="What sets us apart")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "About Values"
        verbose_name_plural = "About Values"
    
    def __str__(self):
        return self.title

class ValueItem(models.Model):
    values_section = models.ForeignKey(AboutValues, on_delete=models.CASCADE, related_name='values')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Value Item"
        verbose_name_plural = "Value Items"
    
    def __str__(self):
        return self.title

class AboutTeam(models.Model):
    title = models.CharField(max_length=200, default="Our Team")
    subtitle = models.CharField(max_length=300, default="Meet the people behind ThemeMarket")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "About Team"
        verbose_name_plural = "About Teams"
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    team_section = models.ForeignKey(AboutTeam, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/')
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
    
    def __str__(self):
        return f"{self.name} - {self.position}"

# CONTACT PAGE MODELS
class ContactHero(models.Model):
    title = models.CharField(max_length=200, default="Get in Touch")
    subtitle = models.TextField(default="Have questions about our themes or need support? We are here to help!")
    description = models.TextField()
    background_image = models.ImageField(upload_to='contact/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Contact Hero"
        verbose_name_plural = "Contact Heroes"
    
    def __str__(self):
        return self.title

class ContactForm(models.Model):
    title = models.CharField(max_length=200, default="Send us a Message")
    subtitle = models.CharField(max_length=300, default="We'll get back to you within 24 hours")
    name_placeholder = models.CharField(max_length=100, default="Your Name")
    email_placeholder = models.CharField(max_length=100, default="Your Email")
    subject_placeholder = models.CharField(max_length=100, default="Subject")
    message_placeholder = models.CharField(max_length=100, default="Your Message")
    button_text = models.CharField(max_length=50, default="Send Message")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"
    
    def __str__(self):
        return self.title

class ContactOffice(models.Model):
    title = models.CharField(max_length=200, default="Support Hours")
    subtitle = models.CharField(max_length=300, default="When we are available")
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Contact Office"
        verbose_name_plural = "Contact Offices"
    
    def __str__(self):
        return self.title

# THEMES PAGE MODELS
class ThemesHero(models.Model):
    title = models.CharField(max_length=200, default="Browse Themes")
    subtitle = models.TextField(default="Discover thousands of professional themes and templates")
    description = models.TextField()
    background_image = models.ImageField(upload_to='themes/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Themes Hero"
        verbose_name_plural = "Themes Heroes"
    
    def __str__(self):
        return self.title

class ThemesFilter(models.Model):
    title = models.CharField(max_length=200, default="Filter Themes")
    subtitle = models.CharField(max_length=300, default="Find exactly what you're looking for")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Themes Filter"
        verbose_name_plural = "Themes Filters"
    
    def __str__(self):
        return self.title

class ThemesGrid(models.Model):
    title = models.CharField(max_length=200, default="All Themes")
    subtitle = models.CharField(max_length=300, default="Browse our complete collection")
    items_per_page = models.IntegerField(default=20)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Themes Grid"
        verbose_name_plural = "Themes Grids"
    
    def __str__(self):
        return self.title

# TEMPLATES PAGE MODELS
class TemplatesHero(models.Model):
    title = models.CharField(max_length=200, default="HTML & UI Templates")
    subtitle = models.TextField(default="Ready-to-use templates for modern websites")
    description = models.TextField()
    background_image = models.ImageField(upload_to='templates/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Templates Hero"
        verbose_name_plural = "Templates Heroes"
    
    def __str__(self):
        return self.title

class HTMLTemplatesSection(models.Model):
    title = models.CharField(max_length=200, default="HTML Templates")
    subtitle = models.CharField(max_length=300, default="Clean, modern HTML templates")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "HTML Templates Section"
        verbose_name_plural = "HTML Templates Sections"
    
    def __str__(self):
        return self.title

class UITemplatesSection(models.Model):
    title = models.CharField(max_length=200, default="UI Templates")
    subtitle = models.CharField(max_length=300, default="Beautiful UI components and templates")
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "UI Templates Section"
        verbose_name_plural = "UI Templates Sections"
    
    def __str__(self):
        return self.title

class LoginPageContent(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero Section'),
        ('login_form', 'Login Form Section'),
        ('register_form', 'Register Form Section'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Login Page Content"
        verbose_name_plural = "Login Page Contents"
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"

class CartPageContent(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero Section'),
        ('cart_items', 'Cart Items Section'),
        ('summary', 'Cart Summary Section'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Cart Page Content"
        verbose_name_plural = "Cart Page Contents"
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"

class CheckoutPageContent(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero Section'),
        ('billing_form', 'Billing Form Section'),
        ('order_summary', 'Order Summary Section'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Checkout Page Content"
        verbose_name_plural = "Checkout Page Contents"
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"

class PaymentPageContent(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero Section'),
        ('payment_form', 'Payment Form Section'),
        ('security_info', 'Security Information'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Payment Page Content"
        verbose_name_plural = "Payment Page Contents"
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"

class PaymentSuccessPageContent(models.Model):
    SECTION_TYPES = [
        ('hero', 'Hero Section'),
        ('success_message', 'Success Message Section'),
        ('next_steps', 'Next Steps Section'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Payment Success Page Content"
        verbose_name_plural = "Payment Success Page Contents"
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"