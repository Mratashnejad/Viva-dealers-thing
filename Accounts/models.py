
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

# hook in the New Manager to our Model


class User(AbstractBaseUser):  # from step 2
    ...
    objects = UserManager()


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active


# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from phonenumber_field.modelfields import PhoneNumberField


# class UserManager(BaseUserManager):
#     def create_user(self, phone_number, email, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError("User Must have an Email Address")
#         if not password:
#             raise ValueError("User Must have a Password")
#         if not phone_number:
#             raise ValueError("User Must have a Phone Number")
#         user_obj = self.model(email=self.normalize_email(email))
#         user_obj.set_password(password)  # change user password
#         user_obj.phone_number(phonenumber_field)
#         user_obj.staff = is_staff
#         user_obj.active = is_active
#         user_obj.admin = is_admin
#         user_obj.save(using=self._db)
#         return user_obj

#     # staff user
#     def create_staffuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             phone_number=PhoneNumberField,
#             is_staff=True
#         )
#         return user
#     # admin user

#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             phone_number=PhoneNumberField,
#             is_staff=True,
#             is_admin=True
#         )
#         return user


# class User(AbstractBaseUser):
#     email = models.EmailField(max_length=255, unique=True)
#     # full_name = models.CharField(max_length=255, blank=True, null=True)
#     active = models.BooleanField(default=True)  # can log in
#     staff = models.BooleanField(default=False)  # staff user non super user
#     admin = models.BooleanField(default=False)  # super user
#     timestamp = models.DateTimeField(auto_now_add=True)
#     phone_number = PhoneNumberField()

#     USERNAME_FIELD = 'email'  # username
#     REQUIRED_FIELDS = []  # FULL_NAME
#     object = UserManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.email

#     def get_short_name(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
