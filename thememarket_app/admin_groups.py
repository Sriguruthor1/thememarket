from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect

class ThemeMarketAdminSite(AdminSite):
    site_header = 'ThemeMarket Admin'
    site_title = 'ThemeMarket Admin Portal'
    index_title = 'Welcome to ThemeMarket Administration'
    
    def get_app_list(self, request, app_label=None):
        """Organize admin models into logical groups"""
        app_list = super().get_app_list(request, app_label)
        
        # Custom organization of admin models matching requested layout
        custom_app_list = [
            {
                'name': 'Site-Wide Settings (Common Elements)',
                'app_label': 'site_config',
                'models': [
                    {'name': '📱 Site Settings', 'object_name': 'SiteSettings', 'admin_url': '/admin/thememarket_app/sitesettings/', 'add_url': '/admin/thememarket_app/sitesettings/add/'},
                    {'name': '🔝 Header Navigation', 'object_name': 'NavigationMenu', 'admin_url': '/admin/thememarket_app/navigationmenu/', 'add_url': '/admin/thememarket_app/navigationmenu/add/'},
                    {'name': '👣 Footer Sections', 'object_name': 'FooterSection', 'admin_url': '/admin/thememarket_app/footersection/', 'add_url': '/admin/thememarket_app/footersection/add/'},
                    {'name': '🔗 Social Links', 'object_name': 'SocialLink', 'admin_url': '/admin/thememarket_app/sociallink/', 'add_url': '/admin/thememarket_app/sociallink/add/'},
                    {'name': '📞 Contact Information', 'object_name': 'ContactInfo', 'admin_url': '/admin/thememarket_app/contactinfo/', 'add_url': '/admin/thememarket_app/contactinfo/add/'},
                ]
            },
            {
                'name': 'Home Page',
                'app_label': 'home_page',
                'models': [
                    {'name': '🎯 Hero Banner', 'object_name': 'HeroBanner', 'admin_url': '/admin/thememarket_app/herobanner/', 'add_url': '/admin/thememarket_app/herobanner/add/'},
                    {'name': '📂 Categories Section', 'object_name': 'CategorySection', 'admin_url': '/admin/thememarket_app/categorysection/', 'add_url': '/admin/thememarket_app/categorysection/add/'},
                    {'name': '⭐ Featured Section', 'object_name': 'FeaturedSection', 'admin_url': '/admin/thememarket_app/featuredsection/', 'add_url': '/admin/thememarket_app/featuredsection/add/'},
                    {'name': '🔥 Popular Section', 'object_name': 'PopularSection', 'admin_url': '/admin/thememarket_app/popularsection/', 'add_url': '/admin/thememarket_app/popularsection/add/'},
                    {'name': '🆕 New Section', 'object_name': 'NewSection', 'admin_url': '/admin/thememarket_app/newsection/', 'add_url': '/admin/thememarket_app/newsection/add/'},
                    {'name': '💡 Why Choose Us', 'object_name': 'WhyChooseSection', 'admin_url': '/admin/thememarket_app/whychoosesection/', 'add_url': '/admin/thememarket_app/whychoosesection/add/'},
                    {'name': '📧 Newsletter Section', 'object_name': 'NewsletterSection', 'admin_url': '/admin/thememarket_app/newslettersection/', 'add_url': '/admin/thememarket_app/newslettersection/add/'},
                    {'name': '💬 Testimonials Section', 'object_name': 'TestimonialsSection', 'admin_url': '/admin/thememarket_app/testimonialssection/', 'add_url': '/admin/thememarket_app/testimonialssection/add/'},
                ]
            },
            {
                'name': 'About Page',
                'app_label': 'about_page',
                'models': [
                    {'name': '🎯 Hero Section', 'object_name': 'AboutHero', 'admin_url': '/admin/thememarket_app/abouthero/', 'add_url': '/admin/thememarket_app/abouthero/add/'},
                    {'name': '🎯 Mission Section', 'object_name': 'AboutMission', 'admin_url': '/admin/thememarket_app/aboutmission/', 'add_url': '/admin/thememarket_app/aboutmission/add/'},
                    {'name': '💫 Values Section', 'object_name': 'AboutValues', 'admin_url': '/admin/thememarket_app/aboutvalues/', 'add_url': '/admin/thememarket_app/aboutvalues/add/'},
                    {'name': '👥 Team Section', 'object_name': 'AboutTeam', 'admin_url': '/admin/thememarket_app/aboutteam/', 'add_url': '/admin/thememarket_app/aboutteam/add/'},
                ]
            },
            {
                'name': 'Contact Page',
                'app_label': 'contact_page',
                'models': [
                    {'name': '🎯 Hero Section', 'object_name': 'ContactHero', 'admin_url': '/admin/thememarket_app/contacthero/', 'add_url': '/admin/thememarket_app/contacthero/add/'},
                    {'name': '📝 Contact Form', 'object_name': 'ContactForm', 'admin_url': '/admin/thememarket_app/contactform/', 'add_url': '/admin/thememarket_app/contactform/add/'},
                    {'name': '🏢 Office Information', 'object_name': 'ContactOffice', 'admin_url': '/admin/thememarket_app/contactoffice/', 'add_url': '/admin/thememarket_app/contactoffice/add/'},
                ]
            },
            {
                'name': 'Themes Page',
                'app_label': 'themes_page',
                'models': [
                    {'name': '🎯 Hero Section', 'object_name': 'ThemesHero', 'admin_url': '/admin/thememarket_app/themeshero/', 'add_url': '/admin/thememarket_app/themeshero/add/'},
                    {'name': '🔍 Filter Section', 'object_name': 'ThemesFilter', 'admin_url': '/admin/thememarket_app/themesfilter/', 'add_url': '/admin/thememarket_app/themesfilter/add/'},
                    {'name': '📱 Grid Settings', 'object_name': 'ThemesGrid', 'admin_url': '/admin/thememarket_app/themesgrid/', 'add_url': '/admin/thememarket_app/themesgrid/add/'},
                    {'name': '📂 Categories', 'object_name': 'Category', 'admin_url': '/admin/thememarket_app/category/', 'add_url': '/admin/thememarket_app/category/add/'},
                    {'name': '🎨 Themes', 'object_name': 'Theme', 'admin_url': '/admin/thememarket_app/theme/', 'add_url': '/admin/thememarket_app/theme/add/'},
                ]
            },
            {
                'name': 'Templates Page',
                'app_label': 'template_page',
                'models': [
                    {'name': '🎯 Hero Section', 'object_name': 'TemplatesHero', 'admin_url': '/admin/thememarket_app/templateshero/', 'add_url': '/admin/thememarket_app/templateshero/add/'},
                    {'name': '🌐 HTML Templates', 'object_name': 'HTMLTemplatesSection', 'admin_url': '/admin/thememarket_app/htmltemplatessection/', 'add_url': '/admin/thememarket_app/htmltemplatessection/add/'},
                    {'name': '💻 UI Templates', 'object_name': 'UITemplatesSection', 'admin_url': '/admin/thememarket_app/uitemplatessection/', 'add_url': '/admin/thememarket_app/uitemplatessection/add/'},
                ]
            },
            {
                'name': 'Account Pages',
                'app_label': 'account_pages',
                'models': [
                    {'name': '🔑 Login Page', 'object_name': 'LoginPageContent', 'admin_url': '/admin/thememarket_app/loginpagecontent/', 'add_url': '/admin/thememarket_app/loginpagecontent/add/'},
                ]
            },
            {
                'name': 'Shopping Pages',
                'app_label': 'shopping_pages',
                'models': [
                    {'name': '🛍️ Cart Page', 'object_name': 'CartPageContent', 'admin_url': '/admin/thememarket_app/cartpagecontent/', 'add_url': '/admin/thememarket_app/cartpagecontent/add/'},
                    {'name': '📝 Checkout Page', 'object_name': 'CheckoutPageContent', 'admin_url': '/admin/thememarket_app/checkoutpagecontent/', 'add_url': '/admin/thememarket_app/checkoutpagecontent/add/'},
                    {'name': '💳 Payment Page', 'object_name': 'PaymentPageContent', 'admin_url': '/admin/thememarket_app/paymentpagecontent/', 'add_url': '/admin/thememarket_app/paymentpagecontent/add/'},
                    {'name': '✅ Success Page', 'object_name': 'PaymentSuccessPageContent', 'admin_url': '/admin/thememarket_app/paymentsuccesspagecontent/', 'add_url': '/admin/thememarket_app/paymentsuccesspagecontent/add/'},
                ]
            },
            {
                'name': 'Other Pages',
                'app_label': 'other_pages',
                'models': [
                    {'name': '📑 Static Pages', 'object_name': 'Page', 'admin_url': '/admin/thememarket_app/page/', 'add_url': '/admin/thememarket_app/page/add/'},
                ]
            },
        ]

        return custom_app_list

# Create custom admin site instance
admin_site = ThemeMarketAdminSite(name='thememarket_admin')