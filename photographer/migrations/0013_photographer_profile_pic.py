# Generated by Django 5.1 on 2024-11-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0012_remove_photographer_rating_photographer_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pic/'),
        ),
    ]
