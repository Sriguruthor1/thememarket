#!/usr/bin/env python
"""
Test script to verify image paths and Django setup
"""
import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).resolve().parent
sys.path.append(str(project_dir))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thememarket_project.settings')

import django
django.setup()

from django.conf import settings
from django.contrib.staticfiles import finders

def test_static_files():
    """Test if static files are properly configured"""
    print("=== Django Static Files Test ===")
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    
    # Test critical images
    critical_images = [
        'images/Frame 1410119443.png',
        'images/Frame 1410119442.png',
        'images/Frame 1410119443 (1).png',
        'images/Themes Images/Dishcovery-Food-Recipe-Hero-Section-Graphics-75526817-1-1-580x387.jpg',
        'images/Themes Images/website-template-business-marketing.jpg',
        'images/Themes Images/hero-header-travel-agency-1024x683.jpg'
    ]
    
    print("\n=== Testing Critical Images ===")
    for image_path in critical_images:
        found = finders.find(image_path)
        status = "[FOUND]" if found else "[MISSING]"
        print(f"{status}: {image_path}")
        if found:
            print(f"    Location: {found}")
    
    # Check if images directory exists
    static_dir = settings.STATICFILES_DIRS[0]
    images_dir = static_dir / 'images'
    print(f"\n=== Images Directory Check ===")
    print(f"Images directory exists: {images_dir.exists()}")
    
    if images_dir.exists():
        image_count = len(list(images_dir.rglob('*.*')))
        print(f"Total image files found: {image_count}")
        
        # List some sample images
        print("\nSample images:")
        for i, img_file in enumerate(images_dir.rglob('*.png')):
            if i < 5:  # Show first 5 PNG files
                print(f"  - {img_file.relative_to(static_dir)}")

def test_urls():
    """Test URL configuration"""
    print("\n=== URL Configuration Test ===")
    try:
        from django.urls import reverse
        urls_to_test = ['home', 'themes', 'template', 'about', 'contact', 'login']
        
        for url_name in urls_to_test:
            try:
                url = reverse(url_name)
                print(f"[OK] {url_name}: {url}")
            except Exception as e:
                print(f"[ERROR] {url_name}: {e}")
    except Exception as e:
        print(f"URL test failed: {e}")

if __name__ == '__main__':
    test_static_files()
    test_urls()
    print("\n=== Test Complete ===")
    print("If all critical images show '✓ FOUND', your setup is correct!")
    print("Run 'python manage.py runserver' to start the development server.")