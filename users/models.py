# # accounts/models.py
# from django.conf import settings
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.db import models
#
# class UserManager(BaseUserManager):
#     def create_user(self, email=None, phone=None, password=None, **extra_fields):
#         if not email and not phone:
#             raise ValueError("Укажите email или телефон")
#         user = self.model(email=email, phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         """ Создание суперпользователя без обязательного поля `user_type` """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         # Убедитесь, что поля обязательные для суперпользователя
#         return self.create_user(email=email, password=password, **extra_fields)
#
# class User(AbstractBaseUser, PermissionsMixin):
#     USER_TYPE_CHOICES = (
#         ('buyer', 'Buyer'),
#         ('supplier', 'Supplier'),
#     )
#     email = models.EmailField(unique=True, null=True, blank=True)
#     phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
#     # user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True, blank=True)  # Сделаем его необязательным
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserManager()
#     USERNAME_FIELD = 'email'  # или можешь сделать кастомный backend
#     REQUIRED_FIELDS = ['user_type']
#
#     def __str__(self):
#         return self.email or self.phone
#
#
#
# class PurchaserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#
#     # Personal Information
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     uae_number = models.CharField(max_length=20)
#     nationality = models.CharField(max_length=100)
#     job_title = models.CharField(max_length=100)
#
#     # Company Information
#     company_name = models.CharField(max_length=255)
#     company_license_number = models.CharField(max_length=100)
#     city_of_license_issuing = models.CharField(max_length=100)
#
#     # Bank Information
#     bank_name = models.CharField(max_length=255)
#     account_name = models.CharField(max_length=255)
#     iban = models.CharField(max_length=34)
#
#     # Documents (uploaded files)
#     emirates_id = models.FileField(upload_to='documents/emirates_id/', blank=True, null=True)
#     company_license = models.FileField(upload_to='documents/company_license/', blank=True, null=True)
#     establishment_contract = models.FileField(upload_to='documents/establishment_contract/', blank=True, null=True)
#     credit_report = models.FileField(upload_to='documents/credit_report/', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.company_name} ({self.user.email or self.user.phone})"
#
#
# class SupplierProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=255)
#     country = models.CharField(max_length=100)
#     certifications = models.TextField(blank=True, null=True)
#     # другие поля для поставщика
