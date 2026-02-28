from django.db import models

# Note: Django provides a built-in User model via django.contrib.auth.models.User
# No need to create a custom User model unless you need additional fields.
# If you need to extend the User model, use a OneToOneField relationship
# or create a custom user model that inherits from AbstractUser.