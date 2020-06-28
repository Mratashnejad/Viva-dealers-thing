from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User Must have an Email Address")
        if not password:
            raise ValueError("User Must have a Password")
        user_obj = self.model(email=self.normalize(email))
        user_obj.set_password(password)  # change user password
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj

        #staff user 
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,

        )

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)  # can log in
    staff = models.BooleanField(default=False)  # staff user non super user
    admin = models.BooleanField(default=False)  # super user
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # username
    REQUIRED_FIELDS = []  # FULL_NAME
    object = UserManager()

    def __str__(self):
        return super().__str__()

    def get_full_name(self):
        return

    def get_short_name(self):
        return

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Profile(models.model):
    user = models.OneToOneField(User)
    # PhoneNumber = models.
