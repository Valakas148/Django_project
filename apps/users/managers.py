from django.contrib.auth.models import UserManager as UManager


class UserManager(UManager):

    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields['is_active'] is not True:
            raise ValueError('Admin/Superuser must have is_active=True')
        if extra_fields['is_staff'] is not True:
            raise ValueError('Admin/Superuser must have is_staff=True')
        if extra_fields['is_admin'] is not True:
            raise ValueError('Admin/Superuser must have is_admin=True')

        user = self.create_user(email, password, **extra_fields)
        return user

    def create_seller(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_seller', True)

        if extra_fields['is_active'] is not True:
            raise ValueError('User-Role Seller must have is_active=True')
        if extra_fields['is_seller'] is not True:
            raise ValueError('User-Role Seller must have is_seller=True')

        user = self.create_user(email, password, **extra_fields)
        return user

    def create_manager(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_manager', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields['is_active'] is not True:
            raise ValueError('Manager must have is_active=True')
        if extra_fields['is_staff'] is not True:
            raise ValueError('Manager must have is_staff=True')
        if extra_fields['is_manager'] is not True:
            raise ValueError('Manager must have is_manager=True')

        user = self.create_user(email, password, **extra_fields)
        return user
