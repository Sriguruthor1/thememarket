#!/usr/bin/env python
"""
Django ThemeMarket Setup Script
This script sets up the complete Django admin panel for the ThemeMarket website.
"""

import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_django():
    """Setup Django environment"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thememarket_project.settings')
    django.setup()

def run_command(command):
    """Run a Django management command"""
    print(f"\n🔄 Running: {command}")
    try:
        execute_from_command_line(command.split())
        print(f"✅ Success: {command}")
        return True
    except Exception as e:
        print(f"❌ Error running {command}: {e}")
        return False

def create_superuser():
    """Create a superuser if it doesn't exist"""
    from django.contrib.auth.models import User
    
    if not User.objects.filter(is_superuser=True).exists():
        print("\n👤 Creating superuser...")
        User.objects.create_superuser(
            username='admin',
            email='admin@thememarket.com',
            password='admin123'
        )
        print("✅ Superuser created: admin / admin123")
    else:
        print("✅ Superuser already exists")

def main():
    """Main setup function"""
    print("🚀 Setting up Django ThemeMarket Admin Panel...")
    print("=" * 50)
    
    # Setup Django
    setup_django()
    
    # Run migrations
    if not run_command("python manage.py makemigrations"):
        return False
    
    if not run_command("python manage.py migrate"):
        return False
    
    # Create superuser
    create_superuser()
    
    # Setup initial data
    if not run_command("python manage.py setup_admin_data"):
        return False
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput"):
        print("⚠️  Static files collection failed, but continuing...")
    
    print("\n" + "=" * 50)
    print("🎉 Setup Complete!")
    print("\n📋 Next Steps:")
    print("1. Install requirements: pip install -r requirements.txt")
    print("2. Run server: python manage.py runserver")
    print("3. Access admin: http://localhost:8000/admin/")
    print("4. Login with: admin / admin123")
    print("5. Access website: http://localhost:8000/")
    print("\n💡 Admin Features:")
    print("• Manage all website content dynamically")
    print("• Upload images with automatic media handling")
    print("• Rich text editing with TinyMCE")
    print("• Organized admin sections for each page")
    print("• Live preview of changes")
    
    return True

if __name__ == "__main__":
    main()