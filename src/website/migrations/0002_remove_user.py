# Generated migration to remove custom User model
# Django's built-in User model (django.contrib.auth.models.User) is used instead

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
