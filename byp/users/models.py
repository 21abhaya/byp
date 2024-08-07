
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for bookyourphotographer.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Phone No.")
    
    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


    #username = None  # type: ignore[assignment]

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    # objects: ClassVar[UserManager] = UserManager()

    