import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thememarket_project.settings')
django.setup()

from django.contrib.auth.models import User

# Check existing users
users = User.objects.all()
print("Existing users:")
for user in users:
    print(f"Username: {user.username}, Email: {user.email}, Is superuser: {user.is_superuser}")

# Create or update admin user
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'is_superuser': True,
        'is_staff': True,
    }
)

if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print("\nNew admin user created:")
else:
    admin_user.set_password('admin123')
    admin_user.is_superuser = True
    admin_user.is_staff = True
    admin_user.save()
    print("\nAdmin user updated:")

print(f"Username: admin")
print(f"Password: admin123")
print(f"Email: {admin_user.email}")
print(f"Is superuser: {admin_user.is_superuser}")
print(f"Is staff: {admin_user.is_staff}")