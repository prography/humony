# from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser, BaseUserManager, PermissionsMixin
# )
#
# class UserManager(BaseUserManager):
#     def create_user(self, email, password =None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         user = self.model(
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password) #change user pw
#         #user.staff = is_staff
#         #user.admin = is_admin
#         #user.active = is_active
#         user.save(using=self._db)
#         return user
#
#  #   def create_staffuser(self, email, password=None):
#  #       user = self.create_user(
#  #           email,
#  #           password=password,
#  #       )
#  #       user.is_staff = True
#  #       user.save(using=self._db)
#  #       return user
#
#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email=email,
#             password=password,
#         )
#
#        # user.is_staff = True,
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
# # 이게 customuser
# class User(AbstractBaseUser, PermissionsMixin):
#     #username = models.CharField()
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     #full_name = models.CharField(max_length=255, blank = True, null=True)
#     is_active = models.BooleanField(default=True) # can login
#    # is_staff = models.BooleanField(default=False) #staff user non superuser
#     is_admin = models.BooleanField(default=False) #superuser
#
#     # username_field and pw are required by default
#     USERNAME_FIELD = 'email' #username
#     REQUIRED_FIELDS = [] #['full name'] #python manage.py createsuperuser
#
#     objects = UserManager()
#
#     def _str_(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.email
#
#     #def get_full_name(self):
#      #   return self.email
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_model_perms(self, app_label):
#         return True
#
#     @property
#     def is_staff(self):
#         return self.is_admin
#         #return self.staff
#
#     @property
#     def is_admin(self):
#         return self.admin
#
#     @property
#     def is_active(self):
#         return self.active
#
# #class Profile(models.Model):
# #    user = models.OneToOneField(User)
#     #extend extra user
#
# #class GusetEmail(models.Model):
# #    email = models.EmailField()
# #    active = models.BooleanField(default = True)
# #    update = models.DateTimeField(auto_now = True)
# #    timestamp = models.DateTimeField(auto_now_add = True)
#
# #    def _str_(self):
# #        return self.email
#
#
#
#
