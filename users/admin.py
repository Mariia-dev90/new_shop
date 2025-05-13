# from django.contrib import admin
#
# # Register your models here.
# from django.contrib import admin
# from .models import User, PurchaserProfile, SupplierProfile
# from django.contrib.auth.admin import UserAdmin
#
# # Регистрация кастомного пользователя в админке
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ('email', 'phone', 'user_type', 'is_active', 'is_staff')
#     list_filter = ('is_active', 'is_staff', 'user_type')
#     search_fields = ('email', 'phone')
#     ordering = ('email',)
#
#     fieldsets = (
#         (None, {'fields': ('email', 'phone', 'password')}),
#         ('Personal info', {'fields': ('user_type', 'is_active', 'is_staff')}),
#         ('Permissions', {'fields': ('is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
#     add_fieldsets = (
#         (None, {'fields': ('email', 'phone', 'password1', 'password2')}),
#         ('Personal info', {'fields': ('user_type',)}),
#         ('Permissions', {'fields': ('is_active', 'is_staff')}),
#     )
#
# # Регистрация профиля покупателя
# class PurchaserProfileAdmin(admin.ModelAdmin):
#     list_display = ('company_name', 'user', 'first_name', 'last_name', 'uae_number')
#     search_fields = ('company_name', 'user__email', 'user__phone')
#
# # Регистрация профиля поставщика
# class SupplierProfileAdmin(admin.ModelAdmin):
#     list_display = ('company_name', 'user', 'country')
#     search_fields = ('company_name', 'user__email', 'user__phone', 'country')
#
# # Регистрируем модели в админке
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(PurchaserProfile, PurchaserProfileAdmin)
# admin.site.register(SupplierProfile, SupplierProfileAdmin)
